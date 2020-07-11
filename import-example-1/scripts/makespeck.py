#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:41:09 2020

@author: james

This makes a speck file for a 5x5x5 grid, with a color key as the 4th column. The first 3 columns are x,y,z positions. 
"""


dim = 5

lines=[]

for i in range(-dim, dim+1):
    for j in range(-dim, dim+1):
        for k in range(-dim, dim+1):
            pos = str(i)+" "+str(j)+" "+str(k)+" "+str(abs(i))
            lines.append(pos)
            

#print(lines)

afile = open('../datapoints.speck', 'w')
afile.write("datavar 0 type\n")
        
for line in lines:
    afile.write("%s\n" % line)

afile.close()
