import json
from collections import OrderedDict

from rocketmq.client import Producer, Message

from backend.models import CaseSetIoOutparam, CaseSetIo, CasesComponents

import time


def get_case_io(set_name):
    """
    获取指定用例入参
    :param set_name:
    :return:
    """
    dict_case = {}
    dic_value_pass = {}
    dic_comp_models = {}
    # 获取值传递信息
    a = CaseSetIoOutparam.objects.filter(case_id=set_name, type=3).order_by('name').values('name', 'assign')
    for i in a:
        # print(i)
        dic_value_pass[i['assign']] = i['name']
    #     获取入参
    b = CaseSetIo.objects.filter(case_id=set_name).order_by('sequence').values('name', 'value', 'description')
    dic = OrderedDict()
    c = CasesComponents.objects.filter(case_id=set_name).order_by('order_id').values('component_name',
                                                                                     'component_clazz')
    for i in c:
        # print(i)
        dic_comp_models[i['component_name']] = i['component_clazz']
    for j in b:
        # print(j)
        dict_temp = {}
        name = j['name']
        dict_temp['component_script_model'] = ['0', dic_comp_models[name]]
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
    # producer_num = 0

    def __init__(self, namesrv_addr, group_id):
        # 通过计数器解决producer重复创建的问题
        # MyProducer.producer_num = MyProducer.producer_num + 1
        self.namesrv_addr = namesrv_addr
        self.group_id = group_id
        self.producer = Producer(self.group_id)

    def start(self):
        self.producer.set_name_server_address(self.namesrv_addr)
        self.producer.start()

    def producing(self, set_names,topic):
        r = []
        for set_name in set_names:
            start_time = time.clock()
            case_io = get_case_io(set_name)
            end_time = time.clock()
            print('Running time: %s Seconds' % (end_time - start_time))
            message = Message(topic)
            message.set_keys(set_name)
            message.set_tags(topic)
            message.set_body(case_io)
            try:
                res = self.producer.send_sync(message)
                r.append({"status": res.status, "msg_id": res.msg_id, "offset": res.offset})
            except Exception as e:
                return e
        return r

    def shutdown(self):
        self.producer.shutdown()
