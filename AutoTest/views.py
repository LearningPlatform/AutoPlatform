from django.shortcuts import render_to_response,HttpResponse
import json

from .platform.datahandle import prodata
from .platform.tools import tostr


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
    如：{
          "msg": "返回成功",
          "data": [
                    {
                      "pro_name": "OA项目",
                      "pro_desc": "办公自动化",
                      "id": 1
                    }
          ]
        }
    """
    resp = prodata.getProList()
    return HttpResponse(json.dumps({"msg": '返回成功',"data": resp}), content_type="application/json")


def pro_detail(req):
    """
    获取特定的项目
    :param req:请求
    请求方法：post
    参数：项目id
    如：
        {"pid": 1}
    :return:特定项目的信息
    如：{
          "data": {
            "pro_desc": "办公自动化",
            "pro_name": "OA项目",
            "id": 1
          },
          "msg": "返回成功"
        }
    """
    tostr(req.body)
    data = json.loads(str(req.body, encoding="utf-8"))
    pro = prodata.getProDetail(data)
    return HttpResponse(json.dumps({"msg": '返回成功', "data":pro}), content_type="application/json")


# def pro_save(req):
#     """
#     保存项目
#     """
#     data = json.loads(str(req.body, encoding="utf-8"))
#     save_type = data['type']
#     resp = {}
#     if save_type == 1:
#         prodata.creatPro(data)
#         resp = prodata.getAllPro()
#     if save_type == 2:
#         prodata.editSavePro(data)
#         resp = prodata.getAllPro()
#     return HttpResponse(json.dumps({
#         "msg": '添加成功',
#         "data": resp
#     }), content_type="application/json")


# def pro_del(req):
#     """
#     删除项目
#     :param req:
#     :return:
#     """
#     data = json.loads(str(req.body, encoding="utf-8"))
#     prodata.delPro(data)
#     resp = prodata.getAllPro()
#     return HttpResponse(json.dumps({
#             "msg": '删除成功',
#             "data": resp
#         }), content_type="application/json")
