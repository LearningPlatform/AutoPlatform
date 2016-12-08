from ..case.mcase import MCase
from ..case.rcdcase import RcdCase
from ...models import Api, Suite, CaseSuite, Case, DepndApi
from ..tools import jsontool, casetool


def get_suite_case_list(data):
    suite_id = data["suite_id"]
    body = []
    test = CaseSuite.objects.all().filter(suite_id=suite_id)
    for a in list(test):
        a = jsontool.class_to_dict(Case.objects.all().get(case_id=a.case_id))
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_api_case_list(data):
    api_id = data["api_id"]
    body = []
    test = list(set(CaseSuite.objects.all().filter(api_id=api_id).values_list("case_id", flat=True)))
    for a in test:
        a = jsontool.class_to_dict(Case.objects.all().get(case_id=a))
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_pro_case_list(data):
    pro_id = data["pro_id"]
    body = []
    test = list(set(CaseSuite.objects.all().filter(pro_id=pro_id).values_list("case_id", flat=True)))
    for a in test:
        a = jsontool.class_to_dict(Case.objects.all().get(case_id=a))
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_case_detail(data):
    case_id = data["case_id"]
    data_case = jsontool.convert_to_dict(Case.objects.all().get(case_id=case_id))
    data_api = jsontool.convert_to_dict(Api.objects.all().get(api_id=data_case["api_id"]))
    del (data_api['_state'])
    if data_case["depnd_api_id"] != 0:
        depnt_api = jsontool.convert_to_dict(DepndApi.objects.all().get(depnd_api_id=data_case["depnd_api_id"]))
        del (depnt_api['_state'])
        data_case["depnt_api"] = depnt_api
    data_case["api"] = data_api
    data_case["case_type"] = 1
    del (data_case['_state'])
    suite_list = list(CaseSuite.objects.all().filter(case_id=case_id,case_type=1).values_list("suite_id", flat=True))
    data_case["suite_list"] = suite_list
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_case
    }


def create_case(data):
    pro_id = data['pro_id']
    api_id = data['api_id']
    case_desc = data['case_desc']
    case_name = data['case_name']
    depnd_api_id = data['depnd_api_id']
    check_type = data['check_type']
    case_id = Case.objects.create(pro_id=pro_id, api_id=api_id, case_desc=case_desc, case_name=case_name,
                                  depnd_api_id=depnd_api_id, check_type=check_type).case_id
    suite_list_data = data['suite_list']
    for suite_id in suite_list_data:
        CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite_id,case_type=1)
    return {
        "code": 1,
        "msg": "保存成功"
    }


def edit_case(data):
    case_id = data['case_id']
    pro_id = data['pro_id']
    api_id = data['api_id']
    case_desc = data['case_desc']
    case_name = data['case_name']
    depnd_api_id = data['depnd_api_id']
    input_data = data['input_data']
    exp_data = data['exp_data']
    case_schema = data['case_schema']
    check_type = data['check_type']
    Case.objects.all().filter(case_id=case_id).update(
        pro_id=pro_id, api_id=api_id, case_desc=case_desc,case_name=case_name, depnd_api_id=depnd_api_id,
        check_type=check_type,input_data=input_data,exp_data=exp_data, case_schema=case_schema)
    CaseSuite.objects.all().filter(case_id=case_id,case_type=1).delete()
    suite_list_data = data['suite_list']
    for suite_id in suite_list_data:
        CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite_id,case_type=1)
    return {
            "code": 1,
            "msg": "保存成功"
        }


# def edit_case_info(data):
#     case_id = data['case_id']
#     pro_id = data['pro_id']
#     api_id = data['api_id']
#     case_desc = data['case_desc']
#     case_name = data['case_name']
#     depnd_api_id = data['depnd_api_id']
#     check_type = data['check_type']
#     Case.objects.all().filter(case_id=case_id).update(pro_id=pro_id, api_id=api_id, case_desc=case_desc,
#                                                       case_name=case_name, depnd_api_id=depnd_api_id,
#                                                       check_type=check_type)
#     CaseSuite.objects.all().filter(case_id=case_id,case_type=1).delete()
#     suite_list_data = data['suite_list']
#     for suite_id in suite_list_data:
#         CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite_id,case_type=1)
#     return {
#         "code": 1,
#         "msg": "保存成功"
#     }
#
#
# def edit_req(data):
#     case_id = data['case_id']
#     input_data = data['input_data']
#     depnd_api_id = data['depnd_api_id']
#     Case.objects.all().filter(case_id=case_id).update(input_data=input_data, is_set=1, depnd_api_id=depnd_api_id)
#     return {
#         "code": 1,
#         "msg": "保存成功"
#     }
#
#
# def edit_resp(data):
#     case_id = data['case_id']
#     exp_data = data['exp_data']
#     case_schema = data['case_schema']
#     check_type = data['check_type']
#     Case.objects.all().filter(case_id=case_id).update(exp_data=exp_data, check_type=check_type,case_schema=case_schema)
#     return {
#         "code": 1,
#         "msg": "保存成功"
#     }
#

def del_case(data):
    case_id = data['case_id']
    Case.objects.all().get(case_id=case_id).delete()
    CaseSuite.objects.all().filter(case_id=case_id,case_type=1).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def run_case(data):
    case_id = data['case_id']
    case_type = data['case_type']
    env_id = data["env_id"]
    var_map = casetool.get_env_var_map(env_id)
    if case_type == 1:
        c = MCase(case_id, var_map, 0)
    else:
        c = RcdCase(case_id, var_map, 0)
    c.run()
    c.check_schema()
    c.check_result()
    return {
        "code": 1,
        "msg": "删除成功",
        "data": {
            "status_code":c.resp["status_code"],
            "response_body":c.resp["response_data"]["body"],
            "schema_check":c.schema_result,
            "schema":c.schema,
            "exp_data":c.exp_data,
            "body_check":c.body_result,
            "request_body":c.param,
            "url":c.url
        }
    }
