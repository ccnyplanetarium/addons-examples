#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:12:12 2020

@author: james
"""

from astropy import units as u
from astropy.coordinates import SkyCoord

lat = 60
long = 360
lines=[]
group = 'group'
subgroup = 'subgroup'

for i in range(-lat, lat+1,30):
    for j in range(0, long+1,30):
        #name = 'image.png'
        name = 'image'+str(i)+'-'+str(j);
        object = SkyCoord(j*u.deg,i*u.deg,distance=10*u.pc, frame='icrs')
        
        pos = str(group)+","+ \
              str(subgroup)+","+ \
              str(name)+","+\
              str(1)+"," + \
              'image_target.png'+"," +\
              str(10)+"," + \
              str(j)+"," + \
              str(i)+"," + \
              str(90)
        lines.append(pos)
            

#print(lines)

afile = open('../skypositions2.csv', 'w')
afile.write("group, subgroup, name, x, y, z, scale, imageName, distance, ra, dec \n")
        
for line in lines:
    afile.write("%s\n" % line)

afile.close()

