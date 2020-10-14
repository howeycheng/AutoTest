from rocketmq.client import PushConsumer, ConsumeStatus
import time
import os


def callback(msg):
    print(msg.id, str(msg.get_property('用例ID'), 'utf8'), str(msg.tags, 'utf8'))
    output = str(msg.body, 'utf8')
    print(output)
    return ConsumeStatus.CONSUME_SUCCESS


def start_consume_message():
    print("日志处理子进程 子进程PID：", os.getpid(), "对应主进程PID", os.getppid())
    consumer = PushConsumer('consumer_group')
    consumer.set_name_server_address('10.1.160.162:9876')
    consumer.subscribe('LOG', callback)
    print('start consume message')
    consumer.start()

    while True:
        time.sleep(3600)
