from django.contrib.auth import authenticate, login, logout

# Create your views here.

# 对应数据库
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view


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
        return Response({'status': '400','error':'用户名已存在'})
    else:
        User.objects.create_user(username=username, password=password)
        return Response({'status': '201'})


@api_view(['POST'])
def login(request):
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
            return Response({'status': '400','error':'验证错误'})
    else:
        return Response({'status': '400','error':'用户不存在'})


# 注销登录
@api_view(['POST'])
def login_out(request):
    logout(request)
    return Response({'status': '200'})
