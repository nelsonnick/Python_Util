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
proxy = {
    'http': 'http://10.153.73.166',
    'https': 'https://10.153.73.166'
}
login_requests = s.post(login_place, headers=headers, data=login_data)
print(login_requests.text)
