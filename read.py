#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import os
import re

file = open("C:\\9.txt", "r", encoding='utf-8')
file_all = open("C:\\8.txt", "a", encoding='utf-8')
# file_all.write("sblb" + "\t")
# file_all.write("bflsh" + "\t")
# file_all.write("pxrylb" + "\t")
# file_all.write("bqbh" + "\t")
# file_all.write("bqmc" + "\t")
# file_all.write("pxjgbh" + "\t")
# file_all.write("pxjgmc" + "\t")
# file_all.write("qjjbrq" + "\t")
# file_all.write("zymc" + "\t")
# file_all.write("pxlx" + "\t")
# file_all.write("kkrq" + "\t")
# file_all.write("jieyhgrs" + "\t")
# file_all.write("sjje" + "\t")
# file_all.write("jkrq" + "\n")
line = file.readline()
while line:
    ones = re.findall(r'<r.+? column_blank_dw', line)
    for one in ones:
        sblb_ = re.findall(r'sblb=.+?zymc', one)[0]
        sblb = sblb_[6:len(sblb_) - 6]
        bflsh_ = re.findall(r'bflsh=.+?pxjgbh', one)[0]
        bflsh = bflsh_[7:len(bflsh_)-8]
        pxrylb_ = re.findall(r'pxrylb=.+?ssqxbh', one)[0]
        pxrylb = pxrylb_[8:len(pxrylb_) - 8]
        bqbh_ = re.findall(r'bqbh=.+?bqmc', one)[0]
        bqbh = bqbh_[6:len(bqbh_) - 6]
        bqmc_ = re.findall(r'bqmc=.+?pxrylb', one)[0]
        bqmc = bqmc_[6:len(bqmc_) - 8]
        pxjgbh_ = re.findall(r'pxjgbh=.+?pxjgmc', one)[0]
        pxjgbh = pxjgbh_[8:len(pxjgbh_) - 8]
        pxjgmc_ = re.findall(r'pxjgmc=.+?bqbh', one)[0]
        pxjgmc = pxjgmc_[8:len(pxjgmc_) - 6]
        zymc_ = re.findall(r'zymc=.+?pxlx', one)[0]
        qjjbrq_ = re.findall(r'qjjbrq=.+?column', one)[0]
        qjjbrq = qjjbrq_[8:len(qjjbrq_) - 8]
        zymc = zymc_[6:len(zymc_) - 6]
        pxlx_ = re.findall(r'pxlx=.+?pxdj', one)[0]
        pxlx = pxlx_[6:len(pxlx_) - 6]
        kkrq_ = re.findall(r'kkrq=.+?jkrq', one)[0]
        kkrq = kkrq_[6:len(kkrq_) - 6]
        jkrq_ = re.findall(r'jkrq=.+?ks', one)[0]
        jkrq = jkrq_[6:len(jkrq_) - 4]
        jieyhgrs_ = re.findall(r'jieyhgrs=.+?jieybfje', one)[0]
        jieyhgrs = jieyhgrs_[10:len(jieyhgrs_) - 10]
        sjje_ = re.findall(r'sjje=.+?qjbl', one)[0]
        sjje = sjje_[6:len(sjje_) - 6]
        file_all.write(sblb + "\t")
        file_all.write(bflsh + "\t")
        file_all.write(pxrylb + "\t")
        file_all.write(bqbh + "\t")
        file_all.write(bqmc + "\t")
        file_all.write(pxjgbh + "\t")
        file_all.write(pxjgmc + "\t")
        file_all.write(qjjbrq + "\t")
        file_all.write(zymc + "\t")
        file_all.write(pxlx + "\t")
        file_all.write(kkrq + "\t")
        file_all.write(jieyhgrs + "\t")
        file_all.write(sjje + "\t")
        file_all.write(jkrq + "\n")
        print(one)
    line = file.readline()
file.close()
file_all.close()
