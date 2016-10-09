# 处理项目相关的请求
"""
@author:liujing
"""

from django.core import serializers
import json

from ...models import Project
from ..tools import dbtool


def getProList():
    """
    获取所有的项目
    :return: 所有的项目，类型为列表
    """
    body = []
    try:
        data = json.loads(serializers.serialize("json", Project.objects.all()))
        for e in data:
            str1 = e['fields']
            str1['id'] = e['pk']
            body.append(str1)
        return {
            "code": 1,
            "msg": "获取成功",
            "data": body
        }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "获取失败",
        }


def getProDetail(data):
    """
    获取单个项目详情
    :param data:
    :return:
    """
    try:
        pro_id = data['pro_id']
        id_list = dbtool.getFieldList(Project, 'id')
        if pro_id in id_list:
            data = Project.objects.all().get(id=pro_id)
            data_json = {
                "id": data.id,
                "pro_name": data.pro_name,
                "pro_desc": data.pro_desc
            }
            return {
                "code": 1,
                "msg": "获取成功",
                "data": data_json
            }
        else:
            return {
                "code": 0,
                "msg": "获取失败，id不存在",
            }
    except Exception as e:
        return {
            "code": 0,
            "msg": "请求超时",
        }


def createPro(data):
    """
    新建项目
    :param data:
    :return: 无
    """
    try:
        name = data['pro_name']
        description = data['pro_desc']
        if name == '':
            return {
                "code": 0,
                "msg": "项目名不能为空！"
            }
        Project.objects.create(pro_name=name, pro_desc=description)
        return {
                "code":1,
                "msg": "项目创建成功"
            }
    except Exception as e:
        print(e)
        return {
                "code": 0,
                "msg": "项目创建失败"
            }


def editPro(data):
    """
    编辑项目
    :param data:
    :return: 无
    """
    try:
        pro_id = data['pro_id']
        pro_name = data['pro_name']
        pro_desc = data['pro_desc']
        if pro_name == '':
            return {
                "code": 0,
                "msg": "项目名不能为空！"
            }
        a = Project.objects.all().filter(id=pro_id).update(pro_name=pro_name,pro_desc=pro_desc)
        if a == 0:
            return {
                "code": 0,
                "msg": "修改失败，项目id不存在！"
            }
        return {
            "code": 1,
            "msg": "修改成功"
        }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "修改失败"
        }


def delPro(data):
    """
    删除项目
    :param data:
    :return:无
    """
    try:
        pro_id = data['pro_id']
        id_list = dbtool.getFieldList(Project, 'id')
        if pro_id in id_list:
            pro = Project.objects.all().get(id=pro_id)
            pro.delete()
            return {
                "code": 1,
                "msg": "删除成功"
            }
        else:
            return {
                "code": 0,
                "msg": "删除失败，项目id不存在"
            }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "请求超时"
        }
