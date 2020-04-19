import time

from rocketmq.client import PushConsumer


def callback(msg):
    print(msg.id, msg.body)


consumer = PushConsumer('CID_XXX')
consumer.set_namesrv_domain('http://onsaddr-internet.aliyun.com/rocketmq/nsaddr4client-internet')
# For ip and port name server address, use `set_namesrv_addr` method, for example:
# consumer.set_namesrv_addr('127.0.0.1:9887')
consumer.set_session_credentials('XXX', 'XXXX', 'ALIYUN') # No need to call this function if you don't use Aliyun.
consumer.subscribe('YOUR-TOPIC', callback)
consumer.start()

# while True:
#     time.sleep(3600)

# consumer.shutdown()