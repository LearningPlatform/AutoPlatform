# 处理项目相关的请求
"""
@author:liujing
"""

from django.core import serializers
import json

from ...models import Project


def getProList():
    """
    获取所有的项目
    :param data:前端的请求数据
    :return: 所有的项目，类型为列表
    """
    body = []
    data = json.loads(serializers.serialize("json", Project.objects.all()))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body


def getProDetail(data):
    """
    获取单个项目详情
    :param data:
    :return:
    """
    pro_id = data['pro_id']
    data = Project.objects.all().get(id=pro_id)
    data_json = {
        "id": data.id,
        "pro_name": data.pro_name,
        "pro_desc": data.pro_desc
    }
    return data_json


def createPro(data):
    """
    新建项目
    :param data:
    :return: 无
    """
    name = data['pro_name']
    description = data['pro_desc']
    Project.objects.create(pro_name=name,pro_desc=description)


def editSavePro(data):
    """
    编辑项目
    :param data:
    :return: 无
    """
    pro_id = data['pro_id']
    pro = Project.objects.all().get(id=pro_id)
    pro.pro_name = data['pro_name']
    pro.pro_desc = data['pro_desc']
    pro.save()


def delPro(data):
    """
    删除项目
    :param data:
    :return:无
    """
    pro_id = data['pro_id']
    pro = Project.objects.all().get(id=pro_id)
    pro.delete()