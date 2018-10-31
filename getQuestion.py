#!/user/bin/env python
# -*- coding: UTF-8 -*-
import pymysql
import re
import random
import requests
from bs4 import BeautifulSoup


def save_one(file, topic, law, title, a, b, c, d, answer):
    db = pymysql.connect("localhost", "root", "root", "law_enforcement")
    cursor = db.cursor()
    cursor.execute("SELECT title FROM question_all WHERE title='" + title + "'")
    sql = "INSERT INTO question_all(file,topic,law,title,a,b,c,d,answer) VALUE ('" + file + "','" + topic + "','" + law + "','" + title + "','" + a + "','" + b + "','" + c + "','" + d + "','" + answer + "')"
    cursor1 = db.cursor()
    cursor1.execute(sql)
    db.commit()
    cursor1.close()
    if cursor.fetchall().__len__() == 0:
        sql = "INSERT INTO question_one(file,topic,law,title,a,b,c,d,answer) VALUE ('" + file + "','" + topic + "','" + law + "','" + title + "','" + a + "','" + b + "','" + c + "','" + d + "','" + answer + "')"
        cursor2 = db.cursor()
        cursor2.execute(sql)
        db.commit()
        cursor2.close()
    cursor.close()
    db.close()


def save_all(file):
    tfng_list = ['tfng_1_container', 'tfng_2_container', 'tfng_3_container', 'tfng_4_container', 'tfng_5_container',
                'tfng_6_container', 'tfng_7_container', 'tfng_8_container', 'tfng_9_container', 'tfng_10_container',
                'tfng_11_container', 'tfng_12_container', 'tfng_13_container', 'tfng_14_container', 'tfng_15_container',
                'tfng_16_container', 'tfng_17_container', 'tfng_18_container', 'tfng_19_container', 'tfng_20_container',
                'tfng_21_container', 'tfng_22_container', 'tfng_23_container', 'tfng_24_container', 'tfng_25_container',
                'tfng_26_container', 'tfng_27_container', 'tfng_28_container', 'tfng_29_container', 'tfng_30_container',
                'tfng_31_container', 'tfng_32_container', 'tfng_33_container', 'tfng_34_container', 'tfng_35_container',
                'tfng_36_container', 'tfng_37_container', 'tfng_38_container', 'tfng_39_container', 'tfng_40_container'
                ]
    single_list = ['single_1_container', 'single_2_container', 'single_3_container', 'single_4_container', 'single_5_container',
                  'single_6_container', 'single_7_container', 'single_8_container', 'single_9_container', 'single_10_container',
                  'single_11_container', 'single_12_container', 'single_13_container', 'single_14_container', 'single_15_container',
                  'single_16_container', 'single_17_container', 'single_18_container', 'single_19_container', 'single_20_container',
                  'single_21_container', 'single_22_container', 'single_23_container', 'single_24_container', 'single_25_container',
                  'single_26_container', 'single_27_container', 'single_28_container', 'single_29_container', 'single_30_container',
                  'single_31_container', 'single_32_container', 'single_33_container', 'single_34_container', 'single_35_container',
                  'single_36_container', 'single_37_container', 'single_38_container', 'single_39_container', 'single_40_container'
                 ]
    multiple_list = ['multiple_1_container', 'multiple_2_container', 'multiple_3_container', 'multiple_4_container', 'multiple_5_container',
                'multiple_6_container', 'multiple_7_container', 'multiple_8_container', 'multiple_9_container', 'multiple_10_container',
                'multiple_11_container', 'multiple_12_container', 'multiple_13_container', 'multiple_14_container', 'multiple_15_container',
                'multiple_16_container', 'multiple_17_container', 'multiple_18_container', 'multiple_19_container', 'multiple_20_container'
                ]
    with open('e:/执法证/题库/' + file + '.txt', 'r', encoding='UTF-8') as f:
        html = BeautifulSoup(f.read(), "html.parser")
        for name in tfng_list:
            topic = '判断题'
            law = re.findall(r'\[(.+?)\]', BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-courseName'}).string)[0]
            title = BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionTitle'})), "html.parser").find('p').string.replace(' ', '').split('.', 1)[1]
            a = 'A.正确'
            b = 'B.错误'
            c = ''
            d = ''
            answer = BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionAnw'})), "html.parser").find('span').string
            save_one(file, topic, law, title, a, b, c, d, answer)
        print('试卷：' + file + '.txt--判断题--读取完成！')
        for name in single_list:
            topic = '单选题'
            law = re.findall(r'\[(.+?)\]', BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-courseName'}).string)[0]
            title = BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionTitle'})), "html.parser").find('p').string.replace(' ', '').split('.', 1)[1]
            a = re.findall(r'\xa0(.+?)\n\t\t\t', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[0]))[0]
            b = re.findall(r'\xa0(.+?)\n\t\t\t', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[1]))[0]
            c = re.findall(r'\xa0(.+?)\n\t\t\t', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[2]))[0]
            try:
                re.findall(r'\xa0(.+?)\n\t\t\t', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[3]))[0]
            except IndexError:
                d = ''
            else:
                d = re.findall(r'\xa0(.+?)\n\t\t\t', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[3]))[0]
            answer = BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionAnw'})), "html.parser").find('span').string
            save_one(file, topic, law, title, a, b, c, d, answer)
        print('试卷：' + file + '.txt--单选题--读取完成！')
        for name in multiple_list:
            topic = '多选题'
            law = re.findall(r'\[(.+?)\]', BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-courseName'}).string)[0]
            title = BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionTitle'})), "html.parser").find('p').string.replace(' ', '').split('.', 1)[1]
            a = re.findall(r'\xa0(.+?)\n', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[0]))[0]
            b = re.findall(r'\xa0(.+?)\n', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[1]))[0]
            c = re.findall(r'\xa0(.+?)\n', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[2]))[0]
            try:
                re.findall(r'\xa0(.+?)\n', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[3]))[0]
            except IndexError:
                d = ''
            else:
                d = re.findall(r'\xa0(.+?)\n', str(BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionOption'})), "html.parser").findAll('div', {'class': 'radioBox'})[3]))[0]
            answer = BeautifulSoup(str(BeautifulSoup(str(html.find('div', {'id': name})), "html.parser").find('div', {'class': 'exam-questionAnw'})), "html.parser").find('span').string
            save_one(file, topic, law, title, a, b, c, d, answer)
        print('试卷：' + file + '.txt--多选题--读取完成！')


def output():
    db = pymysql.connect("localhost", "root", "root", "law_enforcement")
    cursor = db.cursor()
    cursor.execute("SELECT topic, law, title,a,b,c,d,answer FROM question_one")
    questions = cursor.fetchall()
    file = 'e:/执法证/全部题目.txt'
    with open(file, 'w', encoding='utf8') as f:
        f.write('题型\t法律\t题目\t选项A\t选项B\t选项C\t选型D\t正确答案\t\n')
        for question in questions:
            topic = question[0]
            law = question[1]
            title = question[2]
            a = question[3]
            b = question[4]
            c = question[5]
            d = question[6]
            answer = question[7]
            f.write(topic + '\t')
            f.write(law + '\t')
            f.write(title + '\t')
            f.write(a + '\t')
            f.write(b + '\t')
            f.write(c + '\t')
            f.write(d + '\t')
            f.write(answer + '\t\n')
    print('导出文件-->e:/执法证/全部题目.txt！')


def output_one(topic, law):
    db = pymysql.connect("localhost", "root", "root", "law_enforcement")
    cursor = db.cursor()
    cursor.execute("SELECT title,a,b,c,d,answer FROM question_one WHERE topic='" + topic + "' AND law='" + law + "'")
    questions = cursor.fetchall()
    for question in questions:
        title = question[0]
        a = question[1]
        b = question[2]
        c = question[3]
        d = question[4]
        answer = question[5]
        file = 'e:/执法证/' + law + '-' + topic + '.txt'
        with open(file, 'a', encoding='utf8') as f:
            f.write("题目：" + title + '\n')
            f.write(a + '\n')
            f.write(b + '\n')
            f.write(c + '\n')
            f.write(d + '\n')
            f.write("正确答案：" + answer + '\n')
    print('导出文件-->e:/执法证/' + law + '-' + topic + '.txt！')


def output_all():
    topic_list = ['判断题', '单选题', '多选题']
    law_list = ['山东省题库2018新宪法', '山东省题库2018行政许可法', '山东省题库2018行政复议法', '山东省题库2018行政处罚法', '山东省题库2018行政诉讼法',
               '山东省题库2018国家赔偿法', '山东省题库2018行政强制法', '山东省题库2018山东省行政执法监督条例', '山东省题库2018山东省行政程序规定']
    for topic in topic_list:
        for law in law_list:
            output_one(topic, law)
    output()


def count(topic, law, answer):
    db = pymysql.connect("localhost", "root", "root", "law_enforcement")
    cursor = db.cursor()
    if law == '合计':
        sql = "SELECT COUNT(*) FROM question_one WHERE topic='" + topic + "' AND answer='" + answer + "'"
    else:
        sql = "SELECT COUNT(*) FROM question_one WHERE topic='" + topic + "' AND law='" + law + "' AND answer='" + answer + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    num = results[0][0]
    cursor.close()
    db.close()
    return num


def analysis():
    topic_list = ['判断题', '单选题', '多选题']
    law_list = ['山东省题库2018新宪法', '山东省题库2018行政许可法', '山东省题库2018行政复议法', '山东省题库2018行政处罚法', '山东省题库2018行政诉讼法',
                '山东省题库2018国家赔偿法', '山东省题库2018行政强制法', '山东省题库2018山东省行政执法监督条例', '山东省题库2018山东省行政程序规定', '合计']
    answer_list = ['A', 'B', 'C', 'D', 'AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'ABC', 'ACD', 'BCD', 'ABCD']

    with open('e:/执法证/' + topic_list[0] + '--统计.txt', 'w', encoding='utf8') as f:
        f.write("\tA\tB\t\n")
        for law in law_list:
            f.write(law + '\t')
            for answer in ['A', 'B']:
                f.write(str(count(topic_list[0], law, answer)) + '\t')
            f.write('\n')
    print('导出文件-->e:/执法证/' + topic_list[0] + '--统计.txt！')

    with open('e:/执法证/' + topic_list[1] + '--统计.txt', 'w', encoding='utf8') as f:
        f.write("\tA\tB\tC\tD\t\n")
        for law in law_list:
            f.write(law + '\t')
            for answer in ['A', 'B', 'C', 'D']:
                f.write(str(count(topic_list[1], law, answer)) + '\t')
            f.write('\n')
    print('导出文件-->e:/执法证/' + topic_list[1] + '--统计.txt！')

    with open('e:/执法证/' + topic_list[2] + '--统计.txt', 'w', encoding='utf8') as f:
        f.write("\tAB\tAC\tAD\tBC\tBD\tCD\tABC\tACD\tBCD\tABCD\t\n")
        for law in law_list:
            f.write(law + '\t')
            for answer in ['AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'ABC', 'ACD', 'BCD', 'ABCD']:
                f.write(str(count(topic_list[2], law, answer)) + '\t')
            f.write('\n')
    print('导出文件-->e:/执法证/' + topic_list[2] + '--统计.txt！')


# 获取验证码
def get_picture(session):
    api_picture = 'https://www.zhifa315.com/index.php/common/authimg?' + str(random.random())
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = session.get(api_picture, headers=headers)
    picture = open('e:/image.jpg', 'wb')
    picture.write(request.content)
    picture.close()


# 登录
def login(session, auth_code):
    api_login = 'https://www.zhifa315.com/index.php/ucenter/login_ex/validate'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_login = {
        'login_type': '2',
        'username': '370104198606282219',
        'password': '123456',
        'auth_code': auth_code,
        'url': '-1',
        'remember_me': '0',
        'a_id': '1088'
    }
    session.post(api_login, headers=headers, data=data_login)


# 保存题库
def get_question(session, file):
    request = session.get('https://www.zhifa315.com/index.php/ucenter/exam/show_answer2/' + file)
    with open('e:/执法证/题库/' + file + '.txt', 'w', encoding='utf8') as f:
        f.write(request.text)
    print('e:/执法证/题库/' + file + '.txt--下载完成')


def get_questions(session):
    file = open('e:/执法证/题库/下载目录.txt', "r", encoding='utf-8')
    line = file.readline()
    while line:
        get_question(session, line.replace('\n', ''))
        line = file.readline()


# 下载题库
def go():
    session = requests.session()
    get_picture(session)
    picture = input('请查看E盘根目录下的image.jpg文件，并输入验证码: ')
    login(session, picture)
    get_questions(session)


def read():
    file = open('e:/执法证/题库/读取目录.txt', "r", encoding='utf-8')
    line = file.readline()
    while line:
        save_all(line.replace('\n', ''))
        print('e:/执法证/题库/' + line.replace('\n', '') + '.txt--读取完成！')
        line = file.readline()
    output_all()
    analysis()


output_all()
analysis()
# read()
