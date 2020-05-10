import time

from rocketmq.client import Producer, Message

from AutoTest.settings import DATABASES
from backend.rocketmq.get_case import GetCase

producer = Producer('PID-XXX')
# producer.set_namesrv_domain('http://onsaddr-internet.aliyun.com/rocketmq/nsaddr4client-internet')
producer.set_namesrv_addr('127.0.0.1:9876')
producer.start()
msg = Message('CASE2')
a = GetCase("127.0.0.1", 3306, "root", "root", "testcenter_24", "Set518")
case_data = a.get_case_data()
msg.set_keys('担保品买入-单笔委托最低数量,并待报撤单-深-[主板]000001')
msg.set_tags('b')
msg.set_body(case_data)
ret = producer.send_sync(msg)
print(ret)
print(ret.status, ret.msg_id, ret.offset)
producer.shutdown()


class MyProducer:
    def __init__(self, namesrv_addr, topic, case):
        self.namesrv_addr = namesrv_addr
        self.topic = topic
        self.case = case
        self.producer = Producer(self.topic)

    def start(self):
        self.producer.set_namesrv_addr(self.namesrv_addr)
        self.producer.start()

    def producing(self):
        database = DATABASES.get('default').get('NAME')
        user = DATABASES.get('default').get('USER')
        password = DATABASES.get('default').get('PASSWORD')
        ip = DATABASES.get('default').get('HOST')
        port = DATABASES.get('default').get('PORT')
        # getter = GetCase(ip, 3306, user, password, database, self.msg)
        r = []
        for c in self.case:
            getter = GetCase(ip, port, user, password, database, c)
            case = getter.get_case_data()
            message = Message(self.topic)
            message.set_keys(self.case)
            message.set_tags('')
            message.set_body(case)
            res = self.producer.send_sync(message)
            r.append({"status": res.status, "msg_id": res.msg_id, "offset": res.offset})
        return r

    def shutdown(self):
        self.producer.shutdown()
