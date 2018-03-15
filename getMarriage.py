#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import os
import re
import getpass

# 此版本为封装后的版本
# TXT文件名必须为指定名称，放置在C盘根目录下，不需要表头，第一列为身份证号码，第二列为姓名，两列间用tab间隔。
# 输出的个人信息为TXT文档，保存在“C:\婚姻状况获取\”下，命名格式为：查询人身份证号码+查询人姓名。
# 输出的汇总信息为TXT文档，保存在C盘根目录下，命名格式为：待查TXT文件名+“_汇总”。

files = [
    '西市场',
    '五里沟',
    '道德街',
    '营市街',
    '青年公园',
    '中大',
    '振兴街',
    '南辛庄',
    '段北',
    '匡山',
    '张庄',
    '美里湖',
    '腊山',
    '吴家堡',
    '玉清湖',
    '兴福',
         ]


# 创建文件夹
def create_files(path):
    path = path.strip()
    path = path.rstrip("\\")
    # 存在     True
    # 不存在   False
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False


# 创建汇总文件
def create_merge(file_name):
    file = open("C:\\" + file_name + "_汇总.txt", "w", encoding='utf-8')
    file.write("证件号码" + "\t")
    file.write("人员姓名" + "\t")
    file.write("男方姓名" + "\t")
    file.write("男方证件号码" + "\t")
    file.write("女方姓名" + "\t")
    file.write("女方证件号码" + "\t")
    file.write("登记时间" + "\t")
    file.write("登记业务" + "\n")
    file.close()


# 获取验证码
def get_picture(session):
    api_picture = 'http://10.60.0.16/marry/common/showimage.jsp'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = session.get(api_picture, headers=headers)
    picture = open('c:/image.jpg', 'wb')
    picture.write(request.content)
    picture.close()


# 验证验证码
def check_picture(session, username, password, picture):
    api_check = 'http://10.60.0.16/marry/loginCheck.jsp'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_check = {
        'action': 'login',
        'username': username,
        'password': password,
        'x': '12',
        'y': '23',
        'rcode': picture}
    session.post(api_check, headers=headers, data=data_check)


# 登录
def login(session, username, password):
    api_login = 'http://10.60.0.16/marry/loginMarry.do?method=login'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_login = {
        'action': 'login',
        'username': username,
        'password': password
    }
    request = session.post(api_login, headers=headers, data=data_login)


# 获取结婚记录
def get_marriage(session, number):
    api_get = 'http://10.60.0.16/marry/xcdjdj/marryQuery.do?method=query&opType=ICA'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_get1 = {
        'nameMan1': '',
        'certNumMan1': number,
        'nameWoman1': '',
        'certNumWoman1': ''
    }
    data_get2 = {
        'nameMan1': '',
        'certNumMan1': '',
        'nameWoman1': '',
        'certNumWoman1': number
    }
    if int(number[16:17]) % 2 == 1:
        request = session.post(api_get, headers=headers, data=data_get1)
    else:
        request = session.post(api_get, headers=headers, data=data_get2)

    details = re.findall(r'<td\s*height="22" align="center"\s*>.+?</td>|<td\s*height="22" align="center"\s*></td>',
                         request.text)
    return details


# 保存婚姻记录
def down_marriage(session, number, name):
    create_files('c:\\婚姻状况获取\\')
    file = open("C:\\婚姻状况获取\\" + number + name + ".txt", "w", encoding='utf-8')
    details = get_marriage(session, number)
    for detail in details:
        information = re.findall(r'>.+?</td>|></td>', detail)
        for info in information:
            if info[1:5] != "<a t" and info[1:5] != "<a h":
                file.write(info[1:len(info) - 5])
                file.write("\t")
            else:
                if info[1:5] != "<a h":
                    file.write("\n")
                    break
                else:
                    break
    file.close()


# 合并婚姻记录
def merge_marriage(file_name, number, name):
    file_merge = open("C:\\" + file_name + "_汇总.txt", "a", encoding='utf-8')
    file = open("C:\\婚姻状况获取\\" + number + name + ".txt", "r", encoding='utf-8')
    line = file.readline()
    while line:
        file_merge.write(number + "\t")
        file_merge.write(name + "\t")
        file_merge.write(line.split("\t")[0] + "\t")
        file_merge.write(line.split("\t")[1] + "\t")
        file_merge.write(line.split("\t")[2] + "\t")
        file_merge.write(line.split("\t")[3] + "\t")
        file_merge.write(line.split("\t")[4] + "\t")
        file_merge.write(line.split("\t")[5] + "\t")
        file_merge.write(file_name + "\n")
        line = file.readline()
    file.close()
    file_merge.close()


# 下载一个
def get_one(session, file_name):
    create_merge(file_name)
    file = open('c:/' + file_name + '.txt', 'r')
    line = file.readline()
    while line:
        number = line.split("\t")[0]
        name = line.split("\t")[1]
        down_marriage(session, number, name)
        merge_marriage(file_name, number, name)
        print(number + name + '已完成！')
        line = file.readline()
    file.close()


# 下载全部
def get_all():
    session = requests.session()
    get_picture(session)
    picture = input('请查看C盘根目录下的image.jpg文件，并输入验证码: ')
    username = input('输入用户名: ')
    password = input('输入密码: ')
    check_picture(session, username, password, picture)
    login(session, username, password)
    for f in files:
        get_one(session, f)
        print(f + '已完成！')


# 下载全部
def get_all2():
    session = requests.session()
    get_picture(session)
    picture = input('请查看C盘根目录下的image.jpg文件，并输入验证码: ')
    username = 'qixt'
    password = '191919'
    check_picture(session, username, password, picture)
    login(session, username, password)
    for f in files:
        get_one(session, f)
        print(f + '已完成！')


# 下载全部（隐藏输入的用户名和密码）
def get_all_getpass():
    session = requests.session()
    get_picture(session)
    picture = input('请查看C盘根目录下的image.jpg文件，并输入验证码: ')
    username = getpass.getpass('输入用户名: ')
    password = getpass.getpass('输入密码: ')
    check_picture(session, username, password, picture)
    login(session, username, password)
    for f in files:
        get_one(session, f)
        print(f + '已完成！')


get_all_getpass()






