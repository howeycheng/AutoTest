from django.contrib.auth import authenticate, login, logout

# Create your views here.

# 对应数据库
from django.contrib.auth.models import User
from dynamic_db_router import in_database
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Requirement
from manager.project_database import create_project_store, drop_project_store
from manager.models import *


@api_view(['POST'])
def create_user(request):
    """
    创建用户
    :param request:
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    userinfo = User.objects.filter(username=username)
    if userinfo.exists():
        return Response({'status': '400', 'error': '用户名已存在'})
    else:
        User.objects.create_user(username=username, password=password)
        return Response({'status': '201'})


@api_view(['POST'])
def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username=username)
    if user.exists():
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['project'] = 0
            return Response({'status': '200'})
        else:
            return Response({'status': '400', 'error': '验证错误'})
    else:
        return Response({'status': '400', 'error': '用户不存在'})


# 注销登录
@api_view(['POST'])
def login_out(request):
    logout(request)
    return Response({'status': '200'})


@api_view(['GET', 'POST'])
def project_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if Project.objects.filter(name=name).count() != 0:
            return Response({"status": '400', 'error': '项目名称已存在'})
        else:
            project = Project(name=name, description=description, create_user=str(request.user.id))
            project.save()
            project_id = project.project_id
            create_project_store(project_id)
            return Response({"status": '201', "project_id": project_id})
    elif request.method == 'GET':
        project = Project.objects.filter(create_user=str(request.user.id)).values('project_id', 'name', 'description')
        return Response(project)


@api_view(['GET', 'POST'])
def project_user_current(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        request.session['project_id'] = project_id
        return Response({"status": '201', "project_id": project_id})
    elif request.method == 'GET':
        project_id = getattr(request.session, "project_id", "")
        return Response({"status": '200', "project_id": project_id})


@api_view(['POST', 'DELETE'])
def project_user_one(request):
    if request.method == 'DELETE':
        project_id = request.data['project_id']
        drop_project_store(project_id)
        Project.objects.filter(project_id=project_id).delete()
        return Response({'status': '204'})
    elif request.method == 'POST':
        return Response({'status': '201'})
