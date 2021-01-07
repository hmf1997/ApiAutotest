#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 15:08
# @Author  : He Min Fei
# @File    : test.py
import  requests
r=requests.get("http://jy001:8081/futureloan/mvc/api/member/list")
d=r.json()['data']
for i in d:
    print(i['mobilephone'])
    if  i['mobilephone']=='13689105271':
        print(i['mobilephone'])
        break
