#!/user/bin/env python
# coding=utf-8
import pymysql


str1 = ''
str2 = ''
str3 = ''
str4 = ''
str5 = ''
db = pymysql.connect("localhost", "root", "root", "address_book")
cursor1 = db.cursor()
cursor1.execute("SELECT id, name FROM county")
countis = cursor1.fetchall()
for county in countis:
    county_id = county[0]
    county_name = county[1]
    cursor2 = db.cursor()
    cursor2.execute("SELECT id, name FROM bureau WHERE cid="+str(county_id))
    bureaus = cursor2.fetchall()
    for bureau in bureaus:
        bureau_id = bureau[0]
        bureau_name = bureau[1]
        cursor3 = db.cursor()
        cursor3.execute("SELECT id,name,address,img,latitude,longitude,duty,remark FROM department WHERE bid=" + str(bureau_id))
        departments = cursor3.fetchall()
        for department in departments:
            department_id = department[0]
            department_name = department[1]
            department_address = department[2]
            department_img = department[3]
            department_latitude = department[4]
            department_longitude = department[5]
            department_duty = department[6]
            department_remark = department[7]
            cursor4 = db.cursor()
            cursor4.execute("SELECT id,name,address,latitude,longitude,phone,office FROM contact WHERE did=" + str(department_id))
            contacts = cursor4.fetchall()
            for contact in contacts:
                contact_id = contact[0]
                contact_name = contact[1]
                contact_address = contact[2]
                contact_latitude = contact[3]
                contact_longitude = contact[4]
                contact_phone = contact[5]
                contact_office = contact[6]
                str1 = str1 + '{name:"'+contact_name+'",phone:"'+contact_phone+'"},'
            str2 = str2 + '{name:"' + department_name + '",contact:[' + str1[:-1] + '],address:"' + department_address + '",img:"' + department_img + '",latitude:'+str(department_latitude)+',longitude:'+str(department_longitude)+',duty:"'+department_duty+'",remark:"'+department_remark+'"},'
            str1 = ''
        str3 = str3 + '{name:"' + bureau_name +'",department:[' + str2[:-1] + ']},'
        str2 = ''
    str4 = str4 + '{name:"' + county_name + '",bureau:[' + str3[:-1] + ']},'
str5 = 'export var county = [' + str4[:-1] + ']'
#
# data = cursor.fetchone()
# 关闭数据库连接
db.close()
print(str5)
