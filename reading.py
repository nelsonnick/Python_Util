#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import xlrd

file = open("C:\\2.txt", "a", encoding='utf-8')
for k in range(1, 212):
    names = 'c:/b/' + str(k) + '.xls'
    sheet = xlrd.open_workbook(names).sheet_by_name('sheet1')
    for i in range(1, sheet.nrows):
        for j in range(0, sheet.ncols):
            file.write(str(sheet.row_values(i)[j]) + "\t")
        file.write(str(sheet.row_values(i)[j]) + "\n")
    print(names + "-----OK")
file.close()
