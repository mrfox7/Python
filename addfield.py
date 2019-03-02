# -*- coding: utf-8 -*-
# @Author: XIECHEN
# @Date:   2019-01-19 13:22:00
# @Last Modified by:   XIECHEN
# @Last Modified time: 2019-01-25 13:57:28
import csv
import os
# Import system modules
import arcpy
# Set environment settings
arcpy.env.workspace = r"C:\Users\XIECHEN\Desktop\park"


#获得dataframes留下的数据，存到mdb中
mxd = arcpy.mapping.MapDocument(r"C:\Users\XIECHEN\Desktop\park\point.mxd") #首先定义当前的mxd文档 #要用绝对路径要用绝对路径要用绝对路径
for lyr in arcpy.mapping.ListLayers(mxd):
    layername=lyr.name
    # add field
    fieldName1 = "user_ID"
    fieldLength = 10
    arcpy.AddField_management(lyr, fieldName1, "TEXT", field_length=fieldLength)
    layername2=layername.decode('utf-8')
    print layername2
    arcpy.CalculateField_management(lyr, fieldName1, layername2,"VB")
    #进行空间连接

    #export data to 要素集
    outLocation=r"C:\Users\XIECHEN\Desktop\park\Park.mdb\Point"
    outFeatureClass="user_"+layername
    # arcpy.FeatureClassToFeatureClass_conversion(lyr, outLocation, outFeatureClass)
    #空间连接
    join_features=r"C:\Users\XIECHEN\Desktop\park\Park.mdb\ParkArea\Merge_Park"
    out_feature_class=outLocation+"/"+outFeatureClass
    arcpy.SpatialJoin_analysis(lyr, join_features, out_feature_class)
