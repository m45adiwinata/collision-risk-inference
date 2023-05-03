# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:16:55 2023

@author: BSA
"""

import numpy as np
import pandas as pd

data = np.array(pd.read_excel("dummy kapal.xlsx", "Sheet1"))
result = np.array([[0, 0, 0, 0, 0, 0, 0]])
for i in range(data.shape[0] - 1):
    temp = data[i, 2] - data[i+1, 2]
    temp2 = data[i, 1] - data[i+1, 1]
    rbr = round(np.arctan2(temp2, temp) - data[i+1, 3], 8)
    rds = np.sqrt(np.power(temp2, 2) + np.power(temp, 2))
    rvl = data[i, 4] * np.sqrt(1 + (np.power(data[i+1, 4]/data[i, 4], 2) - 2 * (data[i+1, 4]/data[i, 4]) * np.cos(data[i, 3] - data[i+1, 3])))
    srl = np.arccos((data[i, 4] - data[i+1, 4]) * np.cos(data[i, 4] - data[i+1, 4])/rvl)
    dcpa = rds * np.sin(srl - rbr - np.pi)
    tcpa = rds * np.cos(srl - rbr - np.pi) / rvl
    vcd = result[i, 0] - rbr
    result = np.concatenate((result, [[rbr, rds, rvl, srl, dcpa, tcpa, vcd]]), axis=0)
    
result = np.concatenate((data, result), axis=1)