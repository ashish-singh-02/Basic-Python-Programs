# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:00:42 2018


-- Create a new array if elements at odd position are odd values in a given array

@author: C-Ashish.Singh
"""

arr = [9,8,7,6,5,4,1,3,4,6,6,8,10,1,3,5]
arr2 = []

my_list_len = len(arr)

for i in range(0,my_list_len) :
    if (i % 2 == 0 and arr[i] % 2 != 0):
        arr2.append(arr[i])
    

print(arr2)

