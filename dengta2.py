#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = "http://xxjs.dtdjzx.gov.cn/quiz-api/subject_info/list?chapterId=7j0d8qp4r2g28ogjt5hq0cbhne"
json = requests.get(url, headers=headers).content.decode('UTF-8')
topics = open("C:\\题库JS2.txt", "w", encoding='utf-8')
topics.write('var json = ' + json + '\n')
js = '''
var topic = json.data.subjectInfoList
localStorage.setItem('anniujia', 21)
var obj = JSON.parse(sessionStorage.getItem('allDatajingsai'));
var topic = json.data.subjectInfoList
for (var i = 0; i < obj.data.subjectInfoList.length; i++) {
  for (var j = 0; j < topic.length; j++) {
    if (topic[j].subjectTitle == obj.data.subjectInfoList[i].subjectTitle) {
      y = i + 1
      console.group("第" + y + "题：" + topic[j].subjectTitle)
      var answer = topic[j].answer
      if (answer.indexOf("A") >= 0) {
        console.group(topic[j].optionInfoList[0].optionTitle)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].optionInfoList[0].optionTitle) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].optionInfoList[0].optionTitle) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].optionInfoList[0].optionTitle) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].optionInfoList[0].optionTitle) { document.getElementsByName("ra_" + i)[3].checked=true }
      }
      if (answer.indexOf("B") >= 0) {
        console.group(topic[j].optionInfoList[1].optionTitle)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].optionInfoList[1].optionTitle) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].optionInfoList[1].optionTitle) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].optionInfoList[1].optionTitle) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].optionInfoList[1].optionTitle) { document.getElementsByName("ra_" + i)[3].checked=true }
      }
      if (answer.indexOf("C") >= 0) {
        console.group(topic[j].optionInfoList[2].optionTitle)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].optionInfoList[2].optionTitle) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].optionInfoList[2].optionTitle) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].optionInfoList[2].optionTitle) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].optionInfoList[2].optionTitle) { document.getElementsByName("ra_" + i)[3].checked=true }
      }
      if (answer.indexOf("D") >= 0) {
        console.group(topic[j].optionInfoList[3].optionTitle)
        console.groupEnd()
        if (obj.data.subjectInfoList[i].optionInfoList[0].optionTitle == topic[j].optionInfoList[3].optionTitle) { document.getElementsByName("ra_" + i)[0].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[1].optionTitle == topic[j].optionInfoList[3].optionTitle) { document.getElementsByName("ra_" + i)[1].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[2].optionTitle == topic[j].optionInfoList[3].optionTitle) { document.getElementsByName("ra_" + i)[2].checked=true }
        if (obj.data.subjectInfoList[i].optionInfoList[3].optionTitle == topic[j].optionInfoList[3].optionTitle) { document.getElementsByName("ra_" + i)[3].checked=true }
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
