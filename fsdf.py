# -*- coding: utf-8 -*-
# @Author: XIECHEN
# @Date:   2019-01-10 18:29:25
# @Last Modified by:   XIECHEN
# @Last Modified time: 2019-01-11 20:58:47
# import arcpy
# from arcpy import env
# import math
# import csv
# import os
import pandas
import sys
slashUStr="abc\\u0027\\u0026"
decodedUniChars = slashUStr.decode("unicode-escape") 
print type(decodedUniChars)
print dec
# path3=r"C:\Users\XIECHEN\Desktop\sjpprogram\csv"
# env.workspace=r"C:\Users\XIECHEN\Desktop\sjpprogram"
# mxd = arcpy.mp.ArcGISProject(r"C:\Users\XIECHEN\Desktop\sjpprogram\MyProject6\MyProject6.aprx") #首先定义当前的mxd文档 #要用绝对路径要用绝对路径要用绝对路径
# df = mxd.listMaps('Map')[0]
# print df
# for lyr in df.listLayers();
# 	print lyr.symbologyType
# 	print lyr.isFeatureLayer
# 	if lyr.isFeatureLayer:
# 	    sym = lyr.symbology
# 	    print hasattr(sym,'renderer')
# 	    if hasattr(sym, 'renderer'):
# 	      if sym.renderer.type == 'SimpleRenderer':
# 	        sym.updateRenderer('GraduatedColorsRenderer')
# 	        sym.renderer.breakCount = 6
	        
# 	        lyr.symbology = sym