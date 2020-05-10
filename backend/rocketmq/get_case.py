#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/19 21:19
# @Author : 程浩
# @Site : 
# @File : get_case.py
# @Software: PyCharm
import pymysql
import json
# 用于格式化输出，避免中文乱码
import codecs
# 用于按顺序将字典项存入json
from collections import OrderedDict


class GetCase:

    def __init__(self, ip, port, user_name, pass_word, database, case_name):
        self.port = int(port)
        self.ip = ip
        self.user_name = user_name
        self.pass_word = pass_word
        self.database = database
        self.case_name = case_name

    def get_case_data(self):
        # 打开数据库连接
        db = pymysql.connect(host=self.ip, port=self.port, user=self.user_name, password=self.pass_word,
                             database=self.database,
                             charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 用例名称
        # case_name = "担保品买入-单笔委托最低数量,并待报撤单-深-[主板]000001"  # type: str
        dict_case = {}
        # SQL 查询语句
        # sql = "SELECT * FROM allcase_set_io WHERE SET_NAME = (SELECT TABLE_NAME FROM allcase WHERE NAME = %s) ORDER BY sequence"
        sql = "SELECT * FROM allcase_set_io WHERE SET_NAME = %s ORDER BY sequence"
        # sql2 = "SELECT * FROM allcase_set_io_outparam WHERE SET_NAME = (SELECT TABLE_NAME FROM `allcase` WHERE `NAME` " \
        #        "= %s) AND TYPE = 3 ORDER BY name"
        sql2 = "SELECT * FROM allcase_set_io_outparam WHERE SET_NAME = %s AND TYPE = 3 ORDER BY name"
        dic_value_pass = {}

        try:
            cursor.execute(sql2, [self.case_name])
            results = cursor.fetchall()
            for row in results:
                # 存放值传递数据,值由value传向key
                dic_value_pass[row[3]] = row[2]
            # json_str = json.dumps(dic_value_pass, ensure_ascii=False, encoding='utf-8', indent=4)
            # 打印结果
            # print json_str
        except IOError:
            print("Error: unable to write data")

        try:
            # 执行SQL语句
            cursor.execute(sql, [self.case_name])
            # 获取所有记录列表
            results = cursor.fetchall()
            # 新建有序dic，其key为组件名，value为出入参键值对
            dic = OrderedDict()
            for row in results:
                # 新建dictTemp用于存放出入参键值对,其key为字段名，value为字段对应的值（value为list结构，第一位为值传递信息，若其为0，则value取该list第二位中的值，否则，取值传递信息中的对应值）
                dict_temp = {}
                name = row[2]
                description = row[5]
                value = row[4]
                for index in range(len(description.split("\0"))):
                    # 新建listTemp用于存放出入参值
                    str_temp = name + "." + description.split("\0")[index]
                    if str_temp in dic_value_pass.keys():
                        list_temp = [dic_value_pass[name + "." + description.split("\0")[index]],
                                     value.split("\0")[index].lstrip('[').rstrip(']')]
                    else:
                        list_temp = ["0", value.split("\0")[index].lstrip('[').rstrip(']')]
                    dict_temp[description.split("\0")[index]] = list_temp
                # 写入json
                dic[name] = dict_temp
            dict_case[self.case_name] = dic
            json_str = json.dumps(dict_case, ensure_ascii=False)
            print(json_str)
            return json_str
            # 打印结果
            # with codecs.open(self.json_local, 'a+', 'utf-8') as json_file:
            #     json_file.writelines(json_str)
            #     json_file.write('\n')
            #     json_file.close()
        except IOError:
            print("Error: unable to write data")

        # 关闭数据库连接
        db.close()
