# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 13:20:03 2018

@author: XIECHEN
"""
import requests
import json
import time
import re
starttime=time.asctime(time.localtime(time.time()))   
starttime1=time.time();
def getjson(ocoo):
    url='http://dev.virtualearth.net/REST/v1/Locations?locality=London&addressLine='+(ocoo)+'&key=ApDCvJQsXwfgE00ORgBNdxk00ReQu59UKh0pV53t-_HsDoPNmPxuorZofc6ubaER'
    print url
    # url='http://api.map.baidu.com/direction/v2/transit?origin='+ocoo+'&destination=31.1431889586,121.6581503809&coord_type=wgs84&tactics_incity=4&ak=d7vs3eaHfM0io4aV98VQf7kv1v5VmX3N'
    while True:
        try:
            response=requests.get(url=url,timeout=5)
            break
        except requests.exceptions.ConnectionError:
            print 'ConnectionError -- please wait 10 sec'
            time.sleep(10)
        except requests.exceptions.ChunkedEncodingError:
            print 'ChunkedEncodingError -- please wait 10 sec'
            time.sleep(10)
        except:
            print 'Unknow error -- please wait 10 sec'
            time.sleep(10)
    html=response.text
    decodejson=json.loads(html)
    return decodejson
file_object=open(r'C:\Users\XIECHEN\Desktop\test1.txt','r')
file_object2=open(r'C:\Users\XIECHEN\Desktop\output.txt','w')
count=0
try:
    for line in file_object:
        count=count+1
        coor=line
        print coor.strip()
        decodejson=getjson(coor.strip())
        print decodejson.get('statusCode')
        if decodejson.get('statusCode')==200:#表示运行成功
            result=decodejson.get('resourceSets')
            # print len(result)
            location=result[0].get('resources')
            # print location
            location2=location[0].get('point')
            location3=location2.get('coordinates')
            file_object2.write(str(location3[0])+'\n')
            #获得需要的时间和距离
            # if len(routes)>0:     
            #     time2=routes[0].get('duration')
            #     distance=routes[0].get('distance')
            #     file_object2.write(str(idn)+','+str(time2)+','+str(distance) +'\n')
            #     if count%10==0:
            #         finishtime=time.asctime( time.localtime(time.time()))
            #         finishtime1=time.time()
            #         print count
            #         print 'duration:',(finishtime1-starttime1)/60.0,'mins' 
        else:
            print decodejson.get('status')
            # print str(coor)+','+ str(decodejson.get('status'))+','+decodejson.get('message')
finally:
        file_object.close()
        file_object2.close()
        print 'finish'



    

