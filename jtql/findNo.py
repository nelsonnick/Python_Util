#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import openpyxl

filesLocation = 'D:\\excel'
fileList = []
for root, dirs, files in os.walk(filesLocation):
    for file in files:
        fileList.append(os.path.join(root, file).split("\\")[2].split(".")[0])
departmentList = fileList
list = ['物价局','纪委监委', '区委办', '组织部', '宣传部', '统战部', '政法委', '区委编办', '机关工委', '老干部局', '党校', '总工会', '团委','妇联','科协','侨联','残联','工商联','人大','政协','法院','检察院','政府办','发改局','教体局','科技局','工信局','民政局','司法局','财政局','人社局','自然资源局','住建局','城管局','水务局','农业农村局','商务局','文旅局','卫健局','退役军人局','应急管理局','审计局','市场监管局','统计局','医保局','投促局','行政审批服务局','信访局','经济开发区','体育事业发展中心','振兴街','五里沟','青年公园','南辛庄','中大槐树','道德街','营市街','西市场','张庄路','段店北路','匡山','美里湖','兴福','玉清湖','腊山','吴家堡']

for i in list:
    if i in departmentList:
        pass
    else:
        print(i)
