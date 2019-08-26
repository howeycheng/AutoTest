# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Requirement


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
    cases = Requirement.objects.filter(parent_id=rqid).values('rqid', 'name', 'parent_id')
    return Response(cases)
