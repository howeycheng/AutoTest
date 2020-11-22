# Create your views here.
import logging

from django.db import connection
from dynamic_db_router import DynamicDbRouter, in_database
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .mylog.log_save import save_run_recode

import os

from django.conf import settings

# 新建子进程用于获取mq接收的日志
from .mysend.my_producer import MyProducer

# logger = logging.getLogger('django')

print("当前进程PID ", os.getpid(), "对应父进程PID", os.getppid())
# p = Process(target=start_consume_log)
# p.start()

set_temp = []
# 创建用例数据发送客户端
namesrv_addr = settings.ROCKET_MQ.get('nameSrv')
group_id = settings.ROCKET_MQ.get('casesProducerName')
my_producer = MyProducer(namesrv_addr, group_id)
my_producer.start()

external_db = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'cases_manager',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': '10.1.160.162',
    'PORT': '3306'
}


@api_view(['GET', 'POST'])
def get_req(request):
    """
    获取需求
    :param request:
    :return:
    """
    print('_external_db', getattr(request, '_external_db', ''))
    with in_database(getattr(request, '_external_db', '')):
        cases = None
        rqid = request.GET.get('rqid')  # 需求id
        if rqid is None:  # 查询需求根节点
            cases = Requirement.objects.filter(parent_id=0).values('id', 'name', 'parent_id')
        elif rqid is not None:  # 查询点击节点子需求
            cases = Requirement.objects.filter(parent_id=rqid).values('id', 'name', 'parent_id')
        if cases:
            return Response(cases)
        else:
            return Response("")


@api_view(['GET', 'POST'])
def get_scene(request):
    """
    获取需求下场景
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 需求ID
    scene = ReqScene.objects.filter(req_id=rqid).values('id', 'scene_name')
    if scene:
        return Response(scene)


@api_view(['GET', 'POST'])
def get_scene_detail(request):
    """
    获取场景组件
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 需求id
    scene = SceneSet.objects.filter(scene_id=rqid).values('component_name', 'com_id').order_by('order_id')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_cases(request):
    """
    获取场景下用例名称
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')
    scene = Cases.objects.filter(scene_id=rqid).values('name', 'case_id')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_cases_io(request):
    """
    获取用例IO
    :param request:
    :return:
    """
    case_name = request.GET.get('case_name')  #
    scenes = SceneSetIo.objects.filter(name=case_name).values('description', 'value').order_by('sequence')
    case_io = []
    for scene in scenes:
        name = scene['description'].split("\0")
        value = scene['value'].split("\0")
        case_io.append(dict(zip(name, value)))
    return Response(case_io)


@api_view(['GET', 'POST'])
def get_component_col(request):
    """
    获取组件栏位值
    :param request:
    :return:
    """
    component = request.GET.get('component')  #
    component_id = Components.objects.filter(script_name=component).values('id')
    component_col = ParameterRules.objects.filter(fk_com_id=component_id[0]['id']).values('target_field',
                                                                                          'description',
                                                                                          'parameter_value').order_by(
        'id')
    return Response(component_col)


@api_view(['GET', 'POST'])
def get_scene_params(request):
    """
    获取场景组件栏位值，默认值等信息
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 场景id
    component_ids = SceneSet.objects.filter(scene_id=rqid).values('com_id', 'component_name').order_by('order_id')
    components_params = []
    for component_id in component_ids:
        component_col = ParameterRules.objects.filter(fk_com_id=component_id['com_id']).values('target_field',
                                                                                               'description',
                                                                                               'parameter_value').order_by(
            'id')
        components_params.append({component_id['component_name']: component_col})
    return Response(components_params)


@api_view(['GET', 'POST'])
def get_scene_cases_io(request):
    """
    获取场景组件栏位值，默认值等信息
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 场景ID
    current_page = int(request.GET.get('currentPage'))  # 当前页数
    page_size = int(request.GET.get('pageSize'))  # 每页数据数
    cases_list = Cases.objects.filter(scene_id=rqid).values('case_id', 'name').order_by('name')[
                 (current_page - 1) * page_size:current_page * page_size]
    cases_io = []
    for case in cases_list:
        case_id = case.get('case_id')
        case_name = case.get('name')
        case_io_all = CaseSetIo.objects.filter(case_id=case_id).values('name', 'description', 'value',
                                                                       'sequence').order_by('sequence')
        case_io_one = {'name': case_name}
        for set_io in case_io_all:
            description = set_io['description'].split("\0")
            io_value = set_io['value'].split("\0")
            sequence = set_io['sequence']
            set_io_dict = dict(zip(description, io_value))
            for key, value in set_io_dict.items():  # 暂时将各个组件IO放在一个字典中，用sequence标识区分
                case_io_one["sequence_" + str(sequence) + "_" + key] = value.lstrip('[').rstrip(']')
        cases_io.append(case_io_one)
    return Response(cases_io)


@api_view(['GET', 'POST'])
def get_scene_set_io(request):
    """
    获取场景下值传递、校验点等信息
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 场景id
    data_type = request.GET.get('type')  # 数据类型
    set_io = SceneSetIo.objects.filter(scene_id=rqid, type=data_type).values('name', 'assign').order_by(
        'sequence')
    return Response(set_io)


@api_view(['GET', 'POST'])
def get_set(request):
    """
    获取测试集
    :param request:
    :return:
    """
    level = request.GET.get('level')  # 级别
    if level == '0':
        s = Sets.objects.filter(level=0).values('id', 'group_name').order_by(
            'id')
        for index in range(len(s)):
            s[index]['name'] = s[index]['group_name']
    else:
        set_id = request.GET.get('id')  # 测试集ID
        s = Sets.objects.filter(parent_id=set_id).values('id', 'set_name', 'set_id').order_by(
            'id')
        # 统一输出格式
        for index in range(len(s)):
            s[index]['name'] = s[index]['set_name']
    return Response(s)


@api_view(['GET', 'POST'])
def get_cases_in_set(request):
    """
    获取测试集下用例
    :param request:
    :return:
    """
    test_set = request.GET.get('set')
    cases = CasesInSet.objects.filter(set_id=test_set).values('name', 'case_id').order_by('order_id')
    return Response(cases)


@api_view(['GET', 'POST'])
def get_req_of_case(request):
    """
    获取用例所在场景，第一级
    :param request:
    :return:
    """
    global set_temp
    level = request.GET.get('level')  # 级别
    set_id = request.GET.get('set')
    tier = request.GET.get('tier')
    if level == "0":
        set_temp = []
        with connection.cursor() as cursor:
            cursor.execute(
                "select distinct cases.tier from cases join cases_in_set on cases.case_id = cases_in_set.case_id where cases_in_set.set_id = %s",
                [set_id])
            row = cursor.fetchall()
        row_list = []
        for r in row:
            if r[0][0:3] not in row_list:
                row_list.append(r[0][0:3])
        for r in row:
            i = 0
            length = len(r[0])
            while i + 3 < length:
                if r[0][0:i + 3] not in set_temp:
                    set_temp.append(r[0][0:i + 3])
                i = i + 3
        req = Cases.objects.filter(tier__in=row_list).values("id", "name", "case_id", "tier")
        return Response(req)
    else:
        set_row = []
        for s in set_temp:
            if s[:-3] == tier:
                set_row.append(s)
        req = Cases.objects.filter(tier__in=set_row).values("id", "name", "case_id", "tier")
        if len(req) == 0 and tier[-3:] != "000":
            tier = tier + "000"
            with connection.cursor() as cursor:
                cursor.execute(
                    "select cases.id,cases_in_set.name,cases.case_id,cases.tier from cases join cases_in_set on cases.case_id = cases_in_set.case_id where cases_in_set.set_id = %s and cases.tier = %s",
                    [set_id, tier])
                row = cursor.fetchall()
            req_temp = []
            for r in row:
                req_temp.append(dict(zip(['id', 'name', 'case_id', 'tier'], list(r))))
            req = req_temp
        return Response(req)


@api_view(['GET', 'POST'])
def run(request):
    # 保存执行记录到run表
    set_names = request.POST.get('setNames').split(',')
    run_name = request.POST.get('runName')
    set_id = request.POST.get('setId')
    # 保存一条执行记录到run表，并返回该记录的run_id
    run_id_new = save_run_recode(run_name, set_id, len(set_names))
    ret = my_producer.producing(set_names, 'CASES', run_id_new)
    print(str(ret))
    return Response(str(ret))


@api_view(['GET', 'POST'])
def get_cases_to_run(request):
    # 用例或场景id
    checked_cases = request.GET.get('checkedCases').split(',')
    # 测试集id
    set_id = request.GET.get('set')
    cases = []
    tier_all = []
    # 遍历id,若已是用例id,直接将其加入cases列表,若是场景id,则循环递归出该场景下所有用例id并加入cases列表
    for node in checked_cases:
        node_list = node.split(' ')
        # id = node_list[0]
        case_id = node_list[1]
        tier = node_list[2]
        if case_id == 'null':
            with connection.cursor() as cursor:
                cursor.execute(
                    "select concat(tier,'000') from set_req where set_id = %s and left(tier,%s) = %s",
                    [set_id, len(tier), tier])
                row = cursor.fetchall()
            for r in row:
                tier_all.append(r[0])
        else:
            cases.append(case_id)
    tier_all = list(set(tier_all))
    print(tier_all)
    if len(tier_all) != 0:
        with connection.cursor() as cursor:
            cursor.execute(
                "select cases_in_set.case_id from cases_in_set join cases on cases_in_set.case_id =  cases.case_id where set_id = %s and cases.tier in %s",
                [set_id, tier_all])
            row = cursor.fetchall()
            for r in row:
                cases.append(r[0])
    cases = list(set(cases))
    print(cases)
    return Response(cases)


# 获取所有执行记录
@api_view(['GET', 'POST'])
def get_run(request):
    run_log = Run.objects.values('run_name', 'start', 'finish', 'run_id', 'runner_result', 'finish_nums', 'nums')
    return Response(run_log)


# 获取指定执行记录具体信息
@api_view(['GET', 'POST'])
def get_run_set(request):
    run_id = request.GET.get('run_id')
    run_set = RunSet.objects.filter(run_id=run_id, case_type='0').values('case_clazz', 'case_id',
                                                                         'case_state', 'run_id',
                                                                         'runner_result').order_by(
        'order_id')
    return Response(run_set)


# 获取指定执行记录指定用例的组件执行情况
@api_view(['GET', 'POST'])
def get_run_set_one(request):
    run_id = request.GET.get('run_id')
    case_id = request.GET.get('case_id')
    run_set = RunSetIo.objects.filter(run_id=run_id, case_id=case_id).values('component_name', 'value', 'description',
                                                                             'runner_result').order_by('order_id')
    return Response(run_set)


@api_view(['GET', 'POST'])
def test(request):
    print(external_db)
    with in_database(external_db, True, True):
        input2 = Requirement.objects.filter(parent_id=0).values('id', 'name', 'parent_id')
        if input2:
            return Response(input2)


@api_view(['DELETE'])
def delete_run(request):
    run_id = request.data['id']
    Run.objects.filter(run_id=run_id).delete()
    RunSet.objects.filter(run_id=run_id).delete()
    RunSetIo.objects.filter(run_id=run_id).delete()
    return Response({'status': '204'})


@api_view(['GET'])
def get_run_progress(request):
    run_id = request.GET.get('run_id')
    finish_nums_now = Run.objects.filter(run_id=run_id).values('finish_nums')[0]
    return Response(finish_nums_now)
