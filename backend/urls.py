#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/17 21:45 
# @Author : Aries 
# @Site :  
# @File : urls.py 
# @Software: PyCharm
from django.urls import path

from backend import views

urlpatterns = [
    path('testapi', views.testapi, name='testapi'),
]
