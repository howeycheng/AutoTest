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
    cases_parent = {}
    for case in cases:
        if case[2] is 0:
            cases_parent[case[0]] = case[1]
    return JsonResponse(cases_parent, json_dumps_params={'ensure_ascii': False})
