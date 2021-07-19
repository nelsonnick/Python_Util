#!/user/bin/env python
# -*- coding: UTF-8 -*-

import pymysql
db = pymysql.connect(host="localhost", user="root", password="root", database="addressbook")
cursor = db.cursor()
cursor.execute("SELECT unit,dwmc,qtmc,jb,ldzs,nsjg,zyzz,url FROM department")
lists = cursor.fetchall()
jsonStr = ''
for lg in lists:
    _id = str(lg[0])
    dwmc = str(lg[1])
    qtmc = str(lg[2])
    jb = str(lg[3])
    ldzs = str(lg[4])
    nsjg = str(lg[5])
    zyzz = str(lg[6])
    url = str(lg[7])
    jsonStr = jsonStr + '{"_id":"' + _id + '","dwmc":"' + dwmc + '","qtmc":"' + qtmc \
              + '","jb":"' + jb + '","ldzs":"' + ldzs + '","nsjg":"' + nsjg \
              + '","zyzz":"' + zyzz + '","url":"' + url + '"}\n'
    print(jsonStr)
