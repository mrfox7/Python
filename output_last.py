# -*- coding: utf-8 -*-
# @Author: XIECHEN
# @Date:   2019-01-10 18:29:25
# @Last Modified by:   XIECHEN
# @Last Modified time: 2019-01-11 20:58:47

import arcpy
import math
import csv
import os

arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("Spatial")
path = r"C:\Users\XIECHEN\Desktop\ilovexiexie"
arcpy.env.workspace = path
sym_layer = "1018_航中路.img.lyr"
sym_layer2="study_quads_lyr.lyr"
#df2=获得地铁站圈圈的格式
m = 0
mxd = arcpy.mapping.MapDocument("C:\\Users\\XIECHEN\\Desktop\\ilovexiexie\\output10.mxd") #首先定义当前的mxd文档 #要用绝对路径要用绝对路径要用绝对路径
df = arcpy.mapping.ListDataFrames(mxd)[0]

for lyr in arcpy.mapping.ListLayers(mxd):
    arcpy.ApplySymbologyFromLayer_management(lyr,sym_layer) #把"sym_layer"图层的图例应用到其他图层
    lyr.visible = False #关闭所有图层

# addLayer = arcpy.mapping.Layer("E:\\syq\\00 Master\\arcpy\\output\\9_homein_work\\huangpuriver.lyr")
# arcpy.mapping.AddLayer(df, addLayer, "BOTTOM") 
# addLayer = arcpy.mapping.Layer("E:\\syq\\00 Master\\arcpy\\output\\9_homein_work\\街道2000.lyr")
# arcpy.mapping.AddLayer(df, addLayer, "BOTTOM") 
L=[]
for root, dirs, files in os.walk(r'C:\Users\XIECHEN\Desktop\ilovexiexie\metrostation'):  
    for file in files:
        if os.path.splitext(file)[1]=='.shp':
            a= (os.path.join(root,file)).decode('GBK')
            L.append(a)
for lyr in arcpy.mapping.ListLayers(mxd,"",df):
    print(m)
    # print(lyr.name)
    lyr.visible = True #打开某个图层
    #寻找对应图层，lyr.name倒数"1018_航中路.img.lyr"，获得路径
    lyrname=lyr.name
    x = lyrname.split("_", 1)
    y = x[1].split(".",1)
    for str2 in L:
        station=(str2.split("\\"))[6].split(".")[0]
        if(station==y[0]):
            pathtrue=str2
            break
    # path2=
    #将shp转为lyr2
    lyrpath=r"C:\Users\XIECHEN\Desktop\ilovexiexie\lyr"+"\\"+station+".lyr"
    arcpy.MakeFeatureLayer_management(pathtrue, station+".lyr")
    # arcpy.SaveToLayerFile_management("study_quads_lyr", lyrpath, "ABSOLUTE")
    arcpy.ApplySymbologyFromLayer_management(station+".lyr",sym_layer2) 
    #再add
    addLayer = arcpy.mapping.Layer(station+".lyr")
    arcpy.mapping.AddLayer(df,addLayer)


    # addLayer = arcpy.mapping.Layer("E:\\syq\\00 Master\\arcpy\\output\\9_homein_work\\内环2000.lyr")
    # arcpy.mapping.AddLayer(df,addLayer,"TOP")
    # addLayer = arcpy.mapping.Layer("E:\\syq\\00 Master\\arcpy\\output\\9_homein_work\\中环2000.lyr")
    # arcpy.mapping.AddLayer(df,addLayer,"TOP")
    # addLayer = arcpy.mapping.Layer("E:\\syq\\00 Master\\arcpy\\output\\9_homein_work\\中心城区2000.lyr")
    # arcpy.mapping.AddLayer(df,addLayer,"TOP")
    # addLayer = arcpy.mapping.Layer("E:\\syq\\00 Master\\arcpy\\output\\9_homein_work\\metroline.lyr")
    # arcpy.mapping.AddLayer(df,addLayer,"TOP")
    # addLayer = arcpy.mapping.Layer("E:\\syq\\00 Master\\arcpy\\output\\9_homein_work\\metrostation.lyr")
    # arcpy.mapping.AddLayer(df,addLayer,"TOP")


    arcpy.mapping.ExportToJPEG(mxd, lyr.name+".jpg") #输出 
    # mxd.saveACopy("C:\\Users\\XIECHEN\\Desktop\\ilovexiexie\\output2.mxd")
    for lyr4 in arcpy.mapping.ListLayers(mxd, "", df):
        if lyr4.name == station+".lyr":
            print station
            arcpy.mapping.RemoveLayer(df, lyr4)    
    # arcpy.mapping.RemoveLayer(df,addLayer2)
    # print arcpy.mapping.ListLayers(mxd)
    lyr.visible = False #关闭该图层

    m = m + 1
print "finished"