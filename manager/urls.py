#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 10:44
# @Author  : chenghao
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path

from manager import views

urlpatterns = [
    path('user/login', views.login, name='login'),
    path('user/create', views.create_user, name='create_user'),
    path('user/loginout', views.login_out, name='login_out'),
]
