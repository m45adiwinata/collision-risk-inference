# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 20:04:07 2023

@author: BSA
"""

import pandas as pd
import numpy as np
from AIS import CPA
import CRI
import colregs

class Kapal:
    def __init__(self, LON, LAT, COG, SOG):
        self.LAT = LAT
        self.LON = LON
        self.COG = COG
        self.SOG = SOG
    
    def radPoint(self):
        return np.radians((self.LAT, self.LON))
        
data = np.array(pd.read_excel("test.xlsx", "Sheet1"))
kapals = []
for d in data:
    temp = Kapal(d[1], d[2], d[3], d[4])
    kapals.append(temp)
    
radlat_OS, radlong_OS = kapals[0].radPoint()
radlat_TS, radlong_TS = kapals[1].radPoint()

results = []
radlatlong = []
for i in range(len(data)//2):
    idx = i*2
    radlatlong.append(kapals[idx].radPoint())
    radlatlong.append(kapals[idx+1].radPoint())
    ais = CPA(kapals[idx+1], kapals[idx])
    Bx, By = ais.BxyCalc()
    x, y = ais.midxyCalc()
    haversine = ais.distance()
    mid_lat, mid_long = ais.mid_point()
    bearing = ais.bearing()
    relSpeed = ais.relativeSpeed()
    Q = ais.Qvalue(relSpeed)
    relCourse = ais.relativeCourse(Q)
    DCPA, TCPA = ais.cpa()
    VCD = (bearing - relCourse) - bearing
    cri = CRI.getCRI(DCPA, TCPA, VCD, haversine)
    level = CRI.getLevel(cri)
    Colregs = colregs.getColregs(kapals[idx].COG, kapals[idx+1].COG, kapals[idx].SOG, kapals[idx+1].SOG)
    results.append([haversine, mid_lat, mid_long, bearing, relSpeed, Q, relCourse, DCPA, TCPA, VCD, cri, level, Colregs])

results = np.array(results, dtype='object')

'''
ais = CPA(kapals[1], kapals[0])
Bx, By = ais.BxyCalc()
x, y = ais.midxyCalc()
haversine = ais.distance()
mid_lat, mid_long = ais.mid_point()
bearing = ais.bearing()
relSpeed = ais.relativeSpeed()
Q = ais.Qvalue(relSpeed)
relCourse = ais.relativeCourse(Q)
DCPA, TCPA = ais.cpa()
'''