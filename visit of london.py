# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import re
# urls = ['https://www.tripadvisor.cn/Attractions-g186338--Activities-c47-oa{}-London_England.html#FILTERED_LIST'.format(str(i)) for i in range(0,900,30)]
urls=['https://visitlondon.com/search?category=%2fthings-to-do%2fwhats-on%2fart-and-exhibitions&from=28-2-2019&to=28-2-2019&from.date=28%2f02%2f2019&to.date=28%2f02%2f2019&keywords=&page={}'.format(str(i)) for i in range(1,8,1)]
urls=['https://honglingjin.londontheatredirect.com/events/today']
# print urls

headers = {
# 'User-Agent':'Mozilla/5.0'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie': 'ServerPool=X; TART=%1%enc%3AJrLr2lvxwNlLbH9Cmhye81h4fhzdErdMYRa5jIgQ%2BzMdQzRRGJHP%2BEwOn0Pk%2B7RjAypFF0poxcI%3D; TAUnique=%1%enc%3A2cU7ADHy9Eo%2BkIWbO8dIhRvcFs06Zy%2F3vKdc%2Bd3i34gVAETMq8nxvA%3D%3D; TASSK=enc%3AAO0kkqxQ6UQrxO%2Fhkulabq0%2FgYgi6LuHCDMDfxtJkh4LERyb5A9E2%2FKatL80BtAkileXZDy3kvSOK7CHrCLzCQ23W40ydDWAbiH2fJ1WXXdRpNYcX%2FqFl3XA4gaaqM6ZeA%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1529666639404; _ga=GA1.2.130210118.1529061841; _gid=GA1.2.969501517.1529061841; _smt_uid=5b23a1d2.4e54e361; __gads=ID=826c32b0d192b76d:T=1529061847:S=ALNI_MaQj-S3SBC0F86Wrv6BWEmJRhlB0A; CommercePopunder=SuppressAll*1529061865893; ki_r=; TAAuth3=3%3Adf9baacbcf8f189f276b1a5c29e15b62%3AABSHViFhFqb1vgGz0nQ1zKy3RFlL3VHov1qFBzyJY1diYONpPht1Vnv2LCsUNojv60oiLMYJzj8gWWMB1Gkji%2FNpJw%2FwPFAZ7lkigK3UdltaJehxgMM1MGd7i%2BbXmId%2Fs7HB5w%2F1ezojK0b7n9MQXUdQliAXeStS1SzWK%2BRMop3nNuU3H6o3oOHl9Rt4ltQKUw%3D%3D; MobileLastViewedList=%1%%2FAttractions-g187147-Activities-c47-Paris_Ile_de_France.html; interstitialCounter=-1; TATravelInfo=V2*AY.2018*AM.6*AD.24*DY.2018*DM.6*DD.25*A.2*MG.-1*HP.2*FL.3*DSM.1529067170928; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C4%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C1%2C1529148251%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmds%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g187147-Activities-Paris_Ile_de_France.html; roybatty=TNI1625!AHvfFP6GU%2Blwk4iVZ0AzyrpCCufht6MXowsnGvilj0IjbceNq1euKmzBt2GMOqFWaUSHiMCOUhrHs%2Fiu0fHYMWBajyJ97jRyEttR9yaX840tAKQUND6vW0o3JIcYXgjdkO3J4lFTseSHKDIZem%2FBrHlR1JF9frXGbBh3kQvWi8Xk%2C1; ki_t=1529061844713%3B1529061844713%3B1529067216226%3B1%3B28; TASession=%1%V2ID.21FD898339223DC08F21308BF888E17F*SQ.134*MC.16631*LR.https%3A%2F%2Fsp0%5C.baidu%5C.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc%5C.php%3Ftpl%3Dtpl_11534_17355_13016%26l%3D1504452536%26wd%3D%25E7%258C%25AB%25E9%2580%2594%25E9%25B9%25B0%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D3211*LP.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*PR.427%7C*LS.DemandLoadAjax*GR.75*TCPAR.41*TBR.76*EXEX.67*ABTR.62*PHTB.85*FS.25*CPU.80*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.7067C40EA7A60B512E55A582616B88D6*FA.1*DF.0*MS.-1*RMS.-1*FLO.187147*TRA.true*LD.187147; TAUD=LA-1529057833220-1*RDD-1-2018_06_15*HDD-4144951-2018_06_24.2018_06_25*LD-9463016-2018.6.24.2018.6.25*LG-9463017-2.0.F.'

}

c1=0
def get_data(url, data=None):
    wb_data = requests.get(url, headers=headers)
    time.sleep(4)
    # print(wb_data.text)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    global c1
    # print(soup)
    titles=soup.select('#ctl00_MainContent_EventsContainer_ListPanel')
    # print str(titles[0])
    c1=c1+1
    f1=open(r'C:\Users\XIECHEN\Desktop\sc\c'+str(c1)+'.txt',"a+")
    f1.write(str(titles[0]))
    f1.close()
    f=open(r'C:\Users\XIECHEN\Desktop\sc\c'+str(c1)+'.txt')
    l1=''
    for line in f.readlines():
	l1=l1+line.strip()+' '
	f.close()
    # print l1

    p2=r"(?=data-ll=).+?(?=<li)"
    pattern2 = re.compile(p2)
    result2=pattern2.findall(l1)
    # print result2
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
		str1=eName+'>'+rCat+'>'+rDate+'>'+location+"\n"
		print str1
		f.write(str1)


for single_url in urls:
	get_data(single_url)
print('finished')