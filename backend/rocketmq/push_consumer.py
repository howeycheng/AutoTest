from rocketmq.client import PushConsumer, ConsumeStatus
import time
import os

from backend.log.log import Log


def callback(msg):
    print('msg.id: ',msg.id, 'msg.keys',msg.keys, 'msg.tags',str(msg.tags, 'utf8'))
    Log.init_log_data(str(msg.body, 'utf8'), str(msg.keys, 'utf8'), str(msg.tags, 'utf8'))
    return ConsumeStatus.CONSUME_SUCCESS


def start_consume_message():
    print("日志处理子进程 子进程PID：", os.getpid(), "对应主进程PID", os.getppid())
    consumer = PushConsumer('log_customer')
    consumer.set_name_server_address('10.1.160.162:9876')
    consumer.subscribe('LOG', callback)
    print('start consume message')
    consumer.start()

    while True:
        time.sleep(3600)
