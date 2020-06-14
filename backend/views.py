# Create your views here.

from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
# from .rocketmq.producer import MyProducer

SET_TEMP = []


@api_view(['GET', 'POST'])
def get_req(request):
    """
    获取需求
    :param request:
    :return:
    """
    req = []
    rqid = request.GET.get('rqid')  # 需求id
    if rqid is None:  # 查询需求根节点
        cases = Requirement.objects.filter(parent_id=0).values('id', 'name', 'parent_id')
    elif rqid is not None:  # 查询点击节点子需求
        cases = Requirement.objects.filter(parent_id=rqid).values('id', 'name', 'parent_id')
    return Response(cases)


@api_view(['GET', 'POST'])
def get_scene(request):
    """
    获取需求下场景
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 需求ID
    scene = ReqScene.objects.filter(req_id=rqid).values('id', 'scene_name')
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
    type = request.GET.get('type')  # 数据类型
    set_io = SceneSetIo.objects.filter(scene_id=rqid, type=type).values('name', 'assign').order_by(
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
        id = request.GET.get('id')  # 测试集ID
        s = Sets.objects.filter(parent_id=id).values('id', 'set_name', 'set_id').order_by(
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
    set = request.GET.get('set')
    cases = CasesInSet.objects.filter(set_name=set).values('case_name', 'case_clazz', 'table_name')
    return Response(cases)


@api_view(['GET', 'POST'])
def get_req_of_case(request):
    """
    获取用例所在场景，第一级
    :param request:
    :return:
    """
    global SET_TEMP
    level = request.GET.get('level')  # 级别
    set_id = request.GET.get('set')
    tier = request.GET.get('tier')
    if level == "0":
        SET_TEMP = []
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
                if r[0][0:i + 3] not in SET_TEMP:
                    SET_TEMP.append(r[0][0:i + 3])
                i = i + 3
        req = Cases.objects.filter(tier__in=row_list).values("id", "name", "case_id", "tier")
        return Response(req)
    else:
        set_row = []
        for s in SET_TEMP:
            if s[:-3] == tier:
                set_row.append(s)
        req = Cases.objects.filter(tier__in=set_row).values("id", "name", "case_id", "tier")
        if len(req) == 0 and tier[-3:] is not "000":
            tier = tier + "000"
            with connection.cursor() as cursor:
                cursor.execute(
                    "select cases.case_id,cases_in_set.name,cases.tier from cases join cases_in_set on cases.case_id = cases_in_set.case_id where cases_in_set.set_id = %s and cases.tier = %s",
                    [set_id, tier])
                row = cursor.fetchall()
            req_temp = []
            for r in row:
                req_temp.append(dict(zip(['id', 'name', 'tier'], list(r))))
            req = req_temp
        return Response(req)


@api_view(['GET', 'POST'])
def run(request):
    namesrv_addr = request.GET.get('nameSrvAddr')
    topic = request.GET.get('topic')
    set_names = request.GET.get('setNames')
    my_producer = MyProducer(namesrv_addr, topic)
    my_producer.start()
    ret = my_producer.producing(set_names.split(','))
    my_producer.shutdown()
    return Response(ret)
