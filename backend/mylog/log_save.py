"""
@Author 程 浩
@Date 2020/10/15 10:53
@Version 1.0
"""
import datetime
import json

from backend.models import *


def save_run_recode(run_name, set_id, nums):
    # 获取当前run表中run_id最大记录数
    run_id_last_set = Run.objects.values('run_id').order_by('-run_id')
    if len(run_id_last_set) == 0:
        run_id_last = '001'
    else:
        run_id_last = run_id_last_set[0]['run_id'].split('_')[1]
    run_id_new = 'RUN_' + str(int(run_id_last) + 1).rjust(3, '0')
    project_id = 0
    runner = '123'
    start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    finish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    runner_result = 0
    run = Run(project_id=project_id, run_id=run_id_new, run_name=run_name, runner=runner, set_id=set_id,
              start=start,
              finish=finish, runner_result=runner_result, finish_nums=0, nums=nums)
    run.save()
    return run_id_new


def save_log_detail(log, case_id, run_id, runner_result):
    case_name = Cases.objects.filter(case_id=case_id).values('name')[0]['name']
    run_set = RunSet(project_id='0', case_name=case_name, case_clazz=case_name, case_type=0, case_id=case_id,
                     order_id=1,
                     case_state=2, set_id='', run_id=run_id, runner_result=runner_result)
    run_set.save()
    json_log = json.loads(log)
    # comp为组件
    order_id = 0
    for comp in json_log:
        order_id += 1
        name = comp + "#" + json_log[comp]['component_script_model'][1]
        value = ""
        description = ""
        runner_result = json_log[comp]['runner_result'][1]
        for key in json_log[comp]:
            if description == "":
                description = '[' + key + ']'
                value = '[' + json_log[comp][key][1] + ']'
            else:
                description = description + '\0' + '[' + key + ']'
                value = value + '\0' + '[' + json_log[comp][key][1] + ']'
        run_set_io = RunSetIo(project_id='0', component_name=name, value=value, description=description,
                              runner_result=runner_result,
                              case_id=case_id, run_id=run_id, order_id=order_id)
        run_set_io.save()
    # finish_nums_now = int(Run.objects.filter(run_id=run_id).values('finish_nums')[0]['finish_nums']) + 1
    finish_nums_now = RunSet.objects.filter(run_id=run_id).values('case_id').count()
    Run.objects.filter(run_id=run_id).update(finish_nums=finish_nums_now)
