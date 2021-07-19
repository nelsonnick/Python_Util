#!/user/bin/env python
# -*- coding: UTF-8 -*-

import pymysql
db = pymysql.connect(host="localhost", user="root", password="root", database="addressbook")
cursor = db.cursor()
cursor.execute("SELECT wxid,superior,fullname,listname,tag,detail,longitude,latitude,phone,address,remark,unit FROM addressbook")
lists = cursor.fetchall()
jsonStr = ''
for lg in lists:
    _id = str(lg[0])
    superior = str(lg[1])
    fullname = str(lg[2])
    listname = str(lg[3])
    tag = str(lg[4])
    detail = str(lg[5])
    longitude = str(lg[6])
    latitude = str(lg[7])
    if str(lg[8]) == '':
        phone = '""'
    else:
        phone = '["' + str(lg[8]) + '"]'
    address = str(lg[9])
    remark = str(lg[10])
    unit = str(lg[11])
    jsonStr = jsonStr + '{"_id":"' + _id + '","superior":"' + superior + '","fullname":"' + fullname \
              + '","listname":"' + listname + '","tag":"' + tag + '","detail":"' + detail \
              + '","longitude":"' + longitude + '","latitude":"' + latitude + '","phone":' + phone \
              + ',"address":"' + address + '","remark":"' + remark + '","unit":"' + unit + '"}\n'
print(jsonStr)

