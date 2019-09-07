# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *


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
    print(component_ids)
    for component_id in component_ids:
        component_col = TcConstraintsRule.objects.filter(fk_com_id=component_id['fk_com_id']).values('target_field',
                                                                                                     'description',
                                                                                                     'paramvalue').order_by(
            'pk_id')
        components_params.append({component_id['case_name']: component_col})
    return Response(components_params)
