#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:50:42 2020

@author: james
"""



lat = 90
long = 360
lines=[]

for i in range(-lat, lat+1,15):
    for j in range(0, long+1,15):
        pos = "time holder," +str(i)+","+str(j)+","+"Point"+str(i)+str(j)
        lines.append(pos)
            

#print(lines)

afile = open('../globepositions.csv', 'w')
afile.write("time lat long label \n")
        
for line in lines:
    afile.write("%s\n" % line)

afile.close()

