from django.shortcuts import render_to_response,HttpResponse
import json

from .platform.datahandle import prodata, envdata, vardata
from .platform.tools import strtool


def to_index(req):
    """
    渲染主页
    :param req:
    :return:
    """
    return render_to_response('index.html')


def pro_list(req):
    """
    获取所有项目
    :param req:请求
    请求方法：get
    参数：无
    :return:返回所有项目
    如：
    成功：
    {
          "code": 1
          "msg": "返回成功",
          "data": [
                    {
                      "pro_name": "OA项目",
                      "pro_desc": "办公自动化",
                      "id": 1
                    }
          ]
    }
    失败：
    return {
            "code": 0,
            "msg": "获取失败",
        }
    """
    resp = prodata.get_pro_list()
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_detail(req):
    """
    获取特定的项目
    :param req:请求
    请求方法：post
    参数：项目id
    如：
        {"pro_id": 1}
    :return:特定项目的信息
    如：
    成功：
    {
          "data": {
            "pro_desc": "办公自动化",
            "pro_name": "OA项目",
            "id": 1
          },
          "code": 1
          "msg": "返回成功"
        }
    失败：
    {
            "code": 0,
            "msg": "获取失败，id不存在",
        }
    """
    data = json.loads(strtool.byteToStr(req.body))
    resp = prodata.get_pro_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_create(req):
    """
    创建新的项目
    :param req: 请求
    请求方法：post
    参数：项目名 pro_name  项目描述：pro_desc
    如：
    {
        "pro_name": "OA系统"，
        "pro_desc": "自动化办公"
    }
    :return:返回状态信息
    成功为：
    {
        "code": 1
        "msg"："项目创建成功"
    }
    失败：
    {
        "code": 0,
        "msg": "项目名不能为空！"
        }
    """
    data = json.loads(strtool.byteToStr(req.body))
    resp = prodata.create_pro(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_edit(req):
    """
        创建新的项目
        :param req: 请求
        请求方法：post
        参数：项目id pro_id 项目名 pro_name  项目描述：pro_desc
        如：
        {
            "pro_id" : 1,
            "pro_name": "OA系统"，
            "pro_desc": "自动化办公"
        }
        :return:返回状态信息
        成功为：
        {
            "code": 1
            "msg"："项目修改成功"
        }
        失败：
        {
            "code": 0,
            "msg": "项目名不能为空！"
        }
        """
    data = json.loads(strtool.byteToStr(req.body))
    resp = prodata.edit_pro(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_del(req):
    """
    删除
    :param req: 请求
    请求方法：post
    参数：项目id pro_id
    如：
    {
        "pro_id": 1
    }
    :return:返回状态信息
    成功为：
    {
        "code": 1
        "msg"："项目删除成功"
    }
    失败：
    {
         "code": 0,
        "msg": "删除失败，项目id不存在"
        }
    """
    data = json.loads(strtool.byteToStr(req.body))
    resp = prodata.del_pro(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_list(req):
    """
    获取所有项目
    :param req:请求
    请求方法：post
    参数：项目id pro_id
    如：
    {
        "pro_id":1
    }
    :return:返回所有环境
    如：
    成功：
    {
      "code": 1,
      "msg": "获取环境列表成功",
      "data": [
        {
          "id": 1,
          "env_desc": "无",
          "pro_id": 1,
          "env_name": "正式环境"
        }
      ]
    }
    失败：
    {
      "msg": "参数错误",
      "code": 0
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = envdata.get_env_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_detail(req):
    """
    获取特定的环境详情
    :param req:请求
    请求方法：post
    参数：项目id
    如：
        {"env_id": 1}
    :return:特定项目的信息
    如：
    成功：
    {
      "msg": "获取成功",
      "code": 1,
      "data": {
        "env_name": "正式环境",
        "pro_id": 1,
        "id": 1,
        "env_desc": "无"
      }
    }
    失败：
    {
        "code": 0,
        "msg": "获取失败，id不存在",
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = envdata.get_env_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_create(req):
    """
    创建环境
    :param req:请求
    请求方法：post
    参数：项目id：pro_id，环境名：env_name，描述：env_desc
    如：
        {
        "pro_id":1,
        "env_name":"测试环境",
        "env_desc":"描述"
        }
    :return:
    如：
    成功：
    {
        "code": 1,
        "msg": "环境创建成功"
    }
    失败：
    {
        "code": 0,
        "msg": "参数错误，项目id不存在"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = envdata.create_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_edit(req):
    """
    修改编辑环境
    :param req:请求
    请求方法：post
    参数：环境id：env_id，环境名：env_name，描述：env_desc
    如：
        {
        "env_id":1,
        "env_name":"测试环境",
        "env_desc":"描述"
        }
    :return:
    如：
    成功：
    {
        "code": 1,
        "msg": "环境创建成功"
    }
    失败：
    {
        "code": 0,
        "msg": "参数错误，环境id不存在"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = envdata.edit_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_del(req):
    """
    删除环境
    :param req:
    请求方法：post
    参数：环境id：env_id
    如：
        {
        "env_id":1,
        }
    :return:
    如：
    成功：
    {
        "code": 1,
        "msg": "环境删除成功"
    }
    失败：
    {
        "code": 0,
        "msg": "参数错误，环境id不存在"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = envdata.del_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_var_list(req):
    """
    获取特定环境下的变量的列表
    :param req:
    请求方法：post
    参数：环境id：env_id
    如：
        {
        "env_id":1,
        }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "返回成功",
      "data": [
        {
          "pro_id": 1,
          "env_id": 2,
          "var_id": 1,
          "var_type": "string",
          "var_name": "host",
          "var_value": "192.168.40.15",
          "var_desc": "host的值"
        },
        {
          "pro_id": 1,
          "env_id": 2,
          "var_id": 2,
          "var_type": "int",
          "var_name": "变量2",
          "var_value": "值2",
          "var_desc": "描述2"
        }
      ]
    }
    失败：
    {
        "code": 0,
        "msg": "参数错误，环境id不存在"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = envdata.get_env_varList(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_list(req):
    """
    获取项目的变量列表
    :param req:
    参数：项目id：pro_id
    如：
        {
        "pro_id":1,
        }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "返回成功",
      "data": [
        {
          "pro_id": 5,
          "var_desc": "host的值",
          "var_type": "string",
          "var_id": 1,
          "var_name": "host"
        },
        {
          "pro_id": 5,
          "var_desc": "描述2",
          "var_type": "int",
          "var_id": 2,
          "var_name": "变量2"
        }
      ]
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vardata.get_var_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_detail(req):
    """
    获取变量详情，即各个环境下的值
    :param req:
    请求方法：post
    参数：
        变量id：var_id
    如：
        {
        "var_id":1,
        }
    :return:
    如：
    成功：
    {
      "data": {
        "var_id": 1,
        "var_type": "string",
        "pro_id": 5,
        "value": [
          {
            "env_desc": "描述1",
            "env_name": "正式环境",
            "var_value": "192.168.40.15",
            "env_id": 2
          },
          {
            "env_desc": "描述2",
            "env_name": "测试环境",
            "var_value": "127.0.0.1",
            "env_id": 3
          }
        ],
        "var_desc": "host的值",
        "var_name": "host"
      },
      "msg": "返回成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vardata.get_var_of_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_create(req):
    """
    创建变量
    :param req:请求
    请求方法：post
    参数：
        项目id：pro_id   变量名：var_name   变量类型：var_type   变量描述：var_desc
        变量值：var_value---------json类型，key对用环境的id，value对应变量的值
    如：
        {
        "pro_id":1,
        "var_name":"host",
        "var_type":"String",
        "var_desc":"描述",
        "var_value":[{"env_id":1,"value":"192.168.40.25"},{"env_id":2,"value":"192.168.40.30"}]
        }
    :return:
    如：
    成功：
    {
        "code": 1,
        "msg": "变量创建成功"
    }
    失败：
    {
        "code": 0,
        "msg": "参数错误，环境id不存在"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vardata.create_vars(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_edit(req):
    """
    编辑变量
    :param req:请求
    请求方法：post
    参数：
        项目id：pro_id   变量名：var_name   变量类型：var_type   变量描述：var_desc     变量id：var_id
        变量值：var_value---------json类型，key对用环境的id，value对应变量的值
    如：
        {
        "pro_id":5,
        "var_id":1,
        "var_name":"host",
        "var_type":"String",
        "var_desc":"描述",
        "var_value":[{"env_id":2,"value":"192.168.40.25"},{"env_id":3,"value":"192.168.40.30"}]
        }
    :return:
    如：
    成功：
    {
        "code": 1,
        "msg": "变量编辑成功"
    }

    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vardata.edit_var(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_del(req):
    """
    删除变量
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vardata.del_var(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_list(req):
    """
    获取模块列表
    :param req:
    :return:
    """
    pass


def module_detail(req):
    """
    获取模块详情
    :param req:
    :return:
    """
    pass


def module_create(req):
    """
    创建模块
    :param req:请求
    :return
    """
    pass


def module_edit(req):
    """
    修改编辑模块
    :param req:
    :return:
    """
    pass


def module_del(req):
    """
    删除模块
    :param req:
    :return:
    """
    pass


def suite_list(req):
    """
    获取套件列表
    :param req:
    :return:
    """
    pass


def suite_detail(req):
    """
    获取套件详情
    :param req:
    :return:
    """
    pass


def suite_create(req):
    """
    创建套件
    :param req:请求
    :return
    """
    pass


def suite_edit(req):
    """
    修改编辑套件
    :param req:
    :return:
    """
    pass


def suite_del(req):
    """
    删除套件
    :param req:
    :return:
    """
    pass

