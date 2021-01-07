#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 15:29
# @Author  : He Min Fei
# @File    : DbOp.py
'''
面试题
'''
import pymysql

def connect(db) :
    '''
    连接数据库
    ：param db：字典格式的数据db = {'ip':'jy001','port':'4406','user':'root','pwd':'123456','dbname':'future'}

    :param db:
    :return: 连接对象
    '''
    #拿出配置文件的属性
    ip=db['ip']
    port=db['port']
    user=db['user']
    pwd=db['pwd']
    name = db['dbname']
    try:
        conn=pymysql.connect(host=ip, user=user, password=pwd,
             database=name, port=int(port),
             charset='utf8')
        print("数据库连接成功")
        return conn
    except Exception as e:
        print(f"数据库连接失败，原因：{e}")
def disconnect(conn):
    try:
        conn.close()
        print("数据库断开成功")
    except Exception as e:
        print(f"数据库断开异常的原因是：{e}")
def execute(conn,sql):
    try:
        c=conn.cursor()#获取游标
        c.execute(sql)
        c.close()
        conn.commit()
        print(f"数据库操作{sql}语句成功")
    except Exception as e:
        print("数据库操作失败，原因是："+str(e))

