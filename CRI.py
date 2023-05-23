# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:59:40 2023

@author: Mugen
"""

from typing import Tuple

def getLevel(cri) -> str:
    level = '-'
    if cri >= 1:
        level = 'T'
    elif cri >= 0.66 and cri < 1:
        level = 'B'
    elif cri >= 0.33 and cri < 0.66:
        level = 'A'
    elif cri >= 0.01 and cri < 0.33:
        level = 'W'
    return level

def getCRI(dcpa, tcpa, vcd, dr) -> float:
    memDCPA, _ = getMembership(dcpa, 'dcpa')
    memTCPA, _ = getMembership(tcpa, 'tcpa')
    memVCD, _ = getMembership(vcd, 'vcd')
    memDr, _ = getMembership(dr, 'dr')
    cri = dcpa*memDCPA + tcpa*memTCPA + vcd*memVCD + dr*memDr
    
    return cri

def getMembership(val: float, param: str) -> Tuple[float, str]:
    level = ''
    if param == 'dcpa':
        if val <= 0 or (val > 0 and val <= 1.3):
            level = 'tabrakan'
        elif val > 1.3 and val <= 2.6:
            level = 'bahaya'
        elif val > 2.6 and val <= 3.9:
            level = 'ancaman'
        elif val > 3.9:
            level = 'waspada'
        memb = dcpaCategory(val, level)
    if param == 'tcpa':
        if val <= 11.5:
            level = 'tabrakan'
        elif val > 11.5 and val <= 22.9:
            level = 'bahaya'
        elif val > 22.9 and val <= 34.3:
            level = 'ancaman'
        elif val > 34.3:
            level = 'waspada'
        memb = tcpaCategory(val, level)
    if param == 'vcd':
        if val <= 0 or (val > 0 and val <= 30):
            level = 'tabrakan'
        elif val > 30 and val <= 50.2:
            level = 'bahaya'
        elif val > 50.2 and val <= 70.5:
            level = 'ancaman'
        elif val > 70.5:
            level = 'waspada'
        memb = vcdCategory(val, level)
    if param == 'dr':
        if val <= 0 or (val > 0 and val <= 1.2):
            level = 'tabrakan'
        elif val > 1.2 and val <= 2.1:
            level = 'bahaya'
        elif val > 2.1 and val <= 3.0:
            level = 'ancaman'
        elif val > 3.0:
            level = 'waspada'
        memb = drCategory(val, level)
        
    if len(level) > 0:
        return memb, level[0].upper()
    return memb, level
        
def dcpaCategory(dcpa, param) -> float:
    if param == 'tabrakan':
        if dcpa <= 0:
            return 1
        elif dcpa > 0 and dcpa <= 1.3:
            return (1.3-dcpa)/1.3
    elif param == 'bahaya':
        return (2.6-dcpa)/1.3
    elif param == 'ancaman':
        return (3.9-dcpa)/1.3
    elif param == 'waspada':
        return 0
    
def tcpaCategory(tcpa:float, param:str) -> float:
    print(param)
    if param == 'tabrakan':
        if tcpa <= 0:
            return 1
        elif tcpa > 0 and tcpa <= 11.5:
            return (11.5-tcpa)/11.5
    elif param == 'bahaya':
        return (22.9-tcpa)/11.4
    elif param == 'ancaman':
        return (34.3-tcpa)/11.4
    elif param == 'waspada':
        return 0
    
def vcdCategory(vcd, param) -> float:
    if param == 'tabrakan':
        if vcd <= 0:
            return 1
        elif vcd > 0 and vcd <= 30:
            return (30-vcd)/20.3
    elif param == 'bahaya':
        return (50.2-vcd)/20.2
    elif param == 'ancaman':
        return (70.5-vcd)/20.3
    elif param == 'waspada':
        return 0
    
def drCategory(vcd, param) -> float:
    if param == 'tabrakan':
        if vcd <= 0:
            return 1
        elif vcd > 0 and vcd <= 1.2:
            return (1.2-vcd)/1.2
    elif param == 'bahaya':
        return (2.1-vcd)/0.9
    elif param == 'ancaman':
        return (3.0-vcd)/0.9
    elif param == 'waspada':
        return 0