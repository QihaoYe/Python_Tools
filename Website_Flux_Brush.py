#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/10/27'


import sys
import urllib.request


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

url = input('Your website: ')
N = int(input('Brush time: '))

req = urllib.request.Request(url=url, headers=headers)
for i in range(N):
    urllib.request.urlopen(req)
    sys.stdout.write('%08.5f' % ((i + 1) * 100 / N) + '%\r')
    sys.stdout.flush()
