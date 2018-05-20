import requests
import json
import os


# 创建目录
def create_file():
    file = open("D:/视频/目录.txt", "w", encoding='utf-8')
    file.write("主机地址" + "\t")
    file.write("文件名称" + "\t")
    file.write("标题" + "\t")
    file.write("学校" + "\t")
    file.write("教师" + "\t")
    file.write("年级" + "\n")
    file.close()


# 下载文件
def down_mp4(host, file_name):
    if os.path.exists("D:/视频/" + file_name):
        print(file_name + '已存在，不需要再次下载！')
    else:
        url = host + "/disk/content/" + file_name
        r = requests.get(url)
        file = open("D:/视频/" + file_name, "wb")
        file.write(r.content)
        file.close()
        print(file_name + '下载完成！')


def down(m, p, ps):
    # m = "workList"
    # p = "2"
    # ps = "12"
    api = 'http://jnsspt.jndjg.cn/app.php?m=' + m + '&p=' + p + '&ps=' + ps
    data_post = {
        'subject': '18',
        'study_section': '1',
        'qw': '',
        'actionTimeStatus': '进行中',
        'actionType': '1',
        'actionYear': '2018',
        'action': ''
    }
    r = requests.post(api, data=data_post)
    js = json.loads(r.content)
    for i in js['data']:
        file_name = i['myFile']
        title = i['title']
        school_name = i['schoolName']
        teacher_name = i['realname']
        study_grade = i['study_grade']
        host = i['playHostUrl'].split(',')[0]
        # down_mp4(host, file_name)
        file = open("D:/视频/目录.txt", "a", encoding='utf-8')
        file.write(host + "\t")
        file.write(file_name + "\t")
        file.write(title + "\t")
        file.write(school_name + "\t")
        file.write(teacher_name + "\t")
        file.write(study_grade + "\n")
        file.close()


create_file()
down("workList", "1", "80")
