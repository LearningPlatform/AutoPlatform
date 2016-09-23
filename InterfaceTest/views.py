from django.shortcuts import render_to_response
from django.http import HttpResponse
from .datahandle import prodata as phl, envdata as ehl,vardata as vhl,modeldata as mhl,apidata as ahl,suitedata as shl \
    ,casedata as chl,runcase as rc

import json

def test(req):
    return render_to_response('test.html')

def test1(req):
    return render_to_response('test1.html')



def to_index(req):
    """
    渲染主页
    :param req:
    :return:
    """
    return render_to_response('index.html')

#######################################################################################################################
################################### 项目 ###############################################################################
#######################################################################################################################
def pro_get_all(req):
    """
    获取所有项目
    :param req:
    :return:
    """
    resp = phl.getAllPro()
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")
def pro_get(req):
    """
    获取特定的项目
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    pro = phl.getPro(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
        "data":pro}), content_type="application/json")

def pro_save(req):
    """
    保存项目
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    save_type = data['type']
    resp = {}
    if save_type == 1:
        phl.creatPro(data)
        resp = phl.getAllPro()
    if save_type == 2:
        phl.editSavePro(data)
        resp = phl.getAllPro()
    return HttpResponse(json.dumps({
        "msg": '添加成功',
        "data": resp
    }), content_type="application/json")

def pro_del(req):
    """
    删除项目
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    phl.delPro(data)
    resp = phl.getAllPro()
    return HttpResponse(json.dumps({
            "msg": '删除成功',
            "data": resp
        }), content_type="application/json")

########################################################################################################################
########################################## 环境 ######################################################################
#######################################################################################################################
def env_save(req):
    """
    保存环境变量
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    ehl.creatEnv(data)
    resp = ehl.getAllEnv(data)
    return HttpResponse(json.dumps({
        "msg": '添加成功',
        "data": resp
    }), content_type="application/json")

def env_get_all(req):
    """
    获取指定项目的环境列表
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = ehl.getAllEnv(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def env_del(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    ehl.delEnv(data)
    resp = ehl.getAllEnv(data)
    return HttpResponse(json.dumps({
        "msg": '删除成功',
        "data": resp
    }), content_type="application/json")

#######################################################################################################################
################################################ 变量 #################################################################
#######################################################################################################################
def var_save(req):
    """
    保存变量
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    vhl.creatVar(data)
    resp = vhl.getAllVar(data)
    return HttpResponse(json.dumps({
        "msg": '添加成功',
        "data": resp
    }), content_type="application/json")

def var_get_all(req):
    """
    获取所有变量
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vhl.getAllVar(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
        "data":resp}), content_type="application/json")

def var_del(req):
    """
    删除变量
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    vhl.delVar(data)
    resp = vhl.getAllVar(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def pro_get_envVar(req):
    """
    获取特定的环境的所有变量
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vhl.getAllEvnVar(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
        "data":resp}), content_type="application/json")

def pro_get_varEvn(req):
    """
    获取变量在各个环境下的所有值
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vhl.getAllVarEnv(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
        "data":resp}), content_type="application/json")

def pro_get_varEvn_all(req):
    """
    获取所有变量的所有环境下的值：变量对环境
    :param req:
    :return:
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vhl.getAllVarByVar(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
        "data":resp}), content_type="application/json")

#######################################################################################################################
################################################# 模块 ##############################################################
#######################################################################################################################
def model_save(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    mhl.creatModel(data)
    resp = mhl.getModelList(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def model_get(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = mhl.getModelList(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

#######################################################################################################################
################################################# 套件 ##############################################################
#######################################################################################################################
def suite_save(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    shl.creatSuite(data)
    resp = shl.getSuiteList(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def suite_get(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = shl.getSuiteList(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

#######################################################################################################################
################################################# 接口 ##############################################################
#######################################################################################################################
def api_save(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    ahl.creatApi(data)
    resp = ahl.getApiListAll(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def api_get_all(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = ahl.getApiListAll(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def api_get(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = ahl.getApiList(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

#######################################################################################################################
################################################# 用例 ##############################################################
#######################################################################################################################
def case_info_save(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    chl.creatCase(data)
    resp = chl.getAllCase(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def case_req_save(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    chl.saveReq(data)
    resp = chl.getCaseByApi(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def case_api_get(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = chl.getCaseByApi(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def case_namelist_api(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = chl.getCaseNameByApi(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")

def case_info(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = chl.getCaseInfo(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                    "data": resp}), content_type="application/json")


#######################################################################################################################
################################################# 执行 ##############################################################
#######################################################################################################################
def run_case(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    rc.run(data)
    return HttpResponse(json.dumps({"msg": '返回成功',
                                   }), content_type="application/json")