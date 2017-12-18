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
location_pic = 'http://'
location_login = 'http://'
location_get = 'http://'


s = requests.session()
re1 = s.get(location_pic, headers=headers)
local = open('c:/image.jpg', 'wb')
local.write(re1.content)
local.close()
pic = input("pic: ")
data_login = {
    '': '',
    '': '',
    '': pic}
re2 = s.post(location_login, headers=headers, data=data_login)

mkdir('c:\\婚姻状况\\')

file_total = open('c:/婚姻.txt', 'r')
line = file_total.readline()
while line:
    sfzhm = line.split("\t")[0]
    xm = line.split("\t")[1]
    data_get1 = {
        '': '',
        '': '',
        '': ''}
    data_get2 = {
        '': '',
        '': '',
        '': ''}
    if int(sfzhm[16:17]) % 2 == 1:
        re3 = s.get(location_get, headers=headers, data=data_get1)
    else:
        re3 = s.get(location_get, headers=headers, data=data_get2)
    details = re.findall(r'<td>.+?</td><td>.+?</td><td>.+?</td><td>.+?</td><td>.+?</td>', re3.test)
    file_person = open("C:\\婚姻状况\\" + sfzhm + xm + ".txt", "w", encoding='utf-8')
    for detail in details:
        information = re.findall(r'<td>.+?</td>', detail)
        for info in information:
            file_person.write(info[4:len(info) - 5] + "\t")
        file_person.write("\n")
    file_person.close()
    print(sfzhm + xm + '已完成！')
    line = file_total.readline()
file_total.close()





