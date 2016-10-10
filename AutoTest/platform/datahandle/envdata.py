# 处理环境相关的请求
"""
@author:liujing
"""

from ...models import Env, Project
from ..tools import dbtool, jsontool


def get_env_list(data):
    """
    获取环境列表
    :param data:
    :return:
    """
    try:
        pro_id = data['pro_id']
        id_list = dbtool.getFieldList(Env, 'pro_id')
        if pro_id in id_list:
            body = []
            test = Env.objects.all().filter(pro_id=pro_id)
            for a in list(test):
                a = jsontool.class_to_dict(a)
                del (a['_state'])
                body.append(a)
            return {
                "code": 1,
                "msg": "获取环境列表成功",
                "data": body
            }
        else:
            return {
                "code": 0,
                "msg": "获取失败，项目不存在",
            }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "参数错误"
        }


def get_env_detail(data):
    """
    获取环境详情
    :param data:
    :return:
    """
    try:
        env_id = data['env_id']
        id_list = dbtool.getFieldList(Env, 'id')
        if env_id in id_list:
            data = Env.objects.all().get(id=env_id)
            data_json = jsontool.convert_to_dict(data)
            del(data_json['_state'])
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


def create_env(data):
    """
    创建环境
    :param data:
    :return:
    """
    try:
        pro_id = data['pro_id']
        env_name = data['env_name']
        env_desc = data['env_desc']
        pro_id_list = dbtool.getFieldList(Project, 'id')
        if pro_id in pro_id_list:
            if env_name == '':
                return {
                    "code": 0,
                    "msg": "环境名不能为空！"
                }
            Env.objects.create(pro_id=pro_id, env_name=env_name, env_desc=env_desc)
            return {
                    "code": 1,
                    "msg": "环境创建成功"
                }
        else:
            return {
                "code": 0,
                "msg": "参数错误，项目id不存在"
            }
    except Exception as e:
        print(e)
        return {
                "code": 0,
                "msg": "参数错误"
            }


def edit_env(data):
    """
    编辑环境
    :param data:
    :return: 无
    """
    try:
        env_id = data['env_id']
        env_name = data['env_name']
        env_desc = data['env_desc']
        if env_name == '':
            return {
                "code": 0,
                "msg": "项目名不能为空！"
            }
        a = Env.objects.all().filter(id=env_id).update(env_name=env_name, env_desc=env_desc)
        if a == 0:
            return {
                "code": 0,
                "msg": "修改失败，环境id不存在！"
            }
        return {
            "code": 1,
            "msg": "修改成功"
        }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "参数错误"
        }


def del_env(data):
    return {
        "msg": "待定"
    }
