from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Requirement
from .models import Scene


def index(request):
    cases = Requirement.objects.values_list('rqid', 'name', 'parent_id')
    cases_parent = []
    for case in cases:
        if case[2] is 0:
            cases_parent.append(case[1])
    return render(request, template_name='cases/index.html', context={'cases': cases_parent})


# def scene():
#     s = Scene.objects.root_nodes()
#     print(s)
#
#
# scene()
