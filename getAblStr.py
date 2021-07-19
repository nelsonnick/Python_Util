#!/user/bin/env python
# -*- coding: UTF-8 -*-

import pymysql

db = pymysql.connect(host="localhost", user="root", password="root", database="addressbook")
cursor0 = db.cursor()
cursor0.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + "37C" + "'")
level0s = cursor0.fetchall()
jsonStr = ''
for level0 in level0s:
    _id0 = str(level0[0])
    listname0 = str(level0[1])
    tag0 = str(level0[2])
    detail0 = str(level0[3])
    unit0 = str(level0[4])
    cursor1 = db.cursor()
    cursor1.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + _id0 + "'")
    level1s = cursor1.fetchall()
    for level1 in level1s:
        _id1 = str(level1[0])
        listname1 = str(level1[1])
        tag1 = str(level1[2])
        detail1 = str(level1[3])
        unit1 = str(level1[4])
        jsonStr = jsonStr + '{"_id":"' + _id1 + '","name":"' + listname1 + '","tag":"' + tag1 +'","unit":"'+unit1 + '","detail":"' + detail1 + '","child":['

        cursor2 = db.cursor()
        cursor2.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + _id1 + "'")
        level2s = cursor2.fetchall()
        for level2 in level2s:
            _id2 = str(level2[0])
            listname2 = str(level2[1])
            tag2 = str(level2[2])
            detail2 = str(level2[3])
            unit2 = str(level2[4])
            jsonStr = jsonStr + '{"_id":"' + _id2 + '","name":"' + listname2 + '","tag":"' + tag2 +'","unit":"'+unit2 + '","detail":"' + detail2 + '","child":['

            cursor3 = db.cursor()
            cursor3.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + _id2 + "'")
            level3s = cursor3.fetchall()
            for level3 in level3s:
                _id3 = str(level3[0])
                listname3 = str(level3[1])
                tag3 = str(level3[2])
                detail3 = str(level3[3])
                unit3 = str(level3[4])
                jsonStr = jsonStr + '{"_id":"' + _id3 + '","name":"' + listname3 + '","tag":"' + tag3 +'","unit":"'+unit3 + '","detail":"' + detail3 + '","child":['

                cursor4 = db.cursor()
                cursor4.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + _id3 + "'")
                level4s = cursor4.fetchall()
                for level4 in level4s:
                    _id4 = str(level4[0])
                    listname4 = str(level4[1])
                    tag4 = str(level4[2])
                    detail4 = str(level4[3])
                    unit4 = str(level4[4])
                    jsonStr = jsonStr + '{"_id":"' + _id4 + '","name":"' + listname4 + '","tag":"' + tag4 +'","unit":"'+unit4 +  '","detail":"' + detail4 + '","child":['

                    cursor5 = db.cursor()
                    cursor5.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + _id4 + "'")
                    level5s = cursor5.fetchall()
                    for level5 in level5s:
                        _id5 = str(level5[0])
                        listname5 = str(level5[1])
                        tag5 = str(level5[2])
                        detail5 = str(level5[3])
                        unit5 = str(level5[4])
                        jsonStr = jsonStr + '{"_id":"' + _id5 + '","name":"' + listname5 + '","tag":"' + tag5 +'","unit":"'+unit5 + '","detail":"' + detail5 + '","child":['

                        cursor6 = db.cursor()
                        cursor6.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + _id5 + "'")
                        level6s = cursor6.fetchall()
                        for level6 in level6s:
                            _id6 = str(level6[0])
                            listname6 = str(level6[1])
                            tag6 = str(level6[2])
                            detail6 = str(level6[3])
                            unit6 = str(level6[4])
                            jsonStr = jsonStr + '{"_id":"' + _id6 + '","name":"' + listname6 + '","tag":"' + tag6 +'","unit":"'+unit6 + '","detail":"' + detail6 + '","child":['

                            cursor7 = db.cursor()
                            cursor7.execute("SELECT wxid,listname,tag,detail,unit FROM addressbook WHERE superior='" + _id6 + "'")
                            level7s = cursor7.fetchall()
                            for level7 in level7s:
                                _id7 = str(level7[0])
                                listname7 = str(level7[1])
                                tag7 = str(level7[2])
                                detail7 = str(level7[3])
                                unit7 = str(level7[4])
                                jsonStr = jsonStr + '{"_id":"' + _id7 + '","name":"' + listname7 + '","tag":"' + tag7 +'","unit":"'+unit7 + '","detail":"' + detail7 + '"},'


                            jsonStr = jsonStr[:-1] + ']},'
                        jsonStr = jsonStr[:-1] + ']},'
                    jsonStr = jsonStr[:-1] + ']},'
                jsonStr = jsonStr[:-1] + ']},'
            jsonStr = jsonStr[:-1] + ']},'
        jsonStr = jsonStr[:-1] + ']},'
    jsonStr = jsonStr[:-1] + ']}'
j = jsonStr.replace(',"child":]', '')
j = 'export default [' + j + ']'
print(j)
