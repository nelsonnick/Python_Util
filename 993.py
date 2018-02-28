#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import json
import re

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
login_place = 'http://10.153.50.108:7001/lemis3/logon.do'

s = requests.session()
login_data = {
    'method': 'doLogon',
    'userid': 'hyzhx',
    'passwd': '21218cca77804d2ba1922c33e0151105',
    'userLogSign': '0',
    'passWordLogSign': '0',
    'screenHeight': '768',
    'screenWidth': '1024',
    'mode': ''}
login_requests = s.post(login_place, headers=headers, data=login_data)

# window_place = 'http://10.153.50.108:7001/lemis3/lemis3TrainBonus.do'
# window_data = {
#     'method': 'enterTrainBonusPayApprove',
#     'gcbh': '100002',
#     'hdbh': '100002101',
#     '_jbjgqxfw': 'undefined',
#     '_sbjbjg': 'undefined',
#     '_dwqxfw': 'undefined',
# }
# window_requests = s.post(window_place, headers=headers, data=window_data)
# tableMark = re.findall(r'tableMark=\'.+? oncontextmenu=showMenu', window_requests.text)
#
# check_place = 'http://10.153.50.108:7001/lemis3/lemis3TrainBonus.do'
# check_data = {
#     'method': 'querySuccorPayApprove',
#     '_xmlString': '<?xml version="1.0" encoding="UTF-8"?><p><s pxjgbh="" pxjgmc="" sblb="" bqbh="" bqmc="" pxrylb="" sjbfzt="1" sjqrqsny="" sjqrzzny="" qjbfzt="1" qjqrqsny="2016-01-01" qjqrzzny="" hdbh="100002101" jgbh="" jbjgmc="" jbjgbh="" /></p>',
#     'tableMark': tableMark[0][11:58],
#     '_jbjgqxfw': 'undefined',
#     '_sbjbjg': 'undefined',
#     '_dwqxfw': 'undefined',
# }
# check_requests = s.post(check_place, headers=headers, data=check_data)
# print(check_requests.text)
# code_place = 'http://10.153.50.108:7001/lemis3/lemis3Lov.do'
# code_data = {
#     'method': 'queryAllTrainOrgInfo',
#     'containerName': 'queryDemo',
#     '_xmlString': '<?xml version="1.0" encoding="UTF-8"?><p><s para="济南"/></p>',
#     '_jbjgqxfw': 'undefined',
#     '_sbjbjg': 'undefined',
#     '_dwqxfw': 'undefined',
# }
# code_requests = s.post(code_place, headers=headers, data=code_data)
# print(code_requests.text)
file = open("C:\\8", "r", encoding='utf-8')
line = file.readline()
while line:
    sblb = line.split("\t")[0]
    bflsh = line.split("\t")[1]
    pxrylb = line.split("\t")[2]
    bqbh = line.split("\t")[3]
    bqmc = line.split("\t")[4]
    pxjgbh = line.split("\t")[5]
    pxjgmc = line.split("\t")[6]

    get_place = 'http://10.153.50.108:7001/lemis3/lemis3TrainQuery.do'
    pp = '<?xml version="1.0" encoding="UTF-8"?><p><s sblb="'+sblb+'"/><s bflsh="'+bflsh+'"/><s pxrylb="'+pxrylb+'"/><s ssqxbh=""/><s bqbh="'+bqbh+'"/><s bqmc="'+bqmc+'"/><s pxjgbh="'+pxjgbh+'"/><s pxjgmc="'+pxjgmc+'"/></p>'
    get_data = {
        'method': 'enterTrainBonusPayDetailQuery',
        '_xmlString': pp.encode("gbk"),
        '_jbjgqxfw': 'undefined',
        '_sbjbjg': 'undefined',
        '_dwqxfw': 'undefined',
    }
    # print(pp)
    get_requests = s.post(get_place, headers=headers, data=get_data)
    ones = re.findall(r'init.+?script', get_requests.text)[0]
    one = ones[21:len(ones) - 12]
    print(get_requests.text)
    if (one.split("},{").__len__()) == 1:
        print(json.loads(one))
    else:
        for o in one.split("},{"):
            print("过个："+o)
    line = file.readline()
file.close()
