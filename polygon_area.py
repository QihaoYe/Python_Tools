#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/8/15'

import numpy as np


def GetAreaOfPolyGon(points):
    area = 0

    if len(points) < 3:
        raise Exception("Need more than 3 points!")

    p1 = points[0]

    for i in range(1,len(points)-1):
        p2 = points[i]
        p3 = points[i+1]

        vec1 = p2 - p1
        vec2 = p3 - p2
        vecMult = np.linalg.det(np.append(vec1, vec2).reshape([2,2]))
        
        sign = 0
        if vecMult > 0:
            sign = 1
        elif vecMult < 0:
            sign = -1

        triArea = GetAreaOfTriangle(p1, p2, p3) * sign
        area += triArea

    return abs(area)


def GetAreaOfTriangle(p1, p2, p3):
    area = 0
    p1p2 = GetLineLength(p1, p2)
    p2p3 = GetLineLength(p2, p3)
    p3p1 = GetLineLength(p3, p1)
    s = (p1p2 + p2p3 + p3p1) / 2
    area = s * (s - p1p2) * (s - p2p3) * (s - p3p1)
    area = np.sqrt(area)
    return area


def GetLineLength(p1, p2):
    return np.linalg.norm(p1 - p2)

