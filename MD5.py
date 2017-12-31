#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/08/06'


import hashlib


def MD5(text, time=1, left=1, length=32):
    n = 1
    m = hashlib.md5()
    while n<=time:
        m.update(text.encode('utf-8'))
        print(" MD5('%s')\n="%text,end='')
        text = m.hexdigest()
        print(text+'\t#Your MD5 code [%03d]'%n,end='\n ')
        for i in range(32):
            print((i+1)%10,end='')
        print('\t#Line for measuring')
        print()
        n += 1
    return text[left-1:left+length-1]


while True:
    Scanner = input('Please input text for MD5 encryption:\n')
    if Scanner == 'exit' or Scanner == '0':break
    print()
    if len(Scanner.split( ))>1:
        text = ''
        time = 1
        left = 1
        length = 32
        try:
            text = Scanner.split( )[0]
            time = int(Scanner.split( )[1])
            left = int(Scanner.split( )[2])
            length = int(Scanner.split( )[3])
        except:
            pass
        result = MD5(text, time, left, length)
        print(' RESULT\n='+result+'\n')
#    elif len(Scanner.split( )) and Scanner.split( )[0].isdigit():
#        text = ''
#        time = int(Scanner.split( )[0])
#        MD5(text, time)
    else:
        text = Scanner
        MD5(text)
