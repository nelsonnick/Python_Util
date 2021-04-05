#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import os
import re

files = open("C:\\汇总.txt", "w", encoding='utf-8')
files.write("证件号码" + "\t")
files.write("人员姓名" + "\t")
files.write("男方姓名" + "\t")
files.write("男方证件号码" + "\t")
files.write("女方姓名" + "\t")
files.write("女方证件号码" + "\t")
files.write("登记时间" + "\t")
files.write("登记业务" + "\n")
files.close()


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
username = 'qixt'
password = '191919'
pic = input("pic: ")
data_check = {
    'action': 'login',
    'username': username,
    'password': password,
    'x': '12',
    'y': '23',
    'rcode': pic}
re22 = s.post(location_check, headers=headers, data=data_check)
data_login = {
    'action': 'login',
    'username': username,
    'password': password}
re2 = s.post(location_login, headers=headers, data=data_login)
mkdir('c:\\婚姻状况获取\\')
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

    details = re.findall(r'<td\s*height="22" align="center"\s*>.+?</td>|<td\s*height="22" align="center"\s*></td>', re3.text)
    file_person = open("C:\\婚姻状况获取\\" + sfzhm + xm + ".txt", "w", encoding='utf-8')
    for detail in details:
        information = re.findall(r'>.+?</td>|></td>', detail)
        for info in information:
            if info[1:5] != "<a t" and info[1:5] != "<a h":
                file_person.write(info[1:len(info) - 5])
                file_person.write("\t")
            else:
                if info[1:5] != "<a h":
                    file_person.write("\n")
                    break
                else:
                    break
    file_person.close()
    file_all = open("C:\\汇总.txt", "a", encoding='utf-8')
    file_one = open("C:\\婚姻状况获取\\" + sfzhm + xm + ".txt", "r", encoding='utf-8')
    line_one = file_one.readline()
    while line_one:
        file_all.write(sfzhm + "\t")
        file_all.write(xm + "\t")
        file_all.write(line_one.split("\t")[0] + "\t")
        file_all.write(line_one.split("\t")[1] + "\t")
        file_all.write(line_one.split("\t")[2] + "\t")
        file_all.write(line_one.split("\t")[3] + "\t")
        file_all.write(line_one.split("\t")[4] + "\t")
        file_all.write(line_one.split("\t")[5] + "\n")
        line_one = file_one.readline()
    file_one.close()
    file_all.close()
    print(sfzhm + xm + '已完成！')
    line = file_total.readline()
file_total.close()
