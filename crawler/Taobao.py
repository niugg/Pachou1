# -*- coding: utf-8 -*
import requests
import json


#淘宝爬虫类
class TAOBAO:
    #初始化，传入基地址，页数
    def __init__(self,baseUrl,page,goods):
        self.goods=goods
        self.baseUrl=baseUrl+self.goods
        self.page=page
        self.defaultgoods=u"淘宝"
        self.ilt=[]
        self.file=None
    #传入url，获取页面代码
    def getHTMLText(self,url):
        headers={'user-agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"}
        try:
            print url
            r=requests.get(url,headers=headers,timeout=30)
            return r.text
            #print json.dumps(data['mods']['grid']['data']['spus'],ensure_ascii=False)
            #return data
        except requests.exceptions.RequestException,e:
            print e
    #摘取所要数据
    def parsePage(self,html):
        try:
            start = html.find('g_page_config =')
            end = html.find('g_srp_loadCss();')
            text = html[start + 15:end].strip()
            # print start,end,text[:-1]
            data = json.loads(text[:-1])['mods']['grid']['data']['spus']
            self.ilt=data
        except:
            print("摘取数据出错").encode('utf-8')
            return None

    #创建存入数据文件
    def setFileTitle(self):

            self.file = open(goods + ".txt","w+")
    #写入数据
    def writeData(self):
        for i in self.ilt:
            self.file.write(json.dumps(i))

    def start(self):
        self.setFileTitle()
        for i in range(self.page):
            try:
                url = self.baseUrl + '&s=' + str(44*i)
                html = self.getHTMLText(url)
                self.parsePage(html)
            except:
                continue
        self.writeData()

goods=u'手机'
baseurl = "https://s.taobao.com/search?q="
page=1

tb = TAOBAO(baseurl,page,goods)
tb.start()
