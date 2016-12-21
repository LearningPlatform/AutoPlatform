# 处理环境相关的请求
"""
@author:liujing
"""

from ...models import Env, Project, Vars, VarValue
from ..tools import dbtool, jsontool


def get_env_list(data):
    """
    获取环境列表
    :param data:
    :return:
    """
    try:
        pro_id = data['pro_id']
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
        env_id_list = dbtool.getFieldList(Env, 'env_id')
        if env_id in env_id_list:
            data = Env.objects.all().get(env_id=env_id)
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
        a = Env.objects.all().filter(env_id=env_id).update(env_name=env_name, env_desc=env_desc)
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
    """
    删除环境
    :param data:
    :return:
    """
    env_id = data["env_id"]
    Env.objects.all().get(env_id=env_id).delete()
    VarValue.objects.all().filter(env_id=env_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def get_env_varList(data):
    """
    获取该环境下的变量列表
    :param data:
    :return:
    """
    env_id = data["env_id"]
    body = []
    test = VarValue.objects.all().filter(env_id=env_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        var_info = jsontool.class_to_dict(Vars.objects.all().get(var_id=a["var_id"]))
        var = dict(a, **var_info)
        del (var['id'])
        del (var['_state'])
        body.append(var)
    return {
        "code": 1,
        "msg": "返回成功",
        "data": body
    }

