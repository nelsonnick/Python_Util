#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 通过向服务器访问获取题库JSON字符串，再生成JS文件（老版本JS文件）
import requests
import json

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
url = "http://xxjs.dtdjzx.gov.cn/quiz-api/subject_info/randomList"

subjectTitleList = []
topicList = []
topicNumber = 0
for j in range(1, 100):
    questions = json.loads(requests.get(url, headers=headers).content.decode('UTF-8'))['data']['subjectInfoList']
    for question in questions:
        subjectType = question['subjectType']
        subjectTitle = question['subjectTitle']
        optionTitleA = question['optionInfoList'][0]['optionTitle']
        optionTitleB = question['optionInfoList'][1]['optionTitle']
        optionTitleC = question['optionInfoList'][2]['optionTitle']
        optionTitleD = question['optionInfoList'][3]['optionTitle']
        answer = question['answer']

        if subjectTitle not in subjectTitleList:
            topic = 'topic[' + str(topicNumber) + ']={title:"' + subjectTitle + \
                    '",a:"' + optionTitleA + \
                    '",b:"' + optionTitleB + \
                    '",c:"' + optionTitleC + \
                    '",d:"' + optionTitleD + \
                    '",answer:"' + answer + '"};'
            topicList.append(topic)
            topicNumber = topicNumber + 1
            topicPrint = open("C:\\题库.txt", "a+", encoding='utf-8')
            if subjectType == '0':
                topicPrint.write('题目' + str(topicNumber) + '【单选题】：' + subjectTitle + '\n')
            else:
                topicPrint.write('题目' + str(topicNumber) + '【多选题】：' + subjectTitle + '\n')
            topicPrint.write('选项A：' + optionTitleA + '\n')
            topicPrint.write('选项B：' + optionTitleB + '\n')
            topicPrint.write('选项C：' + optionTitleC + '\n')
            topicPrint.write('选项D：' + optionTitleD + '\n')
            topicPrint.write('正确答案：' + answer + '\n')
            topicPrint.close()
            subjectTitleList.append(subjectTitle)
    print('已完成次数：' + str(j))
topics = open("C:\\题库JS.txt", "w", encoding='utf-8')
topics.write('var topic=new Array();' + '\n')
for i in topicList:
    topics.write(i + '\n')
js = '''
localStorage.setItem('anniujia', 21)
var obj=JSON.parse(sessionStorage.getItem('allDatajingsai'));
for (var i=0; i < obj.data.subjectInfoList.length; i++) {
  for (var j= 0; j < topic.length; j++) {
    if (topic[j].title == obj.data.subjectInfoList[i].subjectTitle) {
      y = i + 1
      console.group("第" + y + "题：" + topic[j].title)
      var answer=topic[j].answer
      if (answer.indexOf("A") >= 0) {
        console.group(topic[j].a)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].a) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].a) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].a) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].a) { document.getElementsByName("ra_" + i)[3].checked=true }
      }
      if (answer.indexOf("B") >= 0) {
        console.group(topic[j].b)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].b) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].b) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].b) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].b) { document.getElementsByName("ra_" + i)[3].checked=true }
      }
      if (answer.indexOf("C") >= 0) {
        console.group(topic[j].c)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].c) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].c) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].c) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].c) { document.getElementsByName("ra_" + i)[3].checked=true }
      }
      if (answer.indexOf("D") >= 0) {
        console.group(topic[j].d)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].d) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].d) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].d) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].d) { document.getElementsByName("ra_" + i)[3].checked=true }
      }
      console.groupEnd()
      break
    }
  }
}
var tags=document.getElementsByTagName("span")
for (var k in tags) {
  var tag=tags[k]
  if (tag.className == "W_fr W_mr10 W_quan W_mt22 jiaojuanss W_jiaoquancol") {
    tag.className="W_fr W_mr10 W_quan W_mt22 jiaojuanss "
    break
  }
}
'''
topics.write(js + '\n')
topics.close()
