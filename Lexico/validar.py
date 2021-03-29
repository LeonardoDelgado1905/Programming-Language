# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:30:34 2021

@author: LeonardoDelgado
"""


fmia = open("miSalida.txt", 'r')
freal= open("real.txt", 'r')

lines = fmia.readlines()
linesR = freal.readlines()


for x in range(len(lines)):
    # lines[x] = lines.replace(' ', '')
    # linesR[x] = lines.replace(' ', '')
    if(lines[x] != linesR[x]):
        print("EROOR: " + str(x))
        print(lines[x])
        print(linesR[x])
        break
    