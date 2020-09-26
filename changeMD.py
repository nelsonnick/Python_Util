#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os

# file = r"C:\Users\nelso\OneDrive\人社政策文档库\A法律"
# for root, dirs, files in os.walk(file):
#     for f in files:
#         print(os.path.join(root, f))

filePath = r"C:\Users\nelso\OneDrive\人社政策文档库\A法律\中华人民共和国行政诉讼法.md"
oldFile = open(filePath, "r", encoding='utf-8')
line = oldFile.readline()
newFile = open("numbers.md", "a")
newFileName = os.path.basename(filePath).split('.')[0]
while line:
    if line.startswith(newFileName + "\n"):
        newFile.write("# " + newFileName + "\n")
    elif line.startswith("* "):
        if line.startswith("* 发文字号") or line.startswith("* 效力级别") \
                or line.startswith("* 文件时效") or line.startswith("* 发布日期")\
                or line.startswith("* 实施日期") or line.startswith("* 发布机关"):
            newFile.write(line)
        else:
            newFile.write(line.replace('* ', '&#8195;&#8195;'))
    elif line.startswith("\n"):
        pass
    elif line.startswith("# 基本信息"):
        newFile.write("### 基本信息\n")
    elif line.startswith("# 法律修订"):
        newFile.write("### 法律修订\n")
    elif line.startswith("# 正文"):
        newFile.write("### 正文\n")
    elif line.startswith("# 附"):
        newFile.write(line.replace('# 附', '### 附'))
    elif line.startswith("## 第"):
        newFile.write(line.replace('## 第', '##### 第'))
    elif line.startswith("### 第"):
        newFile.write(line.replace('### 第', '###### 第'))
    else:
        newFile.write(line)
    line = oldFile.readline()
oldFile.close()
newFile.close()
