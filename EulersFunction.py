#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__date__ = '2017/10/09'


def generate_division(n):
    d = 2
    while d * d <= n:
        flag = 1
        while n % d is 0:
            if flag:
                yield d
            flag = 0
            n //= d
        d += 1
    if n > 1:
        yield n


def phi(n):
    assert n > 0
    
    for d in generate_division(n):
        n //= d
        n *= d - 1
    return n

# ---[test zone]---
# print(phi(10007))
for i in range(1, 101):
    print(i, phi(i))
