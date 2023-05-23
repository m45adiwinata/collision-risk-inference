# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:40:53 2023

@author: BSA
"""


from flask import Flask, jsonify
from flask_cors import CORS
import json
from json import JSONEncoder
import numpy as np
import pandas as pd
from AIS import CPA
import CRI
# import colregs
import fuzzy_membership as fm
from typing import Any

app = Flask(__name__)
CORS(app)


class NumpyArrayEncoder(JSONEncoder):
    def default(self, o) -> Any:
        if isinstance(o, np.ndarray):
            return o.tolist()
        return JSONEncoder.default(self, o)


class Kapal:
    """
    This is a brief description of the MyClass.

    This class represents an example class. It has attributes and methods
    that perform certain operations.

    Attributes:
        _lon: longitude kapal.
        _lat: latitude kapal.
    """
    def __init__(self, _lon, _lat, _cog, _sog):
        self.LON = _lat
        self.LAT = _lon
        self.COG = _cog
        self.SOG = _sog

    def rad_point(self) -> np.ndarray:
        """
        Calculate point in radian

        Returns:
            x, y in numpy.ndarray
        """
        return np.radians((self.LAT, self.LON))


@app.route('/hello/', methods=['GET'])
def welcome() -> Any:
    """
    Perform testing

    Returns:
        The test result.
    """
    data = np.array(pd.read_excel("dummy kapal.xlsx", "Sheet1"))
    result = np.array([[0, 0, 0, 0, 0, 0, 0]])
    for i in range(data.shape[0] - 1):
        temp = data[i, 2] - data[i+1, 2]
        temp2 = data[i, 1] - data[i+1, 1]
        rbr = round(np.arctan2(temp2, temp) - data[i+1, 3], 8)
        rds = round(np.sqrt(np.power(temp2, 2) + np.power(temp, 2)), 8)
        rvl = round(data[i, 4] * np.sqrt(1 + (np.power(data[i+1, 4]/data[i, 4], 2) -
                    2 * (data[i+1, 4]/data[i, 4]) * np.cos(data[i, 3] - data[i+1, 3]))), 8)
        srl = round(np.arccos((data[i, 4] - data[i+1, 4])
                    * np.cos(data[i, 4] - data[i+1, 4])/rvl), 8)
        dcpa = round(rds * np.sin(srl - rbr - np.pi), 8)
        tcpa = round(rds * np.cos(srl - rbr - np.pi) / rvl, 8)
        vcd = round(result[i, 0] - rbr, 8)
        result = np.concatenate(
            (result, [[rbr, rds, rvl, srl, dcpa, tcpa, vcd]]), axis=0)
    result = np.concatenate((data, result), axis=1)
    hasil = {
        'data': result,
        'message': 'success'
    }
    json_dump = json.dumps(hasil, cls=NumpyArrayEncoder)
    return json_dump


@app.route('/calculate', methods=['GET'])
def calculate() -> Any:
    """
    Perform the calculation and return the result.

    Returns:
        The calculated result.
    """
    data = np.array(pd.read_excel("test.xlsx", "Sheet1"))
    kapals = []
    results = []
    radlatlong = []
    for d in data:
        temp = Kapal(d[1], d[2], d[3], d[4])
        kapals.append(temp)
    for i in range(len(data)//2):
        idx = i*2
        radlatlong.append(kapals[idx].rad_point())
        radlatlong.append(kapals[idx+1].rad_point())
        ais = CPA(kapals[idx+1], kapals[idx])
        # Bx, By = ais.BxyCalc()
        # x, y = ais.midxyCalc()
        haversine = ais.distance()
        # mid_lat, mid_long = ais.mid_point()
        bearing = ais.bearing()
        relSpeed = ais.relativeSpeed()
        Q = ais.Qvalue(relSpeed)
        relCourse = ais.relativeCourse(Q)
        DCPA, TCPA = ais.cpa()
        VCD = (bearing - relCourse) - bearing
        cri = CRI.getCRI(DCPA, TCPA, VCD, haversine)
        # level = CRI.getLevel(cri)
        # Colregs = colregs.getColregs(kapals[idx].COG, kapals[idx+1].COG, kapals[idx].SOG, kapals[idx+1].SOG)
        # results.append([haversine, mid_lat, mid_long, bearing, relSpeed, Q, relCourse, DCPA, TCPA, VCD, cri, level, Colregs])
        memDCPA, lvlDCPA = CRI.getMembership(DCPA, 'dcpa')
        memTCPA, lvlTCPA = CRI.getMembership(TCPA, 'tcpa')
        memVCD, lvlVCD = CRI.getMembership(VCD, 'vcd')
        memDr, lvlDr = CRI.getMembership(haversine, 'dr')
        results.append([haversine, memDr, lvlDr, DCPA, memDCPA,
                       lvlDCPA, TCPA, memTCPA, lvlTCPA, VCD, memVCD, lvlVCD])

    fm.createDummyPlot()
    return jsonify({
        'kapals': data.tolist(),
        'radlatlong': np.array(radlatlong, dtype='object').tolist(),
        'results': np.array(results, dtype='object').tolist(),
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
