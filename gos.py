#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
from id import get_ip

for i in range(1, 5000):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    s = requests.session()
    rt = s.get("http://rsxf.sdhrss.gov.cn:8181/websenior/validateYzm?temp", headers=headers)
    local = open('c:/image.jpg', 'wb')
    local.write(rt.content)
    local.close()
    pname = input("姓名: ")
    idcard = input("身份证号码: ")
    tel = input("联系电话: ")
    res = input("验证码答案: ")
    ip = get_ip()
    payload = {
        'name': pname,
        'idcard': idcard,
        'tpyzm': res,
        'tel': tel,
        'ip': ip}
    rr = s.post("http://rsxf.sdhrss.gov.cn:8181/websenior/wenjuan/saveToupiao.action?votenumber=63172", data=payload)
    re = rr.text
    print(str(i) + "->投票结果：" + re)
