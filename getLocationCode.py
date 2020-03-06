#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql

api = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'


def get_province():
    province = requests.get(api + 'index.html').content.decode('GB2312')
    soup = BeautifulSoup(province, 'html5lib')
    col_len = len(soup.select(".provincetr"))
    for col in range(0, col_len):
        row_len = len(soup.select(".provincetr")[col].select("a[href]"))
        for row in range(0, row_len):
            province_name = soup.select(".provincetr")[col].select("a[href]")[row].text
            province_url = soup.select(".provincetr")[col].select("a[href]")[row]['href']
            province_dict = {'code': province_url[0:2], 'name': province_name, 'url': province_url}
            # get_city(province_url)
            save_data('省区', province_dict)


def get_city(province_url):
    city = requests.get(api + province_url).content.decode('GB2312')
    soup = BeautifulSoup(city, 'html5lib')
    col_len = len(soup.select(".citytr"))
    for col in range(0, col_len):
        city_name = soup.select(".citytr")[col].select("a[href]")[1].text
        city_code = soup.select(".citytr")[col].select("a[href]")[0].text
        city_url = soup.select(".citytr")[col].select("a[href]")[0]['href']
        city_dict = {'code': city_code[0:4], 'name': city_name, 'url': city_url}
        get_county(province_url, city_url)
        save_data('市洲', city_dict)


def get_county(province_url, city_url):
    county = requests.get(api + city_url).content.decode('GB2312')
    soup = BeautifulSoup(county, 'html5lib')
    col_len = len(soup.select(".countytr"))
    for col in range(0, col_len):
        county_name = ''
        county_code = ''
        county_url = ''
        try:
            soup.select(".countytr")[col].select("a[href]")[1].text
        except IndexError:
            continue
        else:
            county_name = soup.select(".countytr")[col].select("a[href]")[1].text
            county_code = soup.select(".countytr")[col].select("a[href]")[0].text
            county_url = soup.select(".countytr")[col].select("a[href]")[0]['href']
        county_dict = {'code': county_code[0:6], 'name': county_name, 'url': county_url}
        get_town(province_url, county_url)
        save_data('区县', county_dict)


def get_town(province_url, county_url):
    town = requests.get(api + province_url[0:2] + '/' + county_url).content.decode('GB2312')
    soup = BeautifulSoup(town, 'html5lib')
    col_len = len(soup.select(".towntr"))
    for col in range(0, col_len):
        town_name = soup.select(".towntr")[col].select("a[href]")[1].text
        town_code = soup.select(".towntr")[col].select("a[href]")[0].text
        town_url = soup.select(".towntr")[col].select("a[href]")[0]['href']
        town_dict = {'code': town_code[0:9], 'name': town_name, 'url': town_url}
        get_village(province_url, county_url, town_url)
        save_data('街镇', town_dict)


def get_village(province_url, county_url, town_url):
    village = requests.get(api + province_url[0:2] + '/' + county_url[0:2] + '/' + town_url).content.decode('GB2312')
    soup = BeautifulSoup(village, 'html5lib')
    col_len = len(soup.select(".villagetr"))
    for col in range(0, col_len):
        village_code = soup.select(".villagetr")[col].select("td")[0].text
        village_type = soup.select(".villagetr")[col].select("td")[1].text
        village_name = soup.select(".villagetr")[col].select("td")[2].text
        village_dict = {'code': village_code, 'type': village_type, 'name': village_name}
        save_data('村居', village_dict)


def save_data(category_name, location_dict):
    db = pymysql.connect("localhost", "root", "root", "locationCode")
    cursor = db.cursor()
    try:
        cursor.execute(get_sql_str(category_name, location_dict))
        db.commit()
        print(category_name + ":" + location_dict['name'] + "---已保存")
    except:
        db.rollback()
    db.close()


def get_sql_str(category_name, location_dict):
    if category_name == '村居':
        return "INSERT INTO code(code, name, type, category) VALUES ('" + location_dict['code'] + "', '" \
               + location_dict['name'] + "', '" + location_dict['type'] + "','" + category_name + "')"
    else:
        return "INSERT INTO code(code, name, url, category) VALUES ('" + location_dict['code'] + "', '" \
               + location_dict['name'] + "','" + location_dict['url'] + "','" + category_name + "')"


# get_province()
# get_city('37.html')
get_county('37.html', '37/3701.html')
# get_town('37.html', '01/370102.html')
# get_village('37.html', '01/370102.html', '02/370102001.html')
