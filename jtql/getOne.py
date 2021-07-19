#!/user/bin/env python
# -*- coding: UTF-8 -*-
import os
import openpyxl


def getNum(_str):
    if _str is None:
        return 0
    else:
        return float(_str)

filesLocation = 'C:\\Users\\admin\\Desktop\\报表0706\\综合'
# 行
rowList = [12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38, 39, 40, 43, 44, 45, 46,
           47, 48, 51, 52, 53, 54, 55, 56, 57, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 77, 78, 79, 80, 81, 82, 85,
           86, 87, 88, 89, 90, 91, 92, 93, 94, 97, 98, 99, 100, 101, 104, 105, 106, 107, 108, 109, 112, 113]
# 列
columnList = [8, 9]
# 页
sheetList = ['2017年度', '2018年度', '2019年度', '2020年度', '2021年1至5月底']
# 部门
fileList = []
for root, dirs, files in os.walk(filesLocation):
    for file in files:
        fileList.append(os.path.join(root, file).split("\\")[6].split(".")[0])
departmentList = fileList
valueList = []


def check(sheet_id, row_id, column_id):
    for department_id in range(len(departmentList)):
        workbook = openpyxl.load_workbook(filesLocation + '/' + departmentList[department_id] + '.xlsx')
        worksheet = workbook[sheetList[sheet_id]]
        v = getNum(worksheet.cell(row=row_id, column=column_id).value)
        valueList.append(v)
        # print(str(departmentList[department_id]) + '\t' + str(v))

    average = sum(valueList)/len(valueList)
    print(sheetList[sheet_id] + '平均值：' + str(average))
    for num in range(len(valueList)):
        if valueList[num] > average*2:
            print('大于平均值100%：' + str(departmentList[num]) + '\t' + str(valueList[num]))
        if valueList[num] < average*0.2:
            print('小于平均值20%：' + str(departmentList[num]) + '\t' + str(valueList[num]))

# 15  个税
# 16  住房公积金
# 17  养老保险
check(4, 7, 17)
