# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 01:25:21 2017

"""

from selenium import webdriver
from time import sleep
import sys
import re
import json
import pytesseract
import urllib
from PIL import Image

reload(sys)
sys.setdefaultencoding('utf-8')
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)

def getroomprice(text):
    dict = json.loads(text)
    #print dict
    image = dict['image'].encode('utf-8')
    if len(image) <1:
        return []
    urllib.urlretrieve("http:" + image, 'D:\%s.png' % 'aaaaa')
    testdata_dir_config = '--tessdata-dir "D:\\Program Files (x86)\\Tesseract-OCR\\tessdata" --psm 7'
    nums = pytesseract.image_to_string(Image.open("D:\\aaaaa.png"), config=testdata_dir_config)
    nums = [i for i in nums if i >='0']
    #print nums
    num_list = []
    for ii in dict['offset']:
        num = ''
        for i in ii:
            num += nums[i]
        num_list.append(num)
    #print num_list
    return num_list


with open('detail.txt', "a+") as f:
    for i in open("res"):
        ii = i.strip()
        #print ii[0][6:-3]
        url="http://www.ziroom.com/z/nl/r2000TO3500-z3.html?qwd=" + ii
        #print url
        driver.get(url)
        sleep(1)
        rent_list = driver.find_elements_by_css_selector('li.clearfix')
        if '自如寓' in rent_list[0].find_element_by_css_selector('div.txt').text:
            rent_list=rent_list[1:]
        price_list = driver.page_source.encode('utf-8').split('ROOM_PRICE = ')[1].split(';')[0]
        price_list = getroomprice(price_list)
        for i in range(len(price_list)):
            #detail = rent_list[i].find_element_by_css_selector('div.detail').text
            de = rent_list[i].find_element_by_css_selector('div.txt').text
            a = ii + "|" + price_list[i] + "|" + de.replace('\n', '|')
            print(a)
            f.write(a + "\n")

f.close()
