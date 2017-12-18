#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import pymysql
from PIL import Image
from look import get_bin_table, get_result
from id import get_id, get_tel, get_ip, get_name
for i in range(1, 50000):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    s = requests.session()
    rt = s.get("http://rsxf.sdhrss.gov.cn:8181/websenior/validateYzm?temp", headers=headers)
    local = open('c:/image.jpg', 'wb')
    local.write(rt.content)
    local.close()
    # Image.open("C:/image.jpg").show()
    # res = input("res: ")
    out = Image.open("C:/image.jpg").convert('L').point(get_bin_table(), '1')
    oo = get_result(out)
    if oo != 999:
        # 63172
        # 63164,62863,63172,63173
        pname = get_name()
        idcard = get_id()
        tel = get_tel()
        ip = get_ip()
        payload = {
            'name': pname,
            'idcard': idcard,
            'tpyzm': oo,
            # 'tpyzm': res,
            'tel': tel,
            'ip': ip}
        rr = s.post("http://rsxf.sdhrss.gov.cn:8181/websenior/wenjuan/saveToupiao.action?votenumber=63172", data=payload)
        re = rr.text
        if re[4:8] == '投票成功':
            db = pymysql.connect("localhost", "root", "root", "vote", charset='utf8')
            cursor = db.cursor()
            sql = "INSERT INTO detail(pname, idcard, tel, ip, re) \
                  VALUES ('%s', '%s', '%s', '%s', '%s')" % \
                  (pname, idcard, tel, ip, re)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
            db.close()
            print(str(i) + "->投票成功")
        else:
            print(str(i) + "->投票结果：" + re)
