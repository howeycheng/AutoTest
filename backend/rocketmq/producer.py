import time

from rocketmq.client import Producer, Message

from AutoTest.settings import DATABASES
from backend.rocketmq.get_case import GetCase


# producer = Producer('PID-XXX')
# # producer.set_namesrv_domain('http://onsaddr-internet.aliyun.com/rocketmq/nsaddr4client-internet')
# producer.set_namesrv_addr('127.0.0.1:9876')
# producer.start()
# msg = Message('CASE2')
# a = GetCase("127.0.0.1", 3306, "root", "root", "testcenter_24", "担保品买入-单笔委托最低数量,并待报撤单-深-[主板]000001")
# case_data = a.get_case_data()
# msg.set_keys('担保品买入-单笔委托最低数量,并待报撤单-深-[主板]000001')
# msg.set_tags('b')
# msg.set_body(case_data)
# while True:
#     ret = producer.send_sync(msg)
#     print(ret.status, ret.msg_id, ret.offset)
#     # time.sleep(0.5)
# producer.shutdown()


class MyProducer:
    def __init__(self, namesrv_addr, topic, msg):
        self.producer = Producer(self.topic)
        self.namesrv_addr = namesrv_addr
        self.topic = topic
        self.msg = msg

    def start(self):
        self.producer.set_namesrv_addr(self.namesrv_addr)
        self.producer.start()

    def producing(self):
        msg = Message(self.topic)
        database = DATABASES.get('NAME')
        user = DATABASES.get('USER')
        password = DATABASES.get('PASSWORD')
        ip = DATABASES.get('HOST')
        getter = GetCase(ip, 3306, user, password, database, self.msg)
        case_data = getter.get_case_data()
        msg.set_keys(self.msg)
        msg.set_tags('')
        msg.set_body(case_data)
        self.producer.send_async(msg)

    def shutdown(self):
        self.producer.shutdown()
