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
              str(object.galactic.cartesian.x.value)+","+ \
              str(object.galactic.cartesian.y.value)+","+ \
              str(object.galactic.cartesian.z.value)+","+ \
              str(1)+"," + \
              'image_target.png'+"," +\
              str(object.galactic.l.value)+"," + \
              str(object.galactic.b.value)+"," + \
              str(10)+"," + \
              str(j)+"," + \
              str(i)
        lines.append(pos)
            

#print(lines)

afile = open('../skypositions.csv', 'w')
afile.write("group, subgroup, name, x, y, z, scale, imageName, l, b, distance, ra, dec \n")
        
for line in lines:
    afile.write("%s\n" % line)

afile.close()

