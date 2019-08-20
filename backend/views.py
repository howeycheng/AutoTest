import json

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Requirement
from .models import Scene

from django.views.decorators.csrf import csrf_exempt


def testapi(request):
    cases = Requirement.objects.values_list('rqid', 'name', 'parent_id')
    cases_parent = []
    for case in cases:
        if case[2] is 0:
            cases_parent.append(case[1])
    return HttpResponse(cases_parent)


# @csrf_exempt
# def testapi(request):
#     print(request)
#     print(request.method)
#     if request.method == "GET":
#         print(request.GET.get('aa'))
#         resp = {'errorcode': 100, 'type': 'Get', 'data': {'main': request.GET.get('aa')}}
#         return HttpResponse(json.dumps(resp), content_type="application/json")
#     else:
#         print(request.POST)
#         print(request.body)
#         str1 = str(request.body, encoding="utf-8")
#         data = eval(str1)
#         print(data)
#         print(data['aa'])
#         print(type(request.body))
#         resp = {'errorcode': 100, 'type': 'Post', 'data': {'main': data['aa']}}
#         return HttpResponse(json.dumps(resp), content_type="application/json")


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
