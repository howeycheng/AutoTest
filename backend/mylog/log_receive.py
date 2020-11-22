#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 15:35
# @Author  : cheng hao
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : log_receive.py
# @Software: PyCharm
import logging

from rocketmq.client import PushConsumer, ConsumeStatus
import time
import os

from AutoTest import settings
from backend.mylog.log_save import save_log_detail


def preprocessing(msg):
    """
    预处理，判断消息格式是否正确
    :param msg:
    :return:
    """
    if msg.tags == '' or msg.keys == '':
        return False
    else:
        if 'Set' not in str(msg.keys, 'utf8') or 'RUN' not in str(msg.tags, 'utf8'):
            return False
    return True


def receive_log(msg):
    """
    日志消息处理
    :param msg:
    :return:
    """
    if preprocessing(msg):
        print('msg.id: ', msg.id, 'msg.keys', msg.keys, 'msg.tags', msg.tags)
        save_log_detail(str(msg.body, 'utf8'), str(msg.keys, 'utf8'), str(msg.tags, 'utf8'),
                        str(msg.get_property('runner_result'), 'utf8'))
        return ConsumeStatus.CONSUME_SUCCESS


def start_consume_log():
    print("日志处理子进程 子进程PID：", os.getpid(), "对应主进程PID", os.getppid())
    log_consumer = PushConsumer(settings.ROCKET_MQ.get('logConsumerName'))
    log_consumer.set_name_server_address(settings.ROCKET_MQ.get('nameSrv'))
    log_consumer.subscribe('LOG', receive_log)
    print('start consume message')
    log_consumer.start()

    while True:
        time.sleep(3600)
