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
    path('set/', views.get_set, name='set'),
    path('casesInSet/', views.get_cases_in_set, name='casesInSet'),
    path('reqOfCase/', views.get_req_of_case, name='reqOfCase'),
    path('run/', views.run, name='run'),
    path('casesToRun/', views.get_cases_to_run, name='casesToRun'),
    path('runLog/', views.get_run, name='runLog'),
    path('runLog/set/', views.get_run_set, name='runLogSet'),
    path('runLog/set/one', views.get_run_set_one, name='runLogSetOne'),
    # path('getCaseIo/', views.get_case_io, name='getCaseIo'),
]
