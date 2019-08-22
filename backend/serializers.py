#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/22 9:10 
# @Author : Aries 
# @Site :  
# @File : serializers.py 
# @Software: PyCharm

from rest_framework import serializers
from .models import Requirement


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['rqid', 'name', 'parent_id']
