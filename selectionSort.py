# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:11:55 2017

@author: C-Ashish.Singh
"""

def selectionSort(arr):
    l = len(arr)
    min = arr[0]
    for i in range(l):
        if (arr[i] < min):
            min = arr[i]
        for j in range(i,l):
            (arr[j], min) = (min, arr[j])
    return arr

arr = [9,8,7,6,5,4,1]

print(selectionSort(arr))
            