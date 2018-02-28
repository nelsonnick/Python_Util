#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import re
files = open("C:\\汇总.txt", "w", encoding='utf-8')
files.write("证件号码" + "\t")
files.write("人员姓名" + "\t")
files.write("男方姓名" + "\t")
files.write("男方证件号码" + "\t")
files.write("女方姓名" + "\t")
files.write("女方证件号码" + "\t")
files.write("登记时间" + "\t")
files.write("登记业务" + "\n")
files.close()
file_total = open('c:/婚姻.txt', 'r')
line = file_total.readline()
while line:
    sfzhm = line.split("\t")[0]
    xm = line.split("\t")[1]
    file_person = open("C:\\婚姻状况\\" + sfzhm + xm + ".txt", "r", encoding='utf-8')

    details = re.findall(r'<td\s*height="22" align="center"\s*>.+?</td>|<td\s*height="22" align="center"\s*></td>', file_person.read())
    file_result = open("C:\\婚姻状况分析\\" + sfzhm + xm + ".txt", "w", encoding='utf-8')
    for detail in details:
        information = re.findall(r'>.+?</td>|></td>', detail)
        for info in information:
            if info[1:5] != "<a t" and info[1:5] != "<a h":
                file_result.write(info[1:len(info) - 5])
                file_result.write("\t")
            else:
                if info[1:5] != "<a h":
                    file_result.write("\n")
                    break
                else:
                    break
    file_result.close()
    file_person.close()

    file_all = open("C:\\汇总.txt", "a", encoding='utf-8')
    file_one = open("C:\\婚姻状况分析\\" + sfzhm + xm + ".txt", "r", encoding='utf-8')
    line_one = file_one.readline()
    while line_one:
        file_all.write(sfzhm + "\t")
        file_all.write(xm + "\t")
        file_all.write(line_one.split("\t")[0] + "\t")
        file_all.write(line_one.split("\t")[1] + "\t")
        file_all.write(line_one.split("\t")[2] + "\t")
        file_all.write(line_one.split("\t")[3] + "\t")
        file_all.write(line_one.split("\t")[4] + "\t")
        file_all.write(line_one.split("\t")[5] + "\n")
        line_one = file_one.readline()
    file_one.close()
    file_all.close()
    print(sfzhm + xm + '已完成读取！')
    line = file_total.readline()
file_total.close()
