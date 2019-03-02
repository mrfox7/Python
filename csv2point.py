import csv
import os
import arcpy
# attention:only English
# data path & result path
path=arcpy.GetParameterAsText(1)
path3= arcpy.GetParameterAsText(0)
arcpy.env.workspace = path
# get folder filelist
def listdir(path, list_name):  
    for file in os.listdir(path):  
        file_path = os.path.join(path, file) 
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        elif os.path.splitext(file_path)[1]=='.csv' and os.path.split(file_path)[1]!='delete_data.csv':  
            list_name.append(file_path)  
filelist=[]
listdir(path3,filelist)
print filelist
# for each file create point shp
for path2 in filelist:
    ID1= (os.path.split(path2)[1]).split(".")[0].split("_")[0]
    points = ID1+".shp"
    geometry_type = "Point"
    has_m = "ENABLED"
    has_z = "ENABLED"
    print ID1
    # prepare null shp 
    arcpy.CreateFeatureclass_management(path, points, geometry_type, "", has_m, has_z, arcpy.SpatialReference("WGS 1984"))
    filename = path +"\\"+ points
    fieldPrecision = 9
    fieldPrecision2 = 2
    strtem=""
    strtem2=""
    lista=["SHAPE@XY"]
    # open the csv
    with open(path2) as f: 
        f_csv = csv.reader(f)
        headers = next(f_csv)
        # add fields to store attributes
        for col in headers[1:]:
        	arcpy.AddField_management(filename, col, "TEXT","", "",32, "", "NULLABLE")
        	lista.append(col)
        # create a insertcursor to circling
        curLine = arcpy.da.InsertCursor(filename, lista)
    # for each row insert a point into null shp,including point and attributes 
        for row in f_csv:
            startPoint = [float(row[18]), float(row[17])]
            listb=[startPoint]
            for att in row[1:]:
            	listb.append(att)
            curLine.insertRow(listb)
    f.close()