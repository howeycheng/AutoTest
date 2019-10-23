from rocketmq.client import Producer, Message

producer = Producer('PID-XXX')
producer.set_namesrv_domain('http://onsaddr-internet.aliyun.com/rocketmq/nsaddr4client-internet')
# For ip and port name server address, use `set_namesrv_addr` method, for example:
producer.set_namesrv_addr('10.1.160.162:9876')
# producer.set_session_credentials('XXX', 'XXXX', 'ALIYUN') # No need to call this function if you don't use Aliyun.
producer.start()

msg = Message('YOUR-TOPIC')
msg.set_keys('XXX')
msg.set_tags('XXX')
msg.set_body('XXXX')
ret = producer.send_sync(msg)
print(ret.status, ret.msg_id, ret.offset)
producer.shutdown()