# Create your views here.
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.utils import http
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *

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
        cases = Requirement.objects.filter(parent_id=0).values('rqid', 'name', 'parent_id')
    elif rqid is not None:  # 查询点击节点子需求
        cases = Requirement.objects.filter(parent_id=rqid).values('rqid', 'name', 'parent_id')
    return Response(cases)


@api_view(['GET', 'POST'])
def get_scene(request):
    """
    获取需求下场景
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 需求ID
    scene = TcReqScene.objects.filter(fk_req_id=rqid).values('pk_id', 'scene_name')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_scene_detail(request):
    """
    获取场景组件
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 需求id
    scene = TcSceneSet.objects.filter(fk_scene_id=rqid).values('case_name', 'fk_com_id').order_by('wl_action')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_cases(request):
    """
    获取场景下用例名称
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')
    scene = Allcase.objects.filter(fk_scene_id=rqid).values('name', 'table_name')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_cases_io(request):
    """
    获取用例IO
    :param request:
    :return:
    """
    case_name = request.GET.get('case_name')  #
    scenes = AllcaseSetIo.objects.filter(set_name=case_name).values('description', 'value').order_by('sequence')
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
    component_id = Component.objects.filter(scriptname=component).values('pk_id')
    component_col = TcConstraintsRule.objects.filter(fk_com_id=component_id[0]['pk_id']).values('target_field',
                                                                                                'description',
                                                                                                'paramvalue').order_by(
        'pk_id')
    return Response(component_col)


@api_view(['GET', 'POST'])
def get_scene_params(request):
    """
    获取场景组件栏位值，默认值等信息
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 场景id
    component_ids = TcSceneSet.objects.filter(fk_scene_id=rqid).values('fk_com_id', 'case_name').order_by('wl_action')
    components_params = []
    for component_id in component_ids:
        component_col = TcConstraintsRule.objects.filter(fk_com_id=component_id['fk_com_id']).values('target_field',
                                                                                                     'description',
                                                                                                     'paramvalue').order_by(
            'pk_id')
        components_params.append({component_id['case_name']: component_col})
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
    cases_list = Allcase.objects.filter(fk_scene_id=rqid).values('table_name', 'name').order_by('name')[
                 (current_page - 1) * page_size:current_page * page_size]
    cases_io = []
    for case in cases_list:
        case_id = case.get('table_name')
        case_name = case.get('name')
        case_io_all = AllcaseSetIo.objects.filter(set_name=case_id).values('name', 'description', 'value',
                                                                           'sequence').order_by('sequence')
        case_io_one = {'name': case_name}
        for set_io in case_io_all:
            name = set_io['description'].split("\0")
            io_value = set_io['value'].split("\0")
            sequence = set_io['sequence']
            set_io_dict = dict(zip(name, io_value))
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
    set_io = TcSceneSetIo.objects.filter(fk_scene_id=rqid, type=type).values('name', 'assign').order_by(
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
        s = Allset.objects.filter(level=0).values('pk_id', 'group_name').order_by(
            'pk_id')
        # 统一输出格式
        for index in range(len(s)):
            s[index]['name'] = s[index]['group_name']
    else:
        pk_id = request.GET.get('pk_id')  # 测试集ID
        s = Allset.objects.filter(parent_id=pk_id).values('pk_id', 'name', 'table_name').order_by(
            'pk_id')
    return Response(s)


@api_view(['GET', 'POST'])
def get_cases_in_set(request):
    """
    获取测试集下用例
    :param request:
    :return:
    """
    set = request.GET.get('set')
    cases = AllsetSet.objects.filter(set_name=set).values('case_name', 'case_clazz', 'table_name')
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
    req_id = request.GET.get('reqId')
    if level == "0":
        SET_TEMP = []
        with connection.cursor() as cursor:
            cursor.execute(
                "select distinct allcase.tier from allcase join allset_set on allcase.TABLE_NAME = allset_set.TABLE_NAME where allset_set.SET_NAME = %s",
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
        req = Allcase.objects.filter(tier__in=row_list).values("pk_id", "name", "table_name", "tier")
        return Response(req)
    else:
        set_row = []
        for s in SET_TEMP:
            if s[:-3] == req_id:
                set_row.append(s)
        req = Allcase.objects.filter(tier__in=set_row).values("pk_id", "name", "table_name", "tier")
        return Response(req)


@api_view(['GET', 'POST'])
def get_case_of_test_set(request):
    s = request.GET.get('set')  # 测试集
    tier = request.GET.get('tier') + "000"
    with connection.cursor() as cursor:
        cursor.execute(
            "select allcase.TABLE_NAME,allset_set.CASE_NAME,allset_set.CASE_CLAZZ from allcase join allset_set on allcase.TABLE_NAME = allset_set.TABLE_NAME where allset_set.SET_NAME = %s and allcase.tier = %s",
            [s, tier])
        row = cursor.fetchall()
    return Response(row)
