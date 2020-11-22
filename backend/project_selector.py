#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 23:19
# @Author  : cheng hao
# @Email   : howeycheng@163.com
# @File    : project_selector.py
# @Software: PyCharm


from django.utils.deprecation import MiddlewareMixin


class ProjectSelector(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        """
        用于判断用户所在项目
        :param request:
        :return:
        """
        if request.session.get('project_id', "") != "":
            project_id = request.session['project_id']
            name = 'project_unit_' + project_id
            external_db = {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': name,
                'USER': 'root',
                'PASSWORD': 'root',
                'HOST': '10.1.160.162',
                'PORT': '3306',
            }
            setattr(request, '_external_db', external_db)
