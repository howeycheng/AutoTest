"""
@Author 程 浩
@Date 2020/10/15 10:53
@Version 1.0
"""

import json
from backend.models import *


class Log:

    def init_log_data(self, log, case_id, run_id):
        json_log = json.loads(log)
        # comp为组件
        order_id = 0
        for comp in json_log:
            order_id += 1
            name = comp + "#" + json_log[comp]['component_script_model'][1]
            print(name)
            value = ""
            description = ""
            for key in json_log[comp]:
                if key is not 'component_script_model':
                    if description is "":
                        description = '[' + key + ']'
                        value = '[' + json_log[comp][key][1] + ']'
                    else:
                        description = description + '\0' + '[' + key + ']'
                        value = value + '\0' + '[' + json_log[comp][key][1] + ']'
            print(value)
            print(description)
            run_set_io = RunSetIo(project_id='0', component_name=name, value=value, description=description, status='0',
                                  case_id=case_id, run_id=run_id, order_id=order_id)
            run_set_io.save()
