import json

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Requirement
from .models import Scene

from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
def get_req(request):
    rqid = request.GET.get('rqid')  # 需求id
    if rqid is None:  # 查询需求根节点
        cases = Requirement.objects.filter(parent_id=0).values_list('rqid', 'name', 'parent_id')
    elif rqid is not None:  # 查询点击节点子需求
        cases = Requirement.objects.filter(parent_id=rqid).values_list('rqid', 'name', 'parent_id')
    return Response(cases)
