# -*- coding: utf-8 -*-
"""
Created on Wed May  3 23:37:28 2023

@author: Mugen
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def createDummyPlot():
    dcpa_dum = np.arange(0, 4, 0.1)
    tcpa_dum = np.arange(0, 34.4, 0.1)
    vcd_dum = np.arange(9.7, 70.6, 0.1)
    dr_dum = np.arange(0.3, 3.1, 0.1)
    
    shape = [
        [0, 0, 1.3],
        [0, 1.3, 2.6],
        [1.3, 2.6, 3.9],
        [2.6, 3.9, 5]
    ]
    fuzzT, fuzzB, fuzzA, fuzzW = createFuzzPoints(dcpa_dum, shape)
    createPlot(dcpa_dum, [fuzzT, fuzzB, fuzzA, fuzzW], 'DCPA')
    
    shape = [
        [0, 0, 11.5],
        [0, 11.5, 22.9],
        [11.5, 22.9, 34.3],
        [22.9, 34.3, 45.7]
    ]
    fuzzT, fuzzB, fuzzA, fuzzW = createFuzzPoints(tcpa_dum, shape)
    createPlot(tcpa_dum, [fuzzT, fuzzB, fuzzA, fuzzW], 'TCPA')
    
    shape = [
        [9.7, 9.7, 30],
        [9.7, 30, 50.2],
        [30, 50.2, 70.5],
        [50.2, 70.5, 90.8]
    ]
    fuzzT, fuzzB, fuzzA, fuzzW = createFuzzPoints(vcd_dum, shape)
    createPlot(vcd_dum, [fuzzT, fuzzB, fuzzA, fuzzW], 'VCD')
    
    shape = [
        [0.3, 0.3, 1.2],
        [0.3, 1.2, 2.1],
        [1.2, 2.1, 3],
        [2.1, 3, 3.9]
    ]
    fuzzT, fuzzB, fuzzA, fuzzW = createFuzzPoints(dr_dum, shape)
    createPlot(dr_dum, [fuzzT, fuzzB, fuzzA, fuzzW], 'Dr')
    
def createFuzzPoints(arr, shapeCtrl):
    fuzzT = fuzz.trimf(arr, shapeCtrl[0])
    fuzzB = fuzz.trimf(arr, shapeCtrl[1])
    fuzzA = fuzz.trimf(arr, shapeCtrl[2])
    fuzzW = fuzz.trimf(arr, shapeCtrl[3])
    return fuzzT, fuzzB, fuzzA, fuzzW

def createPlot(arr, fuzz, plotname):
    plt.plot(arr, fuzz[0], 'r', linewidth=1.5)
    plt.plot(arr, fuzz[1], 'y', linewidth=1.5)
    plt.plot(arr, fuzz[2], 'b', linewidth=1.5)
    plt.plot(arr, fuzz[3], 'g', linewidth=1.5)
    plt.title('Membership Functions '+plotname)
    plt.ylabel('Membership Degree')
    plt.xlabel(plotname)
    plt.legend(['Tabrakan', 'Bahaya', 'Ancaman', 'Waspada'], loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig("Membership_"+plotname+".svg", bbox_inches='tight', dpi=150)
    plt.close()