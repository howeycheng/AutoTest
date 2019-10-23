from rocketmq.client import PullConsumer


consumer = PullConsumer('CID_XXX')
consumer.set_namesrv_domain('http://onsaddr-internet.aliyun.com/rocketmq/nsaddr4client-internet')
# For ip and port name server address, use `set_namesrv_addr` method, for example:
# consumer.set_namesrv_addr('127.0.0.1:9887')
consumer.set_session_credentials('XXX', 'XXXX', 'ALIYUN') # No need to call this function if you don't use Aliyun.
consumer.start()

for msg in consumer.pull('YOUR-TOPIC'):
    print(msg.id, msg.body)

consumer.shutdown()