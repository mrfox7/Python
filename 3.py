# -*- coding: utf-8 -*-
import re
import csv
f=open(r'C:\Users\XIECHEN\Desktop\new 8.txt')
l1=''
for line in f.readlines():
	l1=l1+line.strip()+' '
# print l1

# l1.replace("\r\n"," ")
# print re.match('[A-Z]+',l1,flags=0)
p2=r"(?=data-ll=).+?(?=<li)"
# p2 = r"(?=data-ll=).+?(?=>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern2 = re.compile(p2)#我们在编译这段正则表达式
result2=pattern2.findall(l1)
# print result2[0]
f=file(r"C:\Users\XIECHEN\Desktop\sc\a.txt","a+")
for data in result2:
	str1=""
	p3 = r"(?=data-ll=).+?(?=>)"#找到地址
	pattern3=re.compile(p3)
	xy=pattern3.findall(data)
	location=xy[0].split('\"')[1]
	p4=r"(?=search-tile-title).+?(?=</a>)"
	pattern4=re.compile(p4)
	name=pattern4.findall(data)
	eName=name[0].split('>')[2]
	p5=r"(?=datetime=).+?(?=>)"
	pattern5=re.compile(p5)
	date=pattern5.findall(data)
	# print len(date)
	rDate=""
	if len(date)!=0:
		rDate=date[0].split('\"')[1]
	else:
		rDate="";
	p6=r"(?=category).+?(?=</p>)"
	pattern6=re.compile(p6)
	cat=pattern6.findall(data)
	print cat
	rCat=""
	if len(cat)!=0:
		rCat=(cat[0].split('>')[1])
	else:
		rCat='';
	str1=eName+'/'+rCat+'/'+rDate+'/'+location+"\n"
	print str1
	f.write(str1)
f.close
	

# 名字时间和事件类型要分开爬取
# p1=r"[A-Z].+?(?=<)"
# pattern1 = re.compile(p1)#我们在编译这段正则表达式
# result1=pattern1.findall(l1)
# f=file(r"C:\Users\XIECHEN\Desktop\sc\a.txt","a+")
# s1=0;
# count1=0
# str1=""
# for data in result1:
#     count1=count1+1
#     str1=str1+","+data
#     if count1 %3 ==0:
#     		s1=s1+1
#     		# print result2[s1]
#     		print result2[s1].split('\"')[1]
#     		str1=str1+","+result2[s1].split('\"')[1]+"\n"
#     		print str1
#     		f.write(str1)
#     		count1=0;
#     		str1="";
    	
# matcher1 = re.search(pattern1,l1)#在源文本中搜索符合正则表达式的部分
# print matcher1.group(0)#打印出来