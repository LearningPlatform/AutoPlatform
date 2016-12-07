from django.shortcuts import render_to_response, HttpResponse
import json

from .platform.datahandle import prodata, envdata, vardata, moduledata, suitedata, \
    casedata, apidata, rundata, resultdata, dapidata, funcdata, recorddata, checkdata
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


def case_detail(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.get_case_detail(data)
    print(json.dumps(resp))
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
    resp = casedata.create_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_edit(req):
    """
    编辑case的基本信息
    请求方法：post
    如：
    {
	"case_id":1,
    "pro_id":2,
    "api_id":2,
    "case_desc":"测试编辑描述",
    "case_name":"正确登录",
    "depnd_api_id":1,
    "input_data":"{'username': '$.data.email', 'pwd': '{$get_md5_value(\"000000\")$}'}",
    "exp_data":"",
    "case_schema":"{\"$schema\":\"http://json-schema.org/draft-04/schema#\",\"type\":\"object\",\"properties\":{\"data\":{\"type\":\"object\",\"properties\":{\"username\":{\"type\":\"string\"},\"hid\":{\"type\":\"string\"},\"email\":{\"type\":\"string\"},\"noticeApp\":{\"type\":\"string\"},\"applyApp\":{\"type\":\"string\"},\"taskApp\":{\"type\":\"string\"},\"position\":{\"type\":\"string\"},\"orgId\":{\"type\":\"integer\"},\"uid\":{\"type\":\"string\"},\"hpwd\":{\"type\":\"string\"},\"companyName\":{\"type\":\"string\"},\"accessToken\":{\"type\":\"string\"},\"entryTime\":{\"type\":\"string\"},\"realname\":{\"type\":\"string\"},\"phone\":{\"type\":\"string\"},\"headimg\":{\"type\":\"string\"},\"orgName\":{\"type\":\"string\"}},\"required\":[\"username\",\"hid\",\"email\",\"noticeApp\",\"applyApp\",\"taskApp\",\"position\",\"orgId\",\"uid\",\"hpwd\",\"companyName\",\"accessToken\",\"entryTime\",\"realname\",\"phone\",\"headimg\",\"orgName\"]},\"msg\":{\"type\":\"string\"},\"code\":{\"type\":\"integer\"}},\"required\":[\"data\",\"msg\",\"code\"]}",
    "check_type":1
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
    resp = casedata.edit_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


# def case_info_edit(req):
#     """
#     编辑case的基本信息
#     请求方法：post
#     如：
#     {
#       "api_id": 1,     接口id
#       "case_id": 1,    case的id
#       "pro_id": 5,     项目id
#       "case_desc": "正向验证",     case描述
#       "case_name": "正确登录",     case名字
#       "suite_list":[1,2,3]     套件列表对象，checked为1，表示被勾选，
#                                                                                 checked为0，表示未被勾选；
#     }
#     :return:
#     如：
#     成功：
#     {
#       "code": 1,
#       "msg": "保存成功"
#     }
#     """
#     data = json.loads(str(req.body, encoding="utf-8"))
#     resp = casedata.edit_case_info(data)
#     return HttpResponse(json.dumps(resp), content_type="application/json")
#
#
# def case_req_edit(req):
#     """
#     编辑case的请求信息
#     请求方法：post
#     如：
#     {
#       "case_id": 1,    case的id
#       "input_data": xx,   根据设定的参数的格式，传入对应的的格式的值。如json的话，就直接传入json格式的对象等，数组就传入数组
#       "depnd_api_id":2    依赖接口id，若没有添加依赖接口，则默认置为0
#     }
#     :return:
#     如：
#     成功：
#     {
#       "code": 1,
#       "msg": "保存成功"
#     }
#     """
#     data = json.loads(str(req.body, encoding="utf-8"))
#     resp = casedata.edit_req(data)
#     return HttpResponse(json.dumps(resp), content_type="application/json")
#
#
# def case_resp_edit(req):
#     """
#    编辑case的请求信息
#    请求方法：post
#    如：
#    {
#      "case_id": 1,    case的id
#      "exp_data": xx,   根据设定的参数的格式，传入对应的的格式的值。如json的话，就直接传入json格式的对象等，数组就传入数组
#      "check_type": 0    核对的类型，0为默认，暂时都设为0，后续优化
#    }
#    :return:
#    如：
#    成功：
#    {
#      "code": 1,
#      "msg": "保存成功"
#    }
#    """
#     data = json.loads(str(req.body, encoding="utf-8"))
#     resp = casedata.edit_resp(data)
#     return HttpResponse(json.dumps(resp), content_type="application/json")


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


def case_run(req):
    """
       运行用例
       请求方法：post
       如：
        {
        "case_id":1,        case_id
        "case_type":2,      case类型，手动为1，录制为2
        "env_id":4          环境id
        }
       :return:
       如：
       成功：
    {
  "data":
  {
        "request_body": "{\"username\": \"liujing3@supernano.com\", \"pwd\": \"670b14728ad9902aecba32e22fa4f6bd\"}",
        "status_code": 200,
        "result_check": 1,
        "response_body": {
          "data": {
            "realname": "刘静3",
            "orgId": 19,
            "orgName": "测试技术部",
            "applyApp": "1",
            "headimg": "http://oa.supernano.com/static/head-img/uploads/219.jpg",
            "email": "liujing3@supernano.com",
            "hid": "liujing3",
            "taskApp": "1",
            "username": "liujing3@supernano.com",
            "accessToken": "704e8e873ae196e83fa3fb9861287823|219",
            "entryTime": "2015-07-08",
            "position": "游戏测试",
            "companyName": "湖南纳米娱乐",
            "phone": "14726968415",
            "noticeApp": "1",
            "hpwd": "000000",
            "uid": "219"
          },
          "code": 20000,
          "msg": "登录成功"
        },
        "exp_data": "刘静",
        "url": "http://oa.supernano.com/index.php?r=api/login/login",
        "schema": {
          "type": "object",
          "$schema": "http://json-schema.org/draft-04/schema#",
          "required": [
            "data",
            "msg",
            "code"
          ],
          "properties": {
            "data": {
              "type": "object",
              "required": [
                "username",
                "hid",
                "email",
                "noticeApp",
                "applyApp",
                "taskApp",
                "position",
                "orgId",
                "uid",
                "hpwd",
                "companyName",
                "accessToken",
                "entryTime",
                "realname",
                "phone",
                "headimg",
                "orgName"
              ],
              "properties": {
                "realname": {
                  "type": "string"
                },
                "orgId": {
                  "type": "integer"
                },
                "orgName": {
                  "type": "string"
                },
                "hid": {
                  "type": "string"
                },
                "applyApp": {
                  "type": "string"
                },
                "headimg": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "noticeApp": {
                  "type": "string"
                },
                "taskApp": {
                  "type": "string"
                },
                "username": {
                  "type": "string"
                },
                "accessToken": {
                  "type": "string"
                },
                "entryTime": {
                  "type": "string"
                },
                "position": {
                  "type": "string"
                },
                "companyName": {
                  "type": "string"
                },
                "phone": {
                  "type": "string"
                },
                "hpwd": {
                  "type": "string"
                },
                "uid": {
                  "type": "string"
                }
              }
            },
            "code": {
              "type": "integer"
            },
            "msg": {
              "type": "string"
            }
          }
        },
        "schema_check": 1
      },
      "code": 1,
      "msg": "删除成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = casedata.run_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def run(req):
    """
   运行用例
   请求方法：post
   如：
    {
    "pro_id":1,        case_id
    "suite_id":2,      case类型，手动为1，录制为2
    "env_id":4          环境id
    "report_name":"123123"
    }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = rundata.get_run_info(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def result_list(req):
    """
      获取项目所有的结果列表
      请求方法：post
      如：
      {
       "pro_id":1      项目id
       }
      :return:
      如：
      成功：
      {
      "data": [
        {
          "result_id": 39,
          "suite_id": 1,
          "start_time": "1478617457",
          "pass_num": 1,
          "report_name": "test",
          "end_time": "1478617457",
          "fail_num": 1,
          "pro_id": 1
        },
        {
          "result_id": 40,
          "suite_id": 1,
          "start_time": "1478617504",
          "pass_num": 1,
          "report_name": " 2016.11.08_ 冒烟测试 ",
          "end_time": "1478617505",
          "fail_num": 1,
          "pro_id": 1
        }
      ],
      "code": 1,
      "msg": "获取成功"
    }
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = resultdata.get_result_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def result_detail_list(req):
    """
      获取项目所有的结果列表
      请求方法：post
      如：
      {
       "result_id":50      结果id
       }
      :return:
      如：
      成功：
      {
      "code": 1,
      "data": [
        {
          "exp_data": "超时11",
          "pro_id": 5,
          "case_name": "正确登录",
          "api_id": 1,
          "module_id": 1,
          "is_pass": 0,
          "case_id": 1,
          "result_id": 50,
          "result_detail_id": 90,
          "is_set": 1,
          "check_type": 0,
          "input_data": "{'pro_id': 2}",
          "out_data": "{'content': {'msg': '请求超时', 'code': 0}, 'header': {'Content-Type': 'application/json', 'Date': 'Tue, 08 Nov 2016 16:04:39 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'Server': 'WSGIServer/0.2 CPython/3.5.2'}, 'status_code': 200}",
          "case_desc": "正向验证"
        },
        {
          "exp_data": "超时",
          "pro_id": 5,
          "case_name": "密码错误",
          "api_id": 1,
          "module_id": 1,
          "is_pass": 1,
          "case_id": 2,
          "result_id": 50,
          "result_detail_id": 91,
          "is_set": 1,
          "check_type": 0,
          "input_data": " {\"username\": \"liujing\",\"pwd\":\"000000\"}",
          "out_data": "{'content': {'msg': '请求超时', 'code': 0}, 'header': {'Content-Type': 'application/json', 'Date': 'Tue, 08 Nov 2016 16:04:39 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'Server': 'WSGIServer/0.2 CPython/3.5.2'}, 'status_code': 200}",
          "case_desc": "反向验证"
        }
      ],
      "msg": "返回成功"
    }
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = resultdata.get_result_detail_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def result_detail(req):
    """
      获取单个用例结果详情
      请求方法：post
      如：
      {
       "result_detail_id":50      结果用例id
       }
      :return:
      如：
      成功：
      {
      "data": {
        "out_data": {
          "response_data": {
            "header": {
              "Connection": "keep-alive",
              "Content-Type": "application/json",
              "Transfer-Encoding": "chunked",
              "X-Powered-By": "PHP/5.4.16",
              "Date": "Wed, 16 Nov 2016 06:22:24 GMT",
              "Server": "nginx/1.6.3"
            },
            "body": {
              "data": {},
              "msg": "用户名或者密码错误",
              "code": 20010
            }
          },
          "status_code": 200
        },
        "depnd_api_id": null,
        "module_id": 2,
        "input_data": {
          "url": "http://oa.supernano.com/index.php?r=api/login/login",
          "body": {
            "username": "liujing3@supernano.com",
            "pwd": "000000"
          }
        },
        "is_set": 1,
        "exp_data": "错误",
        "api_url": "{{host}}/index.php?r=api/login/login",
        "pro_id": 2,
        "case_id": 2,
        "api_method": "post",
        "api_desc": "无",
        "api_name": "登录接口",
        "api_type": "json",
        "api_id": 2,
        "result_detail_id": 163,
        "case_name": "错误登录-密码未加密",
        "is_pass": 1,
        "api_protocol": "http",
        "api_param": "username,pwd",
        "result_id": 94,
        "case_desc": "无",
        "check_type": null
      },
      "msg": "返回成功",
      "code": 1
    }
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = resultdata.get_result_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def result_delete(req):
    """
      删除结果
      请求方法：post
      如：
      {
       "result_id":50      结果id
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
    resp = resultdata.del_result(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_list(req):
    """
       获取项目所有的依赖接口列表
       请求方法：post
       如：
       {
        "pro_id":50      项目id
        }
       :return:
       如：
       成功：
       {
  "msg": "获取成功",
  "code": 1,
  "data": [
        {
          "depnd_api_url": "{{host}}/index.php?r=api/login/login",
          "depnd_api_id": 1,
          "depnd_id": 0,
          "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",
          "depnd_api_method": "post",
          "depnd_api_desc": "测试描述",
          "depnd_api_type": "json",
          "depnd_api_name": "获取uid",
          "pro_id": 2,
          "depnd_api_protocol": "http"
        },
        {
          "depnd_api_url": "{{host}}/index.php?r=api/login/login",
          "depnd_api_id": 4,
          "depnd_id": 0,
          "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",
          "depnd_api_method": "post",
          "depnd_api_desc": "测试描述",
          "depnd_api_type": "json",
          "depnd_api_name": "获取uid",
          "pro_id": 2,
          "depnd_api_protocol": "http"
        }
      ]
    }
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapidata.get_dapi_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_detail(req):
    """
       获取单个依赖接口详情
       请求方法：post
       如：
      {
    "depnd_api_id":1    依赖接口id
    }
       :return:
       如：
       成功：
       {
  "data": {
    "depnd_api_name": "获取uid",
    "depnd_api_protocol": "http",
    "depnd_api_desc": "测试描述",
    "depnd_api_method": "post",
    "depnd_api_type": "json",
    "depnd_api_id": 1,
    "depnd_api_url": "{{host}}/index.php?r=api/login/login",
    "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",
    "pro_id": 2,
    "depnd_id": 0
  },
  "msg": "获取成功",
  "code": 1
}
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapidata.get_dapi_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_create(req):
    """
       创建依赖接口
       请求方法：post
       如：
       {"depnd_api_name": "获取uid",      依赖接口名
        "depnd_api_protocol": "http",       依赖接口请求协议
        "depnd_api_desc": "测试描述",       依赖接口描述
        "depnd_api_method": "get",          依赖接口请求方式
        "depnd_api_type": "post",            依赖接口请求数据格式
        "depnd_api_url": "{{host}}/index.php?r=api/login/login",    依赖接口请求url
        "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",    请求体
        "pro_id": 2,    项目id
        "depnd_id": 0   当前依赖接口所需依赖的接口id
        }
       :return:
       如：
       成功：
       {
  "msg": "创建成功",
  "code": 1
}
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapidata.create_dapi(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_edit(req):
    """
       创建依赖接口
       请求方法：post
       如：
       {
           "depnd_api_id": 3,       需要修改的依赖接口id
       "depnd_api_name": "获取uid",      依赖接口名
        "depnd_api_protocol": "http",       依赖接口请求协议
        "depnd_api_desc": "测试描述",       依赖接口描述
        "depnd_api_method": "get",          依赖接口请求方式
        "depnd_api_type": "post",            依赖接口请求数据格式
        "depnd_api_url": "{{host}}/index.php?r=api/login/login",    依赖接口请求url
        "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",    请求体
        "pro_id": 2,    项目id
        "depnd_id": 0   当前依赖接口所需依赖的接口id
        }
       :return:
       如：
       成功：
       {
  "msg": "修改成功",
  "code": 1
}
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapidata.edit_dapi(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_delete(req):
    """
           删除依赖接口
           请求方法：post
           如：
           {
         "depnd_api_id": 3   依赖接口id
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
    resp = dapidata.del_dapi(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_run(req):
    """
      运行依赖接口
      请求方法：post
      如：
      {
        "depnd_api_id":1,
        "env_id":4
    }
      :return:
      如：
      成功：
    {
      "code": 1,
      "data": {
        "status_code": 200,
        "url": "http://oa.supernano.com/index.php?r=api/login/login",
        "request_body": "{\"username\": \"liujing3@supernano.com\", \"pwd\": \"670b14728ad9902aecba32e22fa4f6bd\"}",
        "response_body": {
          "code": 20000,
          "data": {
            "noticeApp": "1",
            "username": "liujing3@supernano.com",
            "phone": "14726968415",
            "position": "游戏测试",
            "entryTime": "2015-07-08",
            "taskApp": "1",
            "accessToken": "f22bda895ee41a50fab92d625ecae4bc|219",
            "hpwd": "000000",
            "orgId": 19,
            "orgName": "测试技术部",
            "email": "liujing3@supernano.com",
            "realname": "刘静3",
            "headimg": "http://oa.supernano.com/static/head-img/uploads/219.jpg",
            "uid": "219",
            "hid": "liujing3",
            "applyApp": "1",
            "companyName": "湖南纳米娱乐"
          },
          "msg": "登录成功"
        }
      },
      "msg": "删除成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapidata.run_d_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_create(req):
    """
   创建方法
   请求方法：post
   如：
   {
        "pro_id":1,                 项目id
        "func_name":"test",             方法名
        "func_code":"wkcjkdwhwjkh",         方法代码
        "func_desc":"hwbchjdcgxd"           方法描述
    }
   :return:
   如：
   成功：
   {
    "msg": "创建成功",
    "code": 1
    }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = funcdata.create_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_list(req):
    """
   获取项目下方法列表
   请求方法：post
   如：
   {
        "pro_id":1                 项目id
    }
   :return:
   如：
   成功：
   {
  "code": 1,
  "data": [
    {
      "func_desc": "hwbchjdcgxd",
      "pro_id": 1,
      "func_code": "wkcjkdwhwjkh",
      "func_name": "test",
      "func_id": 2
    }
  ],
  "msg": "获取成功"
}
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = funcdata.get_func_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_detail(req):
    """
    获取方法详情
    请求方法：post
    如：
    {
         "func_id":1                 方法id
     }
    :return:
    如：
    成功：
    {
      "data": {
        "func_name": "test",
        "func_id": 2,
        "pro_id": 1,
        "func_desc": "hwbchjdcgxd",
        "func_code": "wkcjkdwhwjkh"
      },
      "code": 1,
      "msg": "获取成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = funcdata.get_func_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_edit(req):
    """
    编辑方法
    请求方法：post
    如：
    {
         "func_id":1,                方法id
         "func_name":"test",             方法名
        "func_code":"wkcjkdwhwjkh",         方法代码
        "func_desc":"hwbchjdcgxd"           方法描述
     }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "编辑成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = funcdata.edit_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_delete(req):
    """
    删除方法
    请求方法：post
    如：
    {
         "func_id":1                 方法id
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
    resp = funcdata.del_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_run(req):
    """
    运行方法
    请求方法：post
    如：
    {
         "func_code":"jdshgjegdj"              方法代码
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
    resp = funcdata.run_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def record_anyproxy_req(req):
    """
        获取anyproxy录制的结果
        请求方法：post
        如：
        {
             req_id:5，    需要获取的请求的id
             host:"192.168.1.102",     本机的anyproxy服务器的host
             port:8002     GUI界面的端口地址（一般默认为8002）
         }
        :return:
        """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = recorddata.get_anyproxy_resp(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def rcd_case_create(req):
    """
    创建录制case
    请求：post
    参数：
    {
        "pro_id":2,     项目id
        "api_id":2,     接口id
        "module_id":1,      模块id
       "case_url": "{{host}}/index.php?r=api/login/login",      用例的url。需要用host与path做拼接
        "case_method" :"post",              接口的请求方式
        "case_protocol":"http",         接口请求协议
        "case_header":"",               接口请求头
        "input_data":{"username":"$.data.email","pwd":"{$get_md5_value('000000')$}"},       接口参数
        "exp_data": "刘静",           期望响应
        "check_type":1,             校验方式
        "case_name":"测试录制名字",        用例名
        "case_desc":"测试录制描述",             用例描述
        "depnd_api_id":1,           依赖接口id
        "resp_type":"json",         参数格式
        "suite_list":[1,2,3]            所属套件表
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = recorddata.create_rcd_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def rcd_case_edit(req):
    """
    创建录制case
    请求：post
    参数：
    {
        "case_id":8,    用例id
        "pro_id":2,     项目id
        "api_id":2,     接口id
        "module_id":1,      模块id
        "case_url": "{{host}}/index.php?r=api/login/login",      用例的url。需要用host与path做拼接
        "case_method" :"post",              接口的请求方式
        "case_protocol":"http",         接口请求协议
        "case_header":"",               接口请求头
        "input_data":{"username":"$.data.email","pwd":"{$get_md5_value('000000')$}"},       接口参数
        "exp_data": "刘静",           期望响应
        "check_type":1,             校验方式
        "case_name":"测试录制名22222222222字",        用例名
        "case_desc":"测试录制描222222述",             用例描述
        "depnd_api_id":1,           依赖接口id
        "resp_type":"json",         参数格式
        "suite_list":[5]            所属套件表
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = recorddata.edit_rcd_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def rcd_case_detail(req):
    """
    创建录制case
    请求：post
    参数：
    {
        "case_id":1,    用例id
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = recorddata.get_rcd_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def rcd_case_delete(req):
    """
    删除录制case
    请求：post
    参数：
    {
        "case_id":8,    用例id
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = recorddata.del_rcd_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_create(req):
    """
   创建方法
   请求方法：post
   如：
   {
        "pro_id":1,                 项目id
        "check_name":"test",             方法名
        "check_code":"wkcjkdwhwjkh",         方法代码
        "check_desc":"hwbchjdcgxd"           方法描述
    }
   :return:
   如：
   成功：
   {
    "msg": "创建成功",
    "code": 1
    }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checkdata.create_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_list(req):
    """
   获取项目下方法列表
   请求方法：post
   如：
   {
        "pro_id":1                 项目id
    }
   :return:
   如：
   成功：
   {
  "code": 1,
  "data": [
    {
      "check_desc": "hwbchjdcgxd",
      "pro_id": 1,
      "check_code": "wkcjkdwhwjkh",
      "check_name": "test",
      "check_id": 2
    }
  ],
  "msg": "获取成功"
}
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checkdata.get_check_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_detail(req):
    """
    获取方法详情
    请求方法：post
    如：
    {
         "check_id":1                 方法id
     }
    :return:
    如：
    成功：
    {
      "data": {
        "check_name": "test",
        "check_id": 2,
        "pro_id": 1,
        "check_desc": "hwbchjdcgxd",
        "check_code": "wkcjkdwhwjkh"
      },
      "code": 1,
      "msg": "获取成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checkdata.get_check_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_edit(req):
    """
    编辑方法
    请求方法：post
    如：
    {
         "check_id":1,                方法id
         "check_name":"test",             方法名
        "check_code":"wkcjkdwhwjkh",         方法代码
        "check_desc":"hwbchjdcgxd"           方法描述
     }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "编辑成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checkdata.edit_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_delete(req):
    """
    删除方法
    请求方法：post
    如：
    {
         "check_id":1                 方法id
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
    resp = checkdata.del_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_run(req):
    """
    运行方法
    请求方法：post
    如：
    {
         "check_code":"jdshgjegdj"              方法代码
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
    resp = checkdata.run_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")
