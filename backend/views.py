import json

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Requirement
from .models import Scene

from django.views.decorators.csrf import csrf_exempt


def testapi(request, *args, **kargs):
    cases = Requirement.objects.values_list('rqid', 'name', 'parent_id')
    cases_parent = {}
    if len(args) is 0 and len(kargs) is 0:
        for case in cases:
            if case[2] is 0:
                cases_parent[case[0]] = case[1]
    elif len(args) is not 0 and len(kargs) is 0:
        pass
    elif len(args) is 0 and len(kargs) is not 0:
        pass
    else:
        pass
    return JsonResponse(cases_parent, json_dumps_params={'ensure_ascii': False})
