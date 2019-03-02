# -*- coding: utf-8 -*-
# @Author: XIECHEN
# @Date:   2019-01-10 18:29:25
# @Last Modified by:   XIECHEN
# @Last Modified time: 2019-01-11 20:58:47

import arcpy
from arcpy import env
import math
import csv
import os
import pandas
import sys
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("Spatial")
# path2=r"C:\Users\XIECHEN\Desktop\sjpprogram\sjp_C.csv"#文件路径
# # 分割csv到文件夹
# with open(path2) as f: 
#         f_csv = csv.reader(f)
#         headers = next(f_csv)
#         print headers
#         count=0
#         Data=[]
#         fid=0
#         nid=-1
#         name=""
#     # for each row insert a point into null shp,including point and attributes 
#         for row in f_csv:
#             fid=row[0]
#             print row
#             if fid!= nid and count>0 :
#             	# 进行操作
#                 with open(r"C:\Users\XIECHEN\Desktop\sjpprogram\csv"+"//"+nid+"_"+name+'.csv','wb') as csvfile:
#                 	csv_write=csv.writer(csvfile)
#                 	csv_write.writerow(headers)
#                 	for data in Data:
#                 		print data
#                 		csv_write.writerow(data)
#                 Data=[]
#             else:
#             	# 读下去
#             	Data.append(row)
#             nid=row[0]
#             name=row[4]
#             count=count+1
# f.close()
# with open(r"C:\Users\XIECHEN\Desktop\sjpprogram\csv"+"//"+nid+"_"+name+'.csv','wb') as csvfile:
#     csv_write=csv.writer(csvfile)
#     csv_write.writerow(headers)
#     for data in Data:
#             csv_write.writerow(data)

path3=r"C:\Users\XIECHEN\Desktop\sjpprogram\csv"
env.workspace=r"C:\Users\XIECHEN\Desktop\sjpprogram"
mxd = arcpy.mapping.MapDocument(r"C:\Users\XIECHEN\Desktop\sjpprogram\test.mxd") #首先定义当前的mxd文档 #要用绝对路径要用绝对路径要用绝对路径
df = arcpy.mapping.ListDataFrames(mxd)[0]
def listdir(path, list_name):  
    for file in os.listdir(path):  
        file_path = os.path.join(path, file) 
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        elif os.path.splitext(file_path)[1]=='.csv' and os.path.split(file_path)[1]!='delete_data.csv':  
            list_name.append(file_path)  
filelist=[]
listdir(path3,filelist)
count2=14
for path2 in filelist:
	print path2
	ID1= (os.path.split(path2)[1]).split(".")[0].decode('GBK')
	# Set the local parameters
	inFeatures="zhen.lyr"
	layerName=ID1
	print type(ID1)
	inField="OBJECTID"
	joinField="OBJECTID_1"
	joinTable=path2

	arcpy.MakeFeatureLayer_management(inFeatures,layerName+".lyr")
	arcpy.AddJoin_management(layerName+".lyr",inField,joinTable,joinField)
	arcpy.FeatureClassToShapefile_conversion(layerName+".lyr", r"C:\Users\XIECHEN\Desktop\sjpprogram\shp2")
	# outLocation=r"C:\Users\XIECHEN\Desktop\sjpprogram\shp\data.mdb"
	# arcpy.ApplySymbologyFromLayer_management(layerName+".lyr","sample.lyr")
	path4="C://Users//XIECHEN//Desktop//sjpprogram//shp2//"+layerName+"_lyr.shp"
	print path4
	newLayer3=arcpy.mapping.Layer(path4)
	arcpy.RefreshActiveView()
	

	newLayer2=arcpy.mapping.Layer("sample.lyr")
	# newLayer=arcpy.mapping.Layer(layerName+".lyr")
	# print newLayer2.symbologyType

	arcpy.mapping.UpdateLayer(df, newLayer3, newLayer2, True)
	arcpy.mapping.AddLayer(df,newLayer3)

	for lyr2 in arcpy.mapping.ListLayers(mxd,"",df):
		print lyr2.name
		if lyr2.name!=u'城镇圈内镇':
	# 	print lyr2.symbologyType
	
			print ID1[0:4]+'__13';

			lyr2.symbology.valueField=ID1[0:4]+'__13'

			count2=count2+1
			lyr2.symbology.numClasses=5
	# 	if lyr2.isFeatureLayer:
	# 		sym=lyr2.symbology
	# 		print lyr2.symbology
	# 		print hasattr(sym,'renderer')
	# mxd.saveACopy("C:\\Users\\XIECHEN\\Desktop\\output2.mxd")
	# 		if hasattr(sym,'renderer'):
				
	# 			if sym.renderer.type=='SimpleRenderer':
	# 				sym.updateRenderer('GraduatedColorRender')
	# 				sym.renderer.classificationField = 's1'
	# 				sym.renderer.breakcount=8
	# 				sym.renderer.classficationMethod='NaturalBreaks'
	# 				lyr2.symbology=sym

	arcpy.mapping.ExportToJPEG(mxd,ID1+".jpg")
	# mxd.saveACopy("C:\\Users\\XIECHEN\\Desktop\\output2.mxd")
	for lyr2 in arcpy.mapping.ListLayers(mxd,"",df):
		if lyr2.name!=u'城镇圈内镇':

			arcpy.mapping.RemoveLayer(df,lyr2)

print "finished"

