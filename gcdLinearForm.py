#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__date__ = '2017/9/25'


import numpy as np
from math import gcd


def linear(a, b):
    if a < b:
        return linear(b, a)[::-1]
    n1 = np.array([1, 0])
    n2 = np.array([0, 1])
    d = gcd(a, b)
    while not b == d:
        k = a // b
        a, b = b, a - k * b
        n1, n2 = n2, n1 - k * n2
    return n2.tolist()


while 1:
    source = input('(a, b): ')
    if source.lower() in ['q', 'quit', 'exit']:
        break;
    a, b = [int(x) for x in source.split(' ')]
    d = gcd(a, b)
    l = linear(a, b)
    s = ('%d * a + %d * b' % (l[0], l[1])).replace('+ -', '- ')
    print('gcd(a, b) = gcd(%d, %d) = %d = %s' % (a, b, d, s))
