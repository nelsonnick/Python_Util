#!/user/bin/env python
# coding=utf-8
import pymysql

# CREATE TABLE `abl` (
# `_id` varchar(255) CHARACTER SET utf8 NOT NULL COMMENT '序号',
# `superior` varchar(255) CHARACTER SET utf8 NULL COMMENT '上级部门序号',
# `fullname` varchar(255) CHARACTER SET utf8 NULL COMMENT '全称',
# `showname` varchar(255) CHARACTER SET utf8 NULL COMMENT '简称',
# `phone` varchar(255) CHARACTER SET utf8 NULL COMMENT '联系电话',
# `address` varchar(255) CHARACTER SET utf8 NULL COMMENT '联系地址',
# `level` varchar(255) CHARACTER SET utf8 NULL COMMENT '层级',
# `longitude` varchar(255) CHARACTER SET utf8 NULL COMMENT '经度',
# `latitude` varchar(255) CHARACTER SET utf8 NULL COMMENT '纬度',
# `remark` varchar(255) CHARACTER SET utf8 NULL COMMENT '备注',
# `istype` varchar(1) CHARACTER SET utf8 NULL COMMENT '1是层级0不是层级',
# PRIMARY KEY (`_id`)
# );

str0 = ''
str1 = ''
str2 = ''
str3 = ''
str4 = ''
str5 = ''
str6 = ''
str7 = ''
str8 = ''
str9 = ''
stra = ''

db = pymysql.connect("localhost", "root", "root", "abl")

cursor = db.cursor()
cursor.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior="+"01")
data = cursor.fetchall()
for d1 in data:
    cursor1 = db.cursor()
    cursor1.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d1[0]))
    if cursor1.rowcount == 0:
        str1 = str1 + '{"label":"' + d1[2] + '","value":"' + d1[0] + '},'
    else:
        data1 = cursor1.fetchall()
        for d2 in data1:
            cursor2 = db.cursor()
            cursor2.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d2[0]))
            if cursor2.rowcount == 0:
                str2 = str2 + '{"label":"' + d2[2] + '","value":"' + d2[0] + '},'
            else:
                data2 = cursor2.fetchall()
                for d3 in data2:
                    cursor3 = db.cursor()
                    cursor3.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d3[0]))
                    if cursor3.rowcount == 0:
                        str3 = str3 + '{"label":"' + d3[2] + '","value":"' + d3[0] + '},'
                    else:
                        data3 = cursor3.fetchall()
                        for d4 in data3:
                            cursor4 = db.cursor()
                            cursor4.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d4[0]))
                            if cursor4.rowcount == 0:
                                str4 = str4 + '{"label":"' + d4[2] + '","value":"' + d4[0] + '},'
                            else:
                                data4 = cursor4.fetchall()
                                for d5 in data4:
                                    cursor5 = db.cursor()
                                    cursor5.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d5[0]))
                                    if cursor5.rowcount == 0:
                                        str5 = str5 + '{"label":"' + d5[2] + '","value":"' + d5[0] + '},'
                                    else:
                                        data5 = cursor5.fetchall()
                                        for d6 in data5:
                                            cursor6 = db.cursor()
                                            cursor6.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d6[0]))
                                            if cursor6.rowcount == 0:
                                                str6 = str6 + '{"label":"' + d6[2] + '","value":"' + d6[0] + '},'
                                            else:
                                                data6 = cursor6.fetchall()
                                                for d7 in data6:
                                                    cursor7 = db.cursor()
                                                    cursor7.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d7[0]))
                                                    if cursor7.rowcount == 0:
                                                        str7 = str7 + '{"label":"' + d7[2] + '","value":"' + d7[0] + '},'
                                                    else:
                                                        data7 = cursor7.fetchall()
                                                        for d8 in data7:
                                                            cursor8 = db.cursor()
                                                            cursor8.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d8[0]))
                                                            if cursor8.rowcount == 0:
                                                                str8 = str8 + '{"label":"' + d8[2] + '","value":"' + d8[0] + '},'
                                                            else:
                                                                data8 = cursor8.fetchall()
                                                                for d9 in data8:
                                                                    cursor9 = db.cursor()
                                                                    cursor9.execute("SELECT _id, superior, showname, istype FROM abl WHERE superior=" + str(d9[0]))
                                                                    if cursor9.rowcount == 0:
                                                                        str9 = str9 + '{"label":"' + d9[2] + '","value":"' + d9[0] + '},'
                                                                    else:
                                                                        data9 = cursor9.fetchall()
                                                                        for da in data9:
                                                                            stra = stra + '{"label":"' + da[2] + '","value":"' + da[0] + '},'


                                                                        str9 = str9 + '{"label":"' + d9[2] + '","value":"' + d9[0] + '","children":[' + stra[:-1] + ']},'
                                                                        stra = ''
                                                                str8 = str8 + '{"label":"' + d8[2] + '","value":"' + d8[0] + '","children":[' + str9[:-1] + ']},'
                                                                str9 = ''
                                                        str7 = str7 + '{"label":"' + d7[2] + '","value":"' + d7[0] + '","children":[' + str8[:-1] + ']},'
                                                        str8 = ''
                                                str6 = str6 + '{"label":"' + d6[2] + '","value":"' + d6[0] + '","children":[' + str7[:-1] + ']},'
                                                str7 = ''
                                        str5 = str5 + '{"label":"' + d5[2] + '","value":"' + d5[0] + '","children":[' + str6[:-1] + ']},'
                                        str6 = ''
                                str4 = str4 + '{"label":"' + d4[2] + '","value":"' + d4[0] + '","children":[' + str5[:-1] + ']},'
                                str5 = ''
                        str3 = str3 + '{"label":"' + d3[2] + '","value":"' + d3[0] + '","children":[' + str4[:-1] + ']},'
                        str4 = ''
                str2 = str2 + '{"label":"' + d2[2] + '","value":"' + d2[0] + '","children":[' + str3[:-1] + ']},'
                str3 = ''
        str1 = str1 + '{"label":"' + d1[2] + '","value":"' + d1[0] + '","children":[' + str2[:-1] + ']},'
        str2 = ''
str0 = 'export var data = [' + str1[:-1] + ']'
# 关闭数据库连接
db.close()
print(str0)
