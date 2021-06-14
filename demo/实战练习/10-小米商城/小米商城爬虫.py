#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import urllib3
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


if __name__ == "__main__":
    urllib3.disable_warnings()
    url = 'https://www.mi.com/'
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    r = session.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(r.content, 'lxml')

    # 左侧导航栏
    out_path = os.getcwd() + '/img/左侧导航栏icon/'
    categoryList = soup.find_all('li', {'class', 'category-item'})
    for category in categoryList:
        title = category.find('a').text.strip()
        print('============', title, '============')
        path = out_path + title
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

        img_list = category.find_all('li')
        for img_warapper in img_list:
            src = img_warapper.img.get('data-src')
            print(src)
            name = img_warapper.span.text.strip().replace('/', ' ').replace('"', '')
            print(name)

            # 读写图片
            suffix = src[src.rindex('.'):]
            filepath = path + '/' + name + suffix
            print(filepath)
            html = requests.get(src)
            image = Image.open(BytesIO(html.content))
            image.save(filepath)

    # 次顶部导航栏
    out_path = os.getcwd() + '/img/次顶部导航栏img/'
    categoryList = soup.find_all('li', {'class', 'nav-item'})
    for category in categoryList:
        title = category.find('span').text
        print('============', title, '============')
        path = out_path + title
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

        img_list = category.find_all('li')
        for img_warapper in img_list:
            src = img_warapper.img.get('data-src')
            print(src)
            name = img_warapper.text.strip().split('\n')[0].replace('/', ' ')
            print(name)

            # 读写图片
            suffix = src[src.rindex('.'):]
            filepath = path + '/' + name + suffix
            print(filepath)
            html = requests.get(src)
            image = Image.open(BytesIO(html.content))
            image.save(filepath)
