# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 13:20:03 2018

@author: XIECHEN
"""
import requests
import json
import time
starttime=time.asctime(time.localtime(time.time()))   
starttime1=time.time();
def getjson(ocoo):
    url='http://api.map.baidu.com/direction/v2/transit?origin='+ocoo+'&destination=31.1431889586,121.6581503809&coord_type=wgs84&tactics_incity=4&ak=
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
        spline=line.split(',')
        idn=spline[0]
        coor=spline[4].strip()+','+spline[5].strip()
        #print coor
        decodejson=getjson(coor)
        if decodejson.get('status')==0:#表示运行成功
            result=decodejson.get('result')
            routes=result.get('routes')
            #获得需要的时间和距离
            if len(routes)>0:     
                time2=routes[0].get('duration')
                distance=routes[0].get('distance')
                file_object2.write(str(idn)+','+str(time2)+','+str(distance) +'\n')
                if count%10==0:
                    finishtime=time.asctime( time.localtime(time.time()))
                    finishtime1=time.time()
                    print count
                    print 'duration:',(finishtime1-starttime1)/60.0,'mins' 
        else:
            print str(coor)+','+ str(decodejson.get('status'))+','+decodejson.get('message')
finally:
        file_object.close()
        file_object2.close()
        print 'finish'



    

