#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__date__ = '2017/9/19'


import numpy as np


MAX_LENGTH = 6
seed = 12345678
try:
    seed = int(input('Enter the seed: '))
except:
    pass
finally:
    print('seed  : %d' % seed)
    np.random.RandomState(seed)
    for i in range(80):
        holder = np.random.randint(48, 123, MAX_LENGTH)
        result = ''.join(chr(x) for x in holder if chr(x).isdigit() or chr(x).isalpha())
        print('result: %s' % result)