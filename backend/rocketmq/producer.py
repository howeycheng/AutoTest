import json
from collections import OrderedDict

from rocketmq.client import Producer, Message

from backend.models import CaseSetIoOutparam, CaseSetIo


def get_case_io(set_name):
    """
    获取指定用例入参
    :param set_name:
    :return:
    """
    dict_case = {}
    dic_value_pass = {}
    a = CaseSetIoOutparam.objects.filter(case_id=set_name, type=3).order_by('name').values('name', 'assign')
    for i in a:
        # print(i)
        dic_value_pass[i['assign']] = i['name']
    b = CaseSetIo.objects.filter(case_id=set_name).order_by('sequence').values('component', 'value', 'description')
    dic = OrderedDict()
    for j in b:
        # print(j)
        dict_temp = {}
        name = j['component']
        description = j['description']
        value = j['value']
        for index in range(len(description.split("\0"))):
            # 新建listTemp用于存放出入参值
            str_temp = name + "." + description.split("\0")[index]
            if str_temp in dic_value_pass.keys():
                list_temp = [dic_value_pass[name + "." + description.split("\0")[index]],
                             value.split("\0")[index].lstrip('[').rstrip(']')]
            else:
                list_temp = ["0", value.split("\0")[index].lstrip('[').rstrip(']')]
            dict_temp[description.split("\0")[index]] = list_temp
        # 写入json
        dic[name] = dict_temp
    dict_case[set_name] = dic
    json_str = json.dumps(dict_case, ensure_ascii=False)
    print(json_str)
    return json_str


class MyProducer:
    def __init__(self, namesrv_addr, topic):
        self.namesrv_addr = namesrv_addr
        self.topic = topic
        self.producer = Producer(self.topic)

    def start(self):
        self.producer.set_namesrv_addr(self.namesrv_addr)
        self.producer.start()

    def producing(self, set_names):
        r = []
        for set_name in set_names:
            case_io = get_case_io(set_name)
            message = Message(self.topic)
            message.set_keys(set_name)
            message.set_tags('')
            message.set_body(case_io)
            try:
                res = self.producer.send_sync(message)
                r.append({"status": res.status, "msg_id": res.msg_id, "offset": res.offset})
            except:
                return "rocketmq.exceptions.ProducerSendSyncFailed"
        return r

    def shutdown(self):
        self.producer.shutdown()
