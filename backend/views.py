# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Requirement, TcSceneSet, Allcase
from .models import TcReqScene


@api_view(['GET', 'POST'])
def get_req(request):
    req = []
    rqid = request.GET.get('rqid')  # 需求id
    if rqid is None:  # 查询需求根节点
        cases = Requirement.objects.filter(parent_id=0).values('rqid', 'name', 'parent_id')
    elif rqid is not None:  # 查询点击节点子需求
        cases = Requirement.objects.filter(parent_id=rqid).values('rqid', 'name', 'parent_id')
    return Response(cases)


@api_view(['GET', 'POST'])
def get_scene(request):
    rqid = request.GET.get('rqid')  # 需求id
    scene = TcReqScene.objects.filter(fk_req_id=rqid).values('pk_id', 'scene_name')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_scene_detail(request):
    rqid = request.GET.get('rqid')  # 需求id
    scene = TcSceneSet.objects.filter(fk_scene_id=rqid).values('case_name').order_by('wl_action')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_cases(request):
    rqid = request.GET.get('rqid')  # 需求id
    scene = Allcase.objects.filter(fk_scene_id=rqid).values('name','table_name')
    return Response(scene)
