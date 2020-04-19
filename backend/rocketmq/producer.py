import time

from rocketmq.client import Producer, Message

from backend.rocketmq.get_case import GetCase

producer = Producer('PID-XXX')
# producer.set_namesrv_domain('http://onsaddr-internet.aliyun.com/rocketmq/nsaddr4client-internet')
producer.set_namesrv_addr('127.0.0.1:9876')
producer.start()
msg = Message('CASE')
a = GetCase("127.0.0.1", 3306, "root", "root", "testcenter_24", "担保品买入-单笔委托最低数量,并待报撤单-深-[主板]000001")
case_data = a.get_case_data()
msg.set_keys('担保品买入-单笔委托最低数量,并待报撤单-深-[主板]000001')
msg.set_tags('b')
msg.set_body(case_data)
while True:
    time.sleep(2)
    ret = producer.send_sync(msg)
    print(ret.status, ret.msg_id, ret.offset)
producer.shutdown()