#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 23:19
# @Author  : cheng hao
# @Email   : howeycheng@163.com
# @File    : project_selector.py
# @Software: PyCharm

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class ProjectSelector(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        """
        用于判断用户所在项目
        :param request:
        :return:
        """
        if "apis/unit/" in request.path_info:
            # 如果请求的api为unit中的api，则根据当前请求用户session中的project_id来动态获取应操作的数据
            if request.session.get('project_id', "") != "":
                project_id = request.session['project_id']
                name = 'project_unit_' + project_id
                external_db = {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': name,
                    'USER': settings.DATABASES.get('default').get('USER'),
                    'PASSWORD': settings.DATABASES.get('default').get('PASSWORD'),
                    'HOST': settings.DATABASES.get('default').get('HOST'),
                    'PORT': settings.DATABASES.get('default').get('PORT'),
                }
                setattr(request, '_external_db', external_db)
            else:
                pass
