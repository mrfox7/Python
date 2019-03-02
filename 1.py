# -*- coding: utf-8 -*-
#技巧1：通过模拟手机页面获得反爬取信息,页面右击检查，device mode 刷新网页，选取设备型号-获取User-Agent---headers
#技巧2：为安全获取反爬信息，设置每次请求睡眠2秒 time.sleep(2)
#技巧3:元素关系的观察，标签的唯一性soup.select(css 标签)
#技巧4：代码写成函数形式，以便调用，实现复用性
#技巧5：Cookie 实现伪登录、device mode模式反爬机制使用
from bs4 import BeautifulSoup
import requests
import time
'''
url='http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
web_data=requests.get(url)
soup=BeautifulSoup(web_data.text,'lxml')
#print(soup)
titles=soup.select('div.property_title > a[target="_blank"]')
imgs=soup.select('img[width="160"]')
cates=soup.select('div.p13n_reasoning_v2')
#print(titles,imgs,cates)

for title,img,cate in zip(titles,imgs,cates):
    data={
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped_strings)
    }
    print(data)
'''

url='http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
url_save='http://www.tripadvisor.cn/Saves#516791'
urls=['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,1020,30)]
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Cookie':'ServerPool=A; TAUnique=%1%enc%3AHpQUnHFM466%2By4VO3LcvxqAvwJBflMCezhEkYXkiQPo2jHwltRJPGQ%3D%3D; TASSK=enc%3AANhmL3wzIzNJaqddI5JQM5lj1hteYF5xCQ5385Dl1QJNjtqgtyjxsQa48nlwTa3CVP04M0CJCzGHTKIF9R33Mm4q5pkSLzawiEFAZH7wAZmM8dTSlhed%2F2KXh71OYjX6eg%3D%3D; TAPD=tripadvisor.cn; __gads=ID=96ccfce0d4473433:T=1476278765:S=ALNI_MZuVI8WFeSB6QEc43fp0RYNwvGFmg; _jzqckmp=1; CommercePopunder=SuppressAll*1476278779336; bdshare_firstime=1476280793818; TAAuth2=%1%3%3A2b2aff650ce812d87fc9f4eaf352cbf9%3AANL5xrs%2FluJvHr9FnqjacB99GxQP4rcJnTg8Mg5210p5LITGEo7HgaprQvE1QKoLnR5S7VIMB0H5a4Xo7b2iBZWr7oKarsKoBkruPunQrl9OviruG7CnrBCn3Np%2B4kdAs8DXks7tbHfCTEIEQoO1YVVqVmMTq9SgJf7gWVdFkUOL%2FK17OXO%2BkUTOrJY%2BDyPiOM25ZFRUsPYdGB%2FVy6v2AQUVgsCztgZs1MTdGhAH51JZ; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.143361_286l103371_286l105127_286l267031_286*RS.1; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C4%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d267031-Reviews-Manhattan_Skyline-New_York_City_New_York.html; roybatty=TNI1625!AJEFGeZG6dW7lq2cZGIqaUfU2ixnSBpl1cfeSJNw8Q%2FEcvDwZZdzfX%2FwOtYuDlsJdMCoZfaKLfuTJVTisKnfw%2FOEgHv9GorHzy43cJ5qXuxmtzqMmJJqfIkX5pS8iyX3Td41fvSgkNjb%2FFIP%2BDCfryqg04Xq4SMItpXHFh4yrpkj%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1476278762; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1476281126; ki_t=1476278765980%3B1476278765980%3B1476281125909%3B1%3B10; ki_r=; _qzja=1.603924426.1476278771083.1476278771083.1476278771084.1476281121016.1476281125939..0.0.10.1; _qzjb=1.1476278771083.10.0.0.0; _qzjc=1; _qzjto=10.1.0; _jzqa=1.1097167754089998200.1476278771.1476278771.1476278771.1; _jzqc=1; _jzqb=1.10.10.1476278771.1; NPID=; TASession=%1%V2ID.B1880F3A51529F710730FA25C2375D8B*SQ.52*PR.427%7C*LS.ActionRecord*GR.45*TCPAR.75*TBR.83*EXEX.39*ABTR.75*PPRP.31*PHTB.59*FS.64*CPU.87*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.2AB35190C0B975C1A01742A5DB675B77*LF.zhCN*FA.1*DF.0*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DA%26returnTo%3D%252FAttractions-g60763-Activities-New_York_City_New_York%5C.html*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.267031; TAUD=LA-1476278758997-1*LG-2388294-2.1.F.*LD-2388295-.....'
}
def get_attractions(url,data=None):
    web_data=requests.get(url)
    time.sleep(2)#保护机制，反爬机制
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div.property_title > a[target="_blank"]')
    imgs = soup.select('img[width="160"]')
    cates = soup.select('div.p13n_reasoning_v2')
    for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings)
        }
        print(data)

def get_favs(url,data=None):
    web_data = requests.get(url_save, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('a.location-name')
    images = soup.select('img.photo_image')
    metas = soup.select('span.format_address')
    for title, image, meta in zip(titles, images, metas):
        data = {
            'title': title.get_text(),
            'image': image.get('src'),
            'meta': list(meta.stripped_strings)
        }
        print(data)


#get_attractions(url)
#get_favs(url_save)
#print(urls)

for single_url in urls:
    get_attractions(single_url)
