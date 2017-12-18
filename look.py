#!/usr/bin/env python3
# encoding:UTF-8
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


def compare(img1, img2):
    num = 0
    for x in range(0, 25):
        for y in range(0, 22):
            if img1.getpixel((x, y)) == img2.getpixel((x, y)):
                num = num + 1
            else:
                num = num
    return num/550


# for num in range(1, 100):
#     image = Image.open("C:\pic\pic" + str(num) + ".jpg")
#
#     out = image.convert('L').point(get_bin_table(), '1')
#     out.crop((5, 3, 30, 25)).save("c:\pic2\psza" + str(num) + ".jpg")
#     out.crop((28, 3, 53, 25)).save("c:\pic2\pfh" + str(num) + ".jpg")
#     out.crop((54, 3, 79, 25)).save("c:\pic2\pszb" + str(num) + ".jpg")
# num = 82
# image = Image.open("C:\pic\pic" + str(num) + ".jpg")
#
# out = image.convert('L').point(get_bin_table(), '1')
# out.save("c:\pic3\pic" + str(num) + ".jpg")
# out.crop((5, 3, 30, 25)).save("c:\pic3\psza" + str(num) + ".jpg")
# out.crop((28, 3, 53, 25)).save("c:\pic3\pfh" + str(num) + ".jpg")
# out.crop((54, 3, 79, 25)).save("c:\pic3\pszb" + str(num) + ".jpg")


def get_type(out):
    types = ''
    rate = 0
    loc = 'C:\p'
    for jia in range(1, 100):
        img = Image.open(loc + "\jia\jia (" + str(jia) + ").jpg")
        o = compare(out.crop((28, 3, 53, 25)), img)
        if o > rate:
            rate = o
            types = '+'
    for jian in range(1, 100):
        img = Image.open(loc + "\jian\jian (" + str(jian) + ").jpg")
        o = compare(out.crop((28, 3, 53, 25)), img)
        if o > rate:
            rate = o
            types = '-'
    for cheng in range(1, 100):
        img = Image.open(loc + "\cheng\cheng (" + str(cheng) + ").jpg")
        o = compare(out.crop((28, 3, 53, 25)), img)
        if o > rate:
            rate = o
            types = '*'
    for chu in range(1, 100):
        img = Image.open(loc + "\chu\chu (" + str(chu) + ").jpg")
        o = compare(out.crop((28, 3, 53, 25)), img)
        if o > rate:
            rate = o
            types = '/'
    return types


def get_number(out, box):
    number = ''
    rate = 0
    loc = 'C:\p'
    for num1 in range(1, 100):
        img = Image.open(loc + "\m1\m1 (" + str(num1) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '1'
    for num2 in range(1, 100):
        img = Image.open(loc + "\m2\m2 (" + str(num2) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '2'
    for num3 in range(1, 100):
        img = Image.open(loc + "\m3\m3 (" + str(num3) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '3'
    for num4 in range(1, 100):
        img = Image.open(loc + "\m4\m4 (" + str(num4) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '4'
    for num5 in range(1, 100):
        img = Image.open(loc + "\m5\m5 (" + str(num5) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '5'
    for num6 in range(1, 100):
        img = Image.open(loc + "\m6\m6 (" + str(num6) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '6'
    for num7 in range(1, 100):
        img = Image.open(loc + "\m7\m7 (" + str(num7) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '7'
    for num8 in range(1, 100):
        img = Image.open(loc + "\m8\m8 (" + str(num8) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '8'
    for num9 in range(1, 100):
        img = Image.open(loc + "\m9\m9 (" + str(num9) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '9'
    for num0 in range(1, 100):
        img = Image.open(loc + "\m0\m0 (" + str(num0) + ").jpg")
        o = compare(out.crop(box), img)
        if o > rate:
            rate = o
            number = '0'
    return number


def get_result(out):
    if get_number(out, (5, 3, 30, 25)) == "":
        return 999
    if get_number(out, (54, 3, 79, 25)) == "":
        return 999
    if get_type(out) == "":
        return 999
    one = int(get_number(out, (5, 3, 30, 25)))
    two = int(get_number(out, (54, 3, 79, 25)))
    if get_type(out) == "+":
        return one + two
    elif get_type(out) == "-":
        return one + two
    elif get_type(out) == "*":
        return one * two
    elif get_type(out) == "/":
        if two == 0:
            return 999
        else:
            return one / two
    else:
        return 999


# image = Image.open("C:\image.jpg")
# out = Image.open("C:\image.jpg").convert('L').point(get_bin_table(), '1')
# box = (54, 3, 79, 25)
# out.crop(box).show()
# print(get_number(out, box))
#
# print(get_type(out))
