#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/03/15'


import urllib.request
from bs4 import BeautifulSoup

SHOW = 0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
info = input("Input your website:\n").split( )
if len(info) > 1:
    temp = info[1]
    if temp.lower() ==  'webcode'   :   SHOW = 1
    if temp.lower() ==  'hyperlink' :   SHOW = 2
url = info[0]
req = urllib.request.Request(url=url, headers=headers)

content = urllib.request.urlopen(req).read()
try:
    content = content.decode('utf-8')
except:
    content = content.decode('gbk')
soup = BeautifulSoup(content,'html.parser')

if SHOW == 0 or SHOW == 2:
    href_ = soup.find_all(name='a')
    Linked_Website = []
    Download_Link = []
    for each in href_:
        if str(each.get('href'))[:4]=='http':
            Linked_Website.append(each.get('href'))
        if str(each.get('href'))[:4]=='ed2k':
            Download_Link.append(each.get('href'))
    print('%s'%'[Linked Website]'.center(80,'-'))
    if Linked_Website:
        for each in Linked_Website:
            print(each)
    else:
        print('NONE')
    print('%s'%'[Linked Website]'.center(80,'-'))
    if Download_Link:
        print('%s'%'[Download  Link]'.center(80,'-'))
        for each in Download_Link:
            print(each)
        print('%s'%'[Download  Link]'.center(80,'-'))


if SHOW == 0 or SHOW == 1:
    print(soup.prettify())
