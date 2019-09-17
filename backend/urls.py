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
    # path('', views.index, name='index'),
    path('req/', views.get_req, name='req'),
    path('scene/', views.get_scene, name='scene'),
    path('sceneDetail/', views.get_scene_detail, name='sceneDetail'),
    path('cases/', views.get_cases, name='cases'),
    path('casesIo/', views.get_cases_io, name='casesDetail'),
    path('componentCol/', views.get_component_col, name='componentCol'),
    path('sceneParams/', views.get_scene_params, name='sceneParams'),
    path('sceneCasesIo/', views.get_scene_cases_io, name='sceneCasesIo'),
    path('sceneSetIo/', views.get_scene_set_io, name='sceneSetIo'),
]
