#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 15:43
# @Author  : cheng hao
# @Email   : howeycheng@163.com
# @File    : disable_csrf_check.py
# @Software: PyCharm
from django.utils.deprecation import MiddlewareMixin


class DisableCSRFCheck(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        setattr(request, '_dont_enforce_csrf_checks', True)
