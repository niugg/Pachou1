# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 01:25:21 2017

"""

from selenium import webdriver
from time import sleep
import sys
import re
p = re.compile(r'\d+')
reload(sys)
sys.setdefaultencoding('utf-8')
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)

with open('detail.txt', "a+") as f:
    for i in open("res"):
        ii=i.strip().split("\t")
        driver.get("https://www.dankegongyu.com/room/bj/p2500.html?search_text=" + ii[0])
        sleep(1)
        try:
         rent_list = driver.find_elements_by_css_selector('div.roomlist')
         for echo_house in rent_list:
            print len(rent_list)
            tex = echo_house.find_element_by_css_selector('div.r_lbx')
            print tex.text
            a=ii[0]+'|'+ii[1]+'|'+ii[2]+"|"+tex.text.replace('\n','|')
            print(a)
            f.write(a+"\n")
        except:
            print 'error'
        driver.get("https://www.dankegongyu.com/room/bj/p2000.html?search_text=" + ii[0])
        sleep(1)
        try:

         rent_list = driver.find_elements_by_css_selector('div.roomlist')
         for echo_house in rent_list:
            print len(rent_list)
            tex = echo_house.find_element_by_css_selector('div.r_lbx')
            print tex.text
            a = ii[0] + '|' + ii[1] + '|' + ii[2] + "|" + tex.text.replace('\n', '|')
            print(a)
            f.write(a + "\n")
        except:
            print 'error'


f.close()