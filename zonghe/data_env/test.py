#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 19:00
# @Author  : He Min Fei
# @File    : test.py
import os,configparser
path=os.getcwd()
print(path)
filepath=path+"\\test.ini"
var = configparser.ConfigParser()
var.read(filepath,encoding="utf8")
print(var.get("DATABASE","host"))
print(var.sections())
print(var.items("URL"))
print(var.options("URL"))
var.remove_section("URL")
print(var.sections())