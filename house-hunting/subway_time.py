# -*- coding: utf-8 -*
#coding=utf-8
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#org = "116.311792,39.979564"
org = "116.472475,40.019242"

# url="http://restapi.amap.com/v3/direction/transit/integrated?origin="+org+"&destination="+des+"&key=77cbb8671751f9957c783e80babe8c4a"

#print url
# r=requests.get(url)
#print r.text
headers = {'user-agent': "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
           'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"}

fw = open(u"中国电子大厦B" + ".txt", "w+")


# "http://restapi.amap.com/v3/place/text?keywords==beijing&offset=1&page=1&key=77cbb8671751f9957c783e80babe8c4a&extensions=base"

for line in open("D:\loc"):
    line = "地铁"+line.strip()+"站"
    url = "http://restapi.amap.com/v3/place/text?keywords=%s&city=beijing&offset=1&page=1&key=77cbb8671751f9957c783e80babe8c4a&extensions=base" % (line)
    org = json.loads(requests.get(url, timeout=30).text)['pois'][0]['location']
    #print org
    org = org.encode('utf-8')
    des = "116.472475,40.019242"
    #des = "116.311792,39.979564"
    url = "http://restapi.amap.com/v3/direction/transit/integrated?key=77cbb8671751f9957c783e80babe8c4a&origin=%s&destination=%s&city=北京&cityd=北京&strategy=0&nightflag=0&time=09:00&extensions=base" % (
        org, des)
    #print url
    r = requests.get(url, headers=headers, timeout=30)
    # print r.text
    data = json.loads(r.text)

    #print data
    fw.write(line + "||" + r.text + "\n")
    dict1 = {}
    for i in data['route']['transits']:
        #print i
        time = int(i['duration']) / 60
        station = line
        #print time,station
        if dict1.get(station, 1000) > time:
            dict1[station] = time

    a = sorted(dict1.items(), lambda x, y: cmp(x[1], y[1]))
    for i in a:
        print i[0], i[1], org
