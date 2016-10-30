from django.shortcuts import render_to_response,HttpResponse
import json

from .platform.datahandle import prodata, envdata, vardata, moduledata, suitedata, \
    casedata, apidata
from .platform.case import case
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
        "value":[{"env_id":1,"var_value":"192.168.40.25"},{"env_id":2,"var_value":"192.168.40.30"}]
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
        变量值：value---------json类型，key对用环境的id，var_value对应变量的值
    如：
        {
        "pro_id":5,
        "var_id":1,
        "var_name":"host",
        "var_type":"String",
        "var_desc":"描述",
        "value":[{"env_id":2,"var_value":"192.168.40.25"},{"env_id":3,"var_value":"192.168.40.30"}]
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
    请求方法：post
    参数：变量id：var_id
    如：
        {
        "var_id":1,
        }
    :return:
    如：
    成功：
    {
        "code": 1,
        "msg": "变量删除成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vardata.del_var(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_list(req):
    """
    获取项目下的模块列表
    :param req:
    请求方法：post
    参数：
        项目id：pro_id
    如：
        {
        "pro_id":5,
        }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "获取成功",
      "data": [
        {
          "pro_id": 5,
          "module_id": 1,
          "module_desc": "ceshimiaoshu111111",
          "module_name": "ceshiming111111"
        }
      ]
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = moduledata.get_module_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_detail(req):
    """
    获取模块详情
    :param req:
    请求方法：post
    参数：
        模块id：module_id
    如：
        {
        "module_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "获取成功",
      "code": 1,
      "data": {
        "module_desc": "ceshimiaoshu111111",
        "module_id": 1,
        "pro_id": 5,
        "module_name": "ceshiming111111"
      }
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = moduledata.get_module_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_create(req):
    """
    创建模块
    :param req:
    请求方法：post
    参数：
        项目id：pro_id    模块名：module_name    模块描述：module_desc
    如：
        {
        "pro_id":5,
        "module_name":"ceshiming",
        "module_desc":"ceshimiaoshu"
        }
    :return:
    如：
    成功：
    {
      "msg": "创建模块成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = moduledata.create_module(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_edit(req):
    """
    编辑模块
    :param req:
    请求方法：post
    参数：
        项目id：pro_id    模块id：module_id    模块名：module_name    模块描述：module_desc
    如：
        {
        "pro_id":5,
        "module_id":1,
        "module_name":"ceshiming",
        "module_desc":"ceshimiaoshu"
        }
    :return:
    如：
    成功：
    {
      "msg": "编辑模块成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = moduledata.edit_module(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_del(req):
    """
    编辑模块
    :param req:
    请求方法：post
    参数：
        模块id：module_id
    如：
        {
        "module_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "删除模块成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = moduledata.del_module(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_api_list(req):
    """
    获取模块下的接口列表
    :param req:
    请求方法：post
    参数：
        项目id：module_id
    如：
        {
        "module_id":1,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "module_id": 1,
          "api_id": 1,
          "api_protocol": "http",
          "api_method": "post",
          "api_type": "34",
          "api_param": "username,pwd",
          "pro_id": 5,
          "api_desc": "登录",
          "api_name": "登录接口",
          "api_url": "{host}/login"
        },
        {
          "module_id": 1,
          "api_id": 2,
          "api_protocol": "http",
          "api_method": "post",
          "api_type": "12",
          "api_param": "email",
          "pro_id": 5,
          "api_desc": "忘记密码",
          "api_name": "忘记密码接口",
          "api_url": "{host}/forgetpwd"
        }
      ],
      "code": 1,
      "msg": "获取成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = moduledata.get_module_api_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_case_list(req):
    """
    获取模块下的用例列表
    :param req:
    请求方法：post
    参数：
        模块id：module_id
    如：
        {
        "module_id":1,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "case_name": "正确登录",
          "input_data": "请求参数",
          "exp_data": "期待输出",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "正向验证",
          "check_type": 0,
          "case_id": 1,
          "api_id": 1,
          "is_set": 1
        },
        {
          "case_name": "密码错误",
          "input_data": "请求参数2",
          "exp_data": "期待输出2",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "反向验证",
          "check_type": 0,
          "case_id": 2,
          "api_id": 1,
          "is_set": 1
        }
      ],
      "msg": "获取成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = moduledata.get_module_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_list(req):
    """
    获取套件列表
    :param req:
    请求方法：post
    参数：
        项目id：pro_id
    如：
        {
        "pro_id":5,
        }
    :return:
    如：
    成功：
    {
      "msg": "获取成功",
      "code": 1,
      "data": [
        {
          "suite_id": 1,
          "suite_desc": "全功能专用用例",
          "suite_name": "全功能测试",
          "pro_id": 5
        },
        {
          "suite_id": 2,
          "suite_desc": "冒烟专用用例",
          "suite_name": "冒烟测试",
          "pro_id": 5
        },
        {
          "suite_id": 3,
          "suite_desc": "测试描述",
          "suite_name": "测试名字",
          "pro_id": 5
        }
      ]
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suitedata.get_suite_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_detail(req):
    """
    获取套件详情
    请求方法：post
    参数：
        模块id：suite_id
    如：
        {
        "suite_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "获取成功",
      "data": {
        "suite_desc": "全功能专用用例",
        "suite_id": 1,
        "pro_id": 5,
        "suite_name": "全功能测试"
      },
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suitedata.get_suite_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_create(req):
    """
    创建套件
    请求方法：post
    参数：
        项目id：pro_id     套件名：suite_name   套件描述：suite_desc
    如：
        {
        "suite_name": "全功能测试2",
        "pro_id": 5,
        "suite_desc": "全功能专用用例2"
      }
    :return:
    如：
    成功：
    {
      "msg": "创建套件成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suitedata.create_suite(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_edit(req):
    """
    修改编辑套件
        请求方法：post
    参数：
        项目id：pro_id     套件id：suite_id    套件名：suite_name   套件描述：suite_desc
    如：
        {
        "suite_id":1,
        "suite_name": "全功能测试2",
        "pro_id": 5,
        "suite_desc": "全功能专用用例2"
      }
    :return:
    如：
    成功：
    {
      "msg": "编辑套件成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suitedata.edit_suite(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_del(req):
    """
    删除套件
    请求方法：post
    参数：
        模块id：suite_id
    如：
        {
        "suite_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "删除成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suitedata.del_suite(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_case_list(req):
    """
    获取套件下的case列表
    请求方法：post
    参数：
        模块id：suite_id
    如：
        {
        "suite_id":1,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "case_name": "正确登录",
          "input_data": "请求参数",
          "exp_data": "期待输出",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "正向验证",
          "check_type": 0,
          "case_id": 1,
          "api_id": 1,
          "is_set": 1
        },
        {
          "case_name": "密码错误",
          "input_data": "请求参数2",
          "exp_data": "期待输出2",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "反向验证",
          "check_type": 0,
          "case_id": 2,
          "api_id": 1,
          "is_set": 1
        }
      ],
      "msg": "获取成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suitedata.get_suite_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_list(req):
    """
    获取项目下的接口列表
    :param req:
    请求方法：post
    参数：
        项目id：pro_id
    如：
        {
        "pro_id":5,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "module_id": 1,
          "api_id": 1,
          "api_protocol": "http",
          "api_method": "post",
          "api_type": "34",
          "api_param": "username,pwd",
          "pro_id": 5,
          "api_desc": "登录",
          "api_name": "登录接口",
          "api_url": "{host}/login"
        },
        {
          "module_id": 1,
          "api_id": 2,
          "api_protocol": "http",
          "api_method": "post",
          "api_type": "12",
          "api_param": "email",
          "pro_id": 5,
          "api_desc": "忘记密码",
          "api_name": "忘记密码接口",
          "api_url": "{host}/forgetpwd"
        }
      ],
      "code": 1,
      "msg": "获取成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = apidata.get_api_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_detail(req):
    """
   获取项目下的接口列表
   :param req:
   请求方法：post
   参数：
       接口id：api_id
   如：
       {
       "api_id":1,
       }
   :return:
   如：
   成功：
       {
      "msg": "获取成功",
      "code": 1,
      "data": {
        "api_param": "username,pwd",
        "api_id": 1,
        "module_id": 1,
        "pro_id": 5,
        "api_url": "{host}/login",
        "api_method": "post",
        "api_type": "34",
        "api_protocol": "http",
        "api_name": "登录接口",
        "api_desc": "登录"
      }
    }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = apidata.get_api_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_create(req):
    """
    创建接口
    请求方法：post
    参数：
    如：
        {
        "api_param": "username,pwd",     接口参数
        "module_id": 1,                  模块id
        "pro_id": 5,                     项目id
        "api_url": "{host}/login",       接口url
        "api_method": "post",            请求方法：get，post，put，detele
        "api_type": "34",                请求类型
        "api_protocol": "http",          请求协议：http，tcp，udp等等（待定）
        "api_name": "登录接口",           接口名字
        "api_desc": "登录"                接口描述
      }
    :return:
    如：
    成功：
    {
      "msg": "创建接口成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = apidata.create_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_edit(req):
    """
    修改编辑接口
        请求方法：post
    如：
       {
        "api_param": "username,pwd",     接口参数
        "module_id": 1,                  模块id
        "pro_id": 5,                     项目id
        "api_id": 5,                     接口id
        "api_url": "{host}/login",       接口url
        "api_method": "post",            请求方法：get，post，put，detele
        "api_type": "34",                请求类型
        "api_protocol": "http",          请求协议：http，tcp，udp等等（待定）
        "api_name": "登录接口",           接口名字
        "api_desc": "登录"                接口描述
      }
    :return:
    如：
    成功：
    {
      "msg": "编辑接口成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = apidata.edit_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_del(req):
    """
    删除接口
    请求方法：post
    参数：
        接口id：api_id
    如：
        {
        "api_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "删除成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = apidata.del_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_case_list(req):
    """
    获取接口下的case列表+
    请求方法：post
    参数：
        接口id：api_id
    如：
        {
        "api_id":1,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "case_name": "正确登录",
          "input_data": "请求参数",
          "exp_data": "期待输出",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "正向验证",
          "check_type": 0,
          "case_id": 1,
          "api_id": 1,
          "is_set": 1
        },
        {
          "case_name": "密码错误",
          "input_data": "请求参数2",
          "exp_data": "期待输出2",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "反向验证",
          "check_type": 0,
          "case_id": 2,
          "api_id": 1,
          "is_set": 1
        }
      ],
      "msg": "获取成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = apidata.get_api_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_list(req):
    """
    获取项目下的case列表+
    请求方法：post
    参数：
        项目id：pro_id
    如：
        {
        "pro_id":5,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "case_name": "正确登录",
          "input_data": "请求参数",
          "exp_data": "期待输出",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "正向验证",
          "check_type": 0,
          "case_id": 1,
          "api_id": 1,
          "is_set": 1
        },
        {
          "case_name": "密码错误",
          "input_data": "请求参数2",
          "exp_data": "期待输出2",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "反向验证",
          "check_type": 0,
          "case_id": 2,
          "api_id": 1,
          "is_set": 1
        }
      ],
      "msg": "获取成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.get_pro_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_create(req):
    """
    创建case
    请求方法：post
    如：
    {
      "api_id": 1,     接口id
      "pro_id": 5,     项目id
      "case_desc": "正向验证",     case描述
      "case_name": "正确登录",     case名字
      "suite_list":[{"checked":1,"suite_id":1},{"checked":0,"suite_id":2}]     套件列表对象，checked为1，表示被勾选，
                                                                                checked为0，表示未被勾选；
    }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "保存成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.create_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_create2(req):
    """
    创建case
    请求方法：post
    如：
    {
      "api_id": 1,     接口id
      "pro_id": 5,     项目id
      "case_desc": "正向验证",     case描述
      "case_name": "正确登录",     case名字
      "suite_list":[1,2]     套件列表对象，列表中为所属的suite_id
    }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "保存成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.create_case2(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_info_edit(req):
    """
    编辑case的基本信息
    请求方法：post
    如：
    {
      "api_id": 1,     接口id
      "case_id": 1,    case的id
      "pro_id": 5,     项目id
      "case_desc": "正向验证",     case描述
      "case_name": "正确登录",     case名字
      "suite_list":[{"checked":1,"suite_id":1},{"checked":0,"suite_id":2}]     套件列表对象，checked为1，表示被勾选，
                                                                                checked为0，表示未被勾选；
    }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "保存成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.edit_case_info(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_info_edit2(req):
    """
    编辑case的基本信息
    请求方法：post
    如：
    {
      "api_id": 1,     接口id
      "case_id": 1,    case的id
      "pro_id": 5,     项目id
      "case_desc": "正向验证",     case描述
      "case_name": "正确登录",     case名字
      "suite_list":[1,2,3]     套件列表对象，checked为1，表示被勾选，
                                                                                checked为0，表示未被勾选；
    }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "保存成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.edit_case_info2(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_req_edit(req):
    """
    编辑case的请求信息
    请求方法：post
    如：
    {
      "case_id": 1,    case的id
      "input_data": xx,   根据设定的参数的格式，传入对应的的格式的值。如json的话，就直接传入json格式的对象等，数组就传入数组
    }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "保存成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.edit_req(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_resp_edit(req):
    """
   编辑case的请求信息
   请求方法：post
   如：
   {
     "case_id": 1,    case的id
     "exp_data": xx,   根据设定的参数的格式，传入对应的的格式的值。如json的话，就直接传入json格式的对象等，数组就传入数组
     "check_type": 0    核对的类型，0为默认，暂时都设为0，后续优化
   }
   :return:
   如：
   成功：
   {
     "code": 1,
     "msg": "保存成功"
   }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.edit_resp(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_del(req):
    """
   删除case
   请求方法：post
   如：
   {
     "case_id": 1,    case的id
   }
   :return:
   如：
   成功：
   {
     "code": 1,
     "msg": "删除成功"
   }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.del_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def test(req):
    t = case.CaseEntity(1)
    return HttpResponse(json.dumps({"msg": 1}), content_type="application/json")


