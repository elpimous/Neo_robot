#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
#  A simple tool to find what values put in HSV mask, for opencv
#
#  Easy. Enter RGB value, and see automatic HSV conversion
#
#                   Vincent FOUCAULT 6 APRIL 2016
######################################################################

import os
import cv2
import numpy as np

os.system('clear')
print"\n\n  ****************************************************"
print"  *        AUTOMATIC BGR (Blue/Green/Red TO HSV CONVERSION           *"
print"  ****************************************************"
print"  *  enter here your RGB value (ex: 0,255,0)  "
a = input('  *  1st nombre >>> ')
b = input('  *  2nd nombre >>> ')
c = input('  *  3rd nombre >>> ')
print"  ****************************************************"
#Value = str(BRG).replace("(","").replace(")","")
print "  *  BGR value to convert : "+str(a)+"/"+str(b)+"/"+str(c)
print"  *"
color = np.uint8([[[a,b,c]]])
HSV = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
HSV = str(HSV).replace("[","").replace("]","")
print "  *  HSV conversion  --->  "+str(HSV)
print"  ****************************************************\n"

