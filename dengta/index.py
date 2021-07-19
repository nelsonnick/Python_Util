#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import json
import base64
import hashlib
import time
import random
import threading
from PIL import Image

path = 'd:/image'

# idCardHash = '3anWxdBsVyRArO91NYiK8QfECqU='
# 获取验证码
def get_picture(session):
    api_picture = 'https://sso.dtdjzx.gov.cn/sso/validateCodeServlet'
    request = session.get(api_picture)
    picture = open(path + '-灯塔.jpg', 'wb')
    picture.write(request.content)
    picture.close()


# 登录
def login(session, username, password, validateCode):
    api_login = 'https://sso.dtdjzx.gov.cn/sso/login'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_login = {
        'username': username,
        'password': password,
        'validateCode': validateCode}
    request = session.post(api_login, headers=headers, data=data_login)
    if request.status_code == 200:
        return session
    print(request)
    # return json.loads(request.content.decode('UTF-8'))['message']


# 手动登录：手动收入验证码
def goLogin_hand(username, password):
    session = requests.session()
    get_picture(session)
    picture = input('请查看D盘根目录下的image-灯塔.jpg文件，并输入验证码: ')
    login(session, username, password, picture)
    return session


# 开始课程
def start(session, courseId, idCardHash):
    url = "https://gbwlxy.dtdjzx.gov.cn/__api/api/study/start"

    payload = "{\"courseId\":\""+courseId+"\",\"idCardHash\":\""+idCardHash+"\",\"studyType\":\"VIDEO\"}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '98',
        'Content-Type': 'application/json;',
        'Host': 'gbwlxy.dtdjzx.gov.cn',
        'Origin': 'https://gbwlxy.dtdjzx.gov.cn',
        'Referer': 'https://gbwlxy.dtdjzx.gov.cn/content',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3872.400 QQBrowser/10.8.4455.400',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Cookie': 'Hm_lvt_d652361e289e90df5f0bacaa8bf8cf2b=1626697951; X-SESSION=4e0e87e7-6669-4d59-9a26-cf948d018892; Hm_lpvt_d652361e289e90df5f0bacaa8bf8cf2b=1626700991; _cs=1bdd0fce-cea6-4709-9b60-9fb6424892ba; Hm_lvt_c6d07abdd39cb2faa9c4355c35abfc55=1626701037; Hm_lpvt_c6d07abdd39cb2faa9c4355c35abfc55=1626701443'
    }
    request = session.post(url, headers=headers, data=payload)
    result = json.loads(request.content.decode('UTF-8'))
    print('start')
    print(result)


# 过程中保存
def progress(session, courseId, idCardHash, studyTimes):
    url = "https://gbwlxy.dtdjzx.gov.cn/__api/api/study/progress"
    payload = "{\"courseId\":\""+courseId+"\",\"idCardHash\":\""+idCardHash+"\",\"studyTimes\":"+str(studyTimes)+"}"
    if studyTimes > 99:
        ContentLength = '95'
    elif studyTimes > 999:
        ContentLength = '96'
    else:
        ContentLength = '94'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': ContentLength,
        'Content-Type': 'application/json;',
        # 'Cookie': 'Hm_lvt_d652361e289e90df5f0bacaa8bf8cf2b=1626697951; X-SESSION=4e0e87e7-6669-4d59-9a26-cf948d018892; Hm_lpvt_d652361e289e90df5f0bacaa8bf8cf2b=1626700991; _cs=1bdd0fce-cea6-4709-9b60-9fb6424892ba; Hm_lvt_c6d07abdd39cb2faa9c4355c35abfc55=1626701037; Hm_lpvt_c6d07abdd39cb2faa9c4355c35abfc55=1626701443',
        'Host': 'gbwlxy.dtdjzx.gov.cn',
        'Origin': 'https://gbwlxy.dtdjzx.gov.cn',
        'Referer': 'https://gbwlxy.dtdjzx.gov.cn/content',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3872.400 QQBrowser/10.8.4455.400',
        'X-Requested-With': 'XMLHttpRequest'
    }
    request = session.post(url, headers=headers, data=payload)
    result = json.loads(request.content.decode('UTF-8'))
    print('progress')
    print(result)


# 结果保存
def end(session, courseId, idCardHash):
    url = "https://gbwlxy.dtdjzx.gov.cn/__api/api/study/v2/end"
    payload = "{\"courseId\":\""+courseId+"\",\"idCardHash\":\""+idCardHash+"\"}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '78',
        'Content-Type': 'application/json;',
        # 'Cookie': 'Hm_lvt_d652361e289e90df5f0bacaa8bf8cf2b=1626697951; X-SESSION=4e0e87e7-6669-4d59-9a26-cf948d018892; Hm_lvt_c6d07abdd39cb2faa9c4355c35abfc55=1626701037; Hm_lpvt_d652361e289e90df5f0bacaa8bf8cf2b=1626703743; _cs=dc002a5e-d9f4-489f-bc7b-227b680b7567; Hm_lpvt_c6d07abdd39cb2faa9c4355c35abfc55=1626703761',
        'Host': 'gbwlxy.dtdjzx.gov.cn',
        'Origin': 'https://gbwlxy.dtdjzx.gov.cn',
        'Referer': 'https://gbwlxy.dtdjzx.gov.cn/content',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3872.400 QQBrowser/10.8.4455.400',
        'X-Requested-With': 'XMLHttpRequest'
    }
    request = session.post(url, headers=headers, data=payload)
    result = json.loads(request.content.decode('UTF-8'))
    print('end')
    print(result)


def go():
    session = goLogin_hand('18653145531', 'hy123456')
    idCardHash = '3anWxdBsVyRArO91NYiK8QfECqU='
    with open('./course.json', 'r', encoding='utf8')as fp:
        courseList = json.load(fp)
        for course in courseList[1]['detail']:
            courseId = course['courseId']
            start(session, courseId, idCardHash)
            progress(session, courseId, idCardHash, course['time'] - 25)



go()
