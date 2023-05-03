# -*- coding: utf-8 -*-
"""
Created on Thu May  4 02:24:09 2023

@author: Mugen
"""

import numpy as np

def getColregs(cogOS, cogTS, sogOS, sogTS) -> str:
    colregs = '-'
    diffcog = np.abs(cogOS - cogTS)
    if cogOS <= 5 and (diffcog >= 174 and diffcog < 186):
        colregs = 'Head-on'
    elif cogOS <= 45 and (diffcog >= 186 and diffcog < 210):
        colregs = 'Crossing'
    elif cogOS > 25 and sogOS > sogTS:
        colregs = 'Being Overtaking'
    elif sogOS > sogTS and cogOS < np.arcsin(0.924*sogTS/sogOS) and ((diffcog >= 0 and diffcog < 90) or (diffcog >= 270 and diffcog < 360)):
        colregs = 'Overtaking'
    
    return colregs