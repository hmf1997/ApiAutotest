#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 16:03
# @Author  : He Min Fei
# @File    : Db.py
'''

'''
from src.com.hmf.zonghe.caw import DbOp


def delete_user(db,mobilephone):
    '''
    根据手机号删除用户
    :param mobilephone: 用户手机号信息
    :param db: 数据库链接
    :return:
    '''
    coon=DbOp.connect(db)
    sql="delete  from member where mobilephone="+"'"+mobilephone+"'"
    DbOp.execute(coon,sql)
    DbOp.disconnect(coon)