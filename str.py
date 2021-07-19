#!/user/bin/env python
# -*- coding: UTF-8 -*-

import pymysql
db = pymysql.connect(host="localhost", user="root", password="root", database="fm")
cursor = db.cursor()
cursor.execute("SELECT DISTINCT province FROM fm")
provinceList = cursor.fetchall()
provinceStr = ''
for province in provinceList:
    province_name = str(province[0])
    cursor1 = db.cursor()
    cursor1.execute("SELECT DISTINCT city FROM fm WHERE province='" + province_name + "'")
    cityList = cursor1.fetchall()
    cityStr = ''
    for city in cityList:
        city_name = str(city[0])

        cursor2 = db.cursor()
        cursor2.execute("SELECT name,address,phone1,phone2,phone3,phone4 FROM fm WHERE city='" + city_name + "' AND province='" + province_name + "'")
        departList = cursor2.fetchall()
        departStr = ''
        for depart in departList:
            name = str(depart[0])
            address = str(depart[1])
            phone1 = str(depart[2])
            phone2 = str(depart[3])
            phone3 = str(depart[4])
            phone4 = str(depart[5])
            phone = '"' + phone1 + '"'
            if phone2 != 'None':
                phone = phone + ',"' + phone2 + '"'
            if phone3 != 'None':
                phone = phone + ',"' + phone3 + '"'
            if phone4 != 'None':
                phone = phone + ',"' + phone4 + '"'

            departStr = departStr + '{"name":"' + name + '","address":"' + address + '","phone":[' + phone + ']},'
        cityStr = cityStr + '{"name":"' + city_name + '","depart":[' + departStr + ']},'
    provinceStr = provinceStr + '{"name":"' + province_name + '","city":[' + cityStr + ']},'
jsonStr = 'export default [' + provinceStr + ']'
print(jsonStr)