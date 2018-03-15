#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 通过向服务器访问获取题库JSON字符串，再生成JS文件
# 使用浏览器登录灯塔（除了IE，其他随意），在正式答题页面按F12调出控制台（Console），将C盘根目录下《灯塔.js》中的JS代码复制进去，按回车执行即可，请手动控制交卷时间。
import requests
import json

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = "http://xxjs.dtdjzx.gov.cn/quiz-api/subject_info/randomList"
j = '{"msg":"操作成功!","code":200,"success":true,"data":{"subjectInfoList":['
subjectTitleList = []
topicList = []
for i in range(1, 100):
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
            topicList.append('{"subjectTitle":"' + subjectTitle + '",'+ \
                '"subjectType":"' + subjectType  + '",'+ \
                '"answer":"' + answer  + '",'+ \
                '"optionInfoList": [' + \
                '{"optionTitle": "' + optionTitleA + '"},' + \
                '{"optionTitle": "' + optionTitleB + '"},' + \
                '{"optionTitle": "' + optionTitleC + '"},' + \
                '{"optionTitle": "' + optionTitleD + '"}]' + '}')
            subjectTitleList.append(subjectTitle)
for i in topicList:
    j = j + i + ','

questions = json.loads(j.rstrip(',')+']}}')['data']['subjectInfoList']
topics = []
for question in questions:
    subjectType = question['subjectType']
    subjectTitle = question['subjectTitle']
    optionTitleA = question['optionInfoList'][0]['optionTitle']
    optionTitleB = question['optionInfoList'][1]['optionTitle']
    optionTitleC = question['optionInfoList'][2]['optionTitle']
    optionTitleD = question['optionInfoList'][3]['optionTitle']
    answer = question['answer']
    if subjectType == '0':
        if subjectTitle.count('（）') == 1:
            if answer == 'A':
                topic = subjectTitle.replace('（）', optionTitleA)
                topics.append(topic)
            elif answer == 'B':
                topic = subjectTitle.replace('（）', optionTitleB)
                topics.append(topic)
            elif answer == 'C':
                topic = subjectTitle.replace('（）', optionTitleC)
                topics.append(topic)
            elif answer == 'D':
                topic = subjectTitle.replace('（）', optionTitleD)
                topics.append(topic)
            else:
                topics.append(subjectTitle)
        elif subjectTitle.count('（）') == 2:
            if answer == 'A':
                s = optionTitleA.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            elif answer == 'B':
                s = optionTitleB.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            elif answer == 'C':
                s = optionTitleC.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            elif answer == 'D':
                s = optionTitleD.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            else:
                topics.append(subjectTitle)
        elif subjectTitle.count('（）') == 3:
            if answer == 'A':
                s = optionTitleA.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            elif answer == 'B':
                s = optionTitleB.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            elif answer == 'C':
                s = optionTitleC.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            elif answer == 'D':
                s = optionTitleD.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            else:
                topics.append(subjectTitle)
        elif subjectTitle.count('（）') == 4:
            if answer == 'A':
                s = optionTitleA.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            elif answer == 'B':
                s = optionTitleB.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            elif answer == 'C':
                s = optionTitleC.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            elif answer == 'D':
                s = optionTitleD.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            else:
                topics.append(subjectTitle)
        else:
            pass
    elif subjectType == '1':
        if subjectTitle.count('（）') == 1:
            As = ''
            if answer.find('A') != -1:
                As = As + optionTitleA + '，'
            if answer.find('B') != -1:
                As = As + optionTitleB + '，'
            if answer.find('C') != -1:
                As = As + optionTitleC + '，'
            if answer.find('D') != -1:
                As = As + optionTitleD
            topic = subjectTitle.replace('（）', As.rstrip('，'))
            topics.append(topic)
        elif subjectTitle.count('（') == 2:
            if answer.find('A') != -1:
                topic = subjectTitle.replace('（）', optionTitleA, 1)
            if answer.find('B') != -1:
                topic = topic.replace('（）', optionTitleB, 1)
            if answer.find('C') != -1:
                topic = topic.replace('（）', optionTitleC, 1)
            if answer.find('D') != -1:
                topic = topic.replace('（）', optionTitleD, 1)
            topics.append(topic)
        elif subjectTitle.count('（）') == 3:
            if answer.find('A') != -1:
                topic = subjectTitle.replace('（）', optionTitleA, 1)
            if answer.find('B') != -1:
                topic = topic.replace('（）', optionTitleB, 1)
            if answer.find('C') != -1:
                topic = topic.replace('（）', optionTitleC, 1)
            if answer.find('D') != -1:
                topic = topic.replace('（）', optionTitleD, 1)
            topics.append(topic)
        elif subjectTitle.count('（）') == 4:
            if answer.find('A') != -1:
                topic = subjectTitle.replace('（）', optionTitleA, 1)
            if answer.find('B') != -1:
                topic = topic.replace('（）', optionTitleB, 1)
            if answer.find('C') != -1:
                topic = topic.replace('（）', optionTitleC, 1)
            if answer.find('D') != -1:
                topic = topic.replace('（）', optionTitleD, 1)
            topics.append(topic)
        else:
            pass
    else:
        pass

topicNumber = 0
top = open("C:\\灯塔.js", "w", encoding='utf-8')
top.write('var topic = new Array();' + '\n')
for topic in topics:
    t = 'topic[' + str(topicNumber) + ']={title:"' + topic + '"};'
    topicNumber = topicNumber + 1
    top.write(t + '\n')
js = '''
//去掉两边的空白
function trim(s){
    return trimRight(trimLeft(s));
}
//去掉左边的空白
function trimLeft(s){
    if(s == null) {
        return "";
    }
    var whitespace = new String(" \\t\\n\\r");
    var str = new String(s);
    if (whitespace.indexOf(str.charAt(0)) != -1) {
        var j=0, i = str.length;
        while (j < i && whitespace.indexOf(str.charAt(j)) != -1){
            j++;
        }
        str = str.substring(j, i);
    }
    return str;
}

//去掉右边的空白
function trimRight(s){
    if(s == null) return "";
    var whitespace = new String(" \\t\\n\\r");
    var str = new String(s);
    if (whitespace.indexOf(str.charAt(str.length-1)) != -1){
        var i = str.length - 1;
        while (i >= 0 && whitespace.indexOf(str.charAt(i)) != -1){
            i--;
        }
        str = str.substring(0, i+1);
    }
    return str;
}
localStorage.setItem('anniujia', 21)
var obj = JSON.parse(sessionStorage.getItem('allDatajingsai'))
// var allDatajingsai= ""
// var obj = JSON.parse(allDatajingsai)
var As, Bs, Cs, Ds, an, y
for (var i = 0; i < obj.data.subjectInfoList.length; i++) {
    y = i + 1
    var subjectType = obj.data.subjectInfoList[i].subjectType.toString()
    var subjectTitle = trim(obj.data.subjectInfoList[i].subjectTitle).toString()
    var optionTitleA = trim(obj.data.subjectInfoList[i].optionInfoList[0].optionTitle).toString()
    var optionTitleB = trim(obj.data.subjectInfoList[i].optionInfoList[1].optionTitle).toString()
    var optionTitleC = trim(obj.data.subjectInfoList[i].optionInfoList[2].optionTitle).toString()
    var optionTitleD = trim(obj.data.subjectInfoList[i].optionInfoList[3].optionTitle).toString()
    var S = subjectTitle.split('（）')
    As = optionTitleA.split(' ')
    Bs = optionTitleB.split(' ')
    Cs = optionTitleC.split(' ')
    Ds = optionTitleD.split(' ')
    // 一个空格
    if (S.length == 2) {
        for (var j = 0; j < topic.length; j++) {
            // 空格不在开头
            if (S[0] != '') {
                if (topic[j].title.indexOf(S[0]) != -1) {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        an = topic[j].title.replace(S[0], '').replace(S[1], '')
                        console.group("第" + y + "题：" + topic[j].title)
                        //单选题
                        if (subjectType == 0) {
                            if (an.indexOf(optionTitleA) != -1 && subjectTitle.replace("（）", optionTitleA) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[0].checked = true
                                console.log(optionTitleA)
                            }else{}
                            if (an.indexOf(optionTitleB) != -1 && subjectTitle.replace("（）", optionTitleB) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[1].checked = true
                                console.log(optionTitleB)
                            }else{}
                            if (an.indexOf(optionTitleC) != -1 && subjectTitle.replace("（）", optionTitleC) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[2].checked = true
                                console.log(optionTitleC)
                            }else{}
                            if (an.indexOf(optionTitleD) != -1 && subjectTitle.replace("（）", optionTitleD) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[3].checked = true
                                console.log(optionTitleD)
                            }else{}
                        }else{
                            if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                            if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                            if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                            if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                        }
                        console.groupEnd()
                    }
                }
            } else {
                if (topic[j].title.indexOf(S[1]) != -1) {
                    an = topic[j].title.replace(S[1], '')
                    console.group("第" + y + "题：" + topic[j].title)
                    //单选题
                    if (subjectType == 0) {
                        if (an.indexOf(optionTitleA) != -1 && subjectTitle.replace("（）", optionTitleA) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[0].checked = true
                            console.log(optionTitleA)
                        }else{}
                        if (an.indexOf(optionTitleB) != -1 && subjectTitle.replace("（）", optionTitleB) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[1].checked = true
                            console.log(optionTitleB)
                        }else{}
                        if (an.indexOf(optionTitleC) != -1 && subjectTitle.replace("（）", optionTitleC) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[2].checked = true
                            console.log(optionTitleC)
                        }else{}
                        if (an.indexOf(optionTitleD) != -1 && subjectTitle.replace("（）", optionTitleD) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[3].checked = true
                            console.log(optionTitleD)
                        }else{}
                    }else {
                        if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                        if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                        if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                        if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                    }
                    console.groupEnd()
                }
            }

        }
    // 两个空格
    } else if (S.length == 3) {
        //   选项中只有一个内容
        if (As.length == 1) {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                console.groupEnd()
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            an = topic[j].title.replace(S[1], '').replace(S[2], '')
                            console.group("第" + y + "题：" + topic[j].title)
                            if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                            if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                            if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                            if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                            console.groupEnd()
                        }
                    }
                }
            }
            //    选项中有多个内容
        } else {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA)  }
                                if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB)  }
                                if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC)  }
                                if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD)  }
                                console.groupEnd()
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            an = topic[j].title.replace(S[1], '').replace(S[2], '')
                            console.group("第" + y + "题：" + topic[j].title)
                            if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA)  }
                            if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB)  }
                            if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC)  }
                            if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD)  }
                            console.groupEnd()
                        }
                    }
                }
            }
        }
    // 三个空格
    } else if (S.length == 4) {
        //   选项中只有一个内容
        if (As.length == 1) {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                console.groupEnd()
                            }
                        }
                    }
                }
            }
        //    选项中有多个内容
        } else {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                console.groupEnd()
                            }
                        }
                    }
                }
            }
        }
    // 有四个空格
    } else {
        //   选项中只有一个内容
        if (As.length == 1) {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    if (topic[j].title.indexOf(S[4]) != -1) {
                                        an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                        console.group("第" + y + "题：" + topic[j].title)
                                        if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                        if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                        if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                        if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                        console.groupEnd()
                                    }
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                if (topic[j].title.indexOf(S[4]) != -1) {
                                    an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                }
            }
            //    选项中有多个内容
        } else {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    if (topic[j].title.indexOf(S[4]) != -1) {
                                        an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                        console.group("第" + y + "题：" + topic[j].title)
                                        if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                        if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                        if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                        if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                        console.groupEnd()
                                    }
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                if (topic[j].title.indexOf(S[4]) != -1) {
                                    an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                }
            }
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
top.write(js + '\n')
top.close()
print("代码生成完毕！")
