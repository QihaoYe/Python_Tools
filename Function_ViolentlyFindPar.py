#!/usr/bin/env python3
# coding: utf-8

from itertools import product

#Use this function to create all the combinations of the parameters you need to test
def FindBestPar(test):
    allproducts = list(product(*test))
    return allproducts

#A simple example of this function
a = FindBestPar([[1,2],[3,4],[5,6],[7,8],[9,10]])
for b in a:
    print(b)
