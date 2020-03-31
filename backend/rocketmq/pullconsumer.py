from rocketmq.client import PullConsumer


consumer = PullConsumer('CID_XXX')
consumer.set_namesrv_domain('http://onsaddr-internet.aliyun.com/rocketmq/nsaddr4client-internet')
# For ip and port name server address, use `set_namesrv_addr` method, for example:
consumer.set_namesrv_addr('122.51.44.31:9887')
consumer.start()

for msg in consumer.pull('YOUR-TOPIC'):
    print(msg.id, msg.body)

consumer.shutdown()