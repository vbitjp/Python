#!/usr/bin/env python3
# coding: utf-8
'''
ブールインデックス参照
'''
import numpy as np

arr = np.array([2, 4, 6, 8, 10]) 
print(arr[np.array([True, True, True, False, True])])  
arr = np.arange(16) 
print(arr[arr % 3 == 1])
print(arr[(arr % 3 == 0) + (arr % 5 == 0)])
print(arr[(arr % 3 == 0) * (arr % 5 == 0)])