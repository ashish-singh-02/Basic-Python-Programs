# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:36:28 2018

@author: C-Ashish.Singh
"""



a = {1 : '1a', 2 : '2a', 3 : '3a'}
b = {1 : '1b', 2 : '2b', 3 : '3b'}
c = {1 : '1c', 2 : '2c', 3 : '3c'}

dic1 = {1 : a, 2 : b, 3 : c}

print(dic1[3][3])


l1 = (1,2,3,4,5)
l2 = [6,7,8,9]
l3 = [10,11,12,13,14]

dic2 = {1 : l1, 2 : l2, 3 : l3}

print(dic2[3][-3 :])