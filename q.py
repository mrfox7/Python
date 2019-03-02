# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:30:55 2017

@author: Jiawei
"""

import pandas as pd
import time
starttime=time.asctime( time.localtime(time.time()) )
starttime1=time.time()

a = pd.read_csv('/Users/XIECHEN/Desktop/test1.csv') #导入csv文件（！！！改成相应的输入路径）
#a=a[0:1000]

#排序、重置index
a['sort1']=a['O']*a['D']
a['sort2']=a['O']+a['D']
a=a.sort_values(by=['sort1','sort2'])
a=a.reset_index(drop = True)

#添加匹配、选出、求和字段
a['match']=0
a['choose']=0
a['sum']=0
k=max(a.index)

#显示运算进度变量赋值
n=0.0+k
m=0.0

#开始遍历求和
for i in range(0,k):
	m=m+1
	print 'complete:',m/n*100.0,'%' #显示运算进度条
	j=i+1
	if a.ix[i,'match']==0:
                if a.ix[j,'O']==a.ix[i,'D'] and a.ix[j,'D']==a.ix[i,'O']:
                        a.ix[i,'match']=1
                        a.ix[j,'match']=1
                        a.ix[i,'choose']=1
                        a.ix[i,'sum']=a.ix[i,'m']+a.ix[j,'m']
                else:
                        a.ix[i,'choose']=1
                        a.ix[i,'sum']=a.ix[i,'m']
        else:
                continue

#末项检查
if a.ix[k,'match']==0:
	a.ix[k,'sum']=a.ix[max(a.index),'m']
	a.ix[k,'choose']=1

#去除正反方向中的其中一项
a=a[a.choose==1]

b=a.drop(['match','choose','sort1','sort2'],axis=1) #删除多余列
print b
print len(b.index) #输出行数
b.to_csv('/Users/XIECHEN/Desktop/nodirection.csv',index=False) #写出csv文件（！！！改成相应的输出路径）

#代码运行时间计算
finishtime=time.asctime( time.localtime(time.time()) )
finishtime1=time.time()
print 'Cong! All done'
print 'starttime:',starttime
print 'finishtime:',finishtime
print 'duration:',(finishtime1-starttime1)/60.0,'mins' 
