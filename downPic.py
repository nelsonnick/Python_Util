#!/usr/bin/env python3
# encoding:UTF-8
import requests
from PIL import Image


def get_bin_table(threshold=210):
    """
    获取灰度转二值的映射table
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
for num in range(1, 3000):
    rt = requests.get("http://rsxf.sdhrss.gov.cn:8181/websenior/validateYzm?temp", headers=headers)
    file = open("C:\pic\pic" + str(num) + ".jpg", "wb")
    file.write(rt.content)
    file.close()
    image = Image.open("C:\pic\pic" + str(num) + ".jpg")

    out = image.convert('L').point(get_bin_table(), '1')
    out.crop((5, 3, 30, 25)).save("c:\pic2\psza" + str(num) + ".jpg")
    out.crop((28, 3, 53, 25)).save("c:\pic2\pfh" + str(num) + ".jpg")
    out.crop((54, 3, 79, 25)).save("c:\pic2\pszb" + str(num) + ".jpg")
