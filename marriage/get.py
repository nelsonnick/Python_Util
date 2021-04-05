#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import os
import re


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    # 存在     True
    # 不存在   False
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
location_pic = 'http://10.60.0.16/marry/common/showimage.jsp'
location_check = 'http://10.60.0.16/marry/loginCheck.jsp'
location_login = 'http://10.60.0.16/marry/loginMarry.do?method=login'
location_get = 'http://10.60.0.16/marry/xcdjdj/marryQuery.do?method=query&opType=ICA'


s = requests.session()
re1 = s.get(location_pic, headers=headers)
local = open('c:/image.jpg', 'wb')
local.write(re1.content)
local.close()
pic = input("pic: ")
data_check = {
    'action': 'login',
    'username': 'qixt',
    'password': '191919',
    'x': '12',
    'y': '23',
    'rcode': pic}
re22 = s.post(location_check, headers=headers, data=data_check)
data_login = {
    'action': 'login',
    'username': 'qixt',
    'password': '191919'}
re2 = s.post(location_login, headers=headers, data=data_login)
mkdir('c:\\婚姻状况\\')

file_total = open('c:/婚姻.txt', 'r')
line = file_total.readline()
while line:
    sfzhm = line.split("\t")[0]
    xm = line.split("\t")[1]
    data_get1 = {
        'nameMan1': '',
        'certNumMan1': sfzhm,
        'nameWoman1': '',
        'certNumWoman1': ''}
    data_get2 = {
        'nameMan1': '',
        'certNumMan1': '',
        'nameWoman1': '',
        'certNumWoman1': sfzhm}
    if int(sfzhm[16:17]) % 2 == 1:
        re3 = s.post(location_get, headers=headers, data=data_get1)
    else:
        re3 = s.post(location_get, headers=headers, data=data_get2)
    html = re3.text
    # details = re.findall(r'<td>.+?</td><td>.+?</td><td>.+?</td><td>.+?</td><td>.+?</td>', re3.test)
    file_person = open("C:\\婚姻状况\\" + sfzhm + xm + ".txt", "w", encoding='utf-8')
    file_person.write(html)
    # for detail in details:
    #     information = re.findall(r'<td>.+?</td>', detail)
    #     for info in information:
    #         file_person.write(info[4:len(info) - 5] + "\t")
    #     file_person.write("\n")
    file_person.close()
    print(sfzhm + xm + '已完成！')
    line = file_total.readline()
file_total.close()
