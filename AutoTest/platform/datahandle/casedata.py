from ...models import Api, Suite, CaseSuite, Case
from ..tools import jsontool


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


def create_case(data):
    pro_id = data['pro_id']
    api_id = data['api_id']
    case_desc = data['case_desc']
    case_name = data['case_name']
    case_id = Case.objects.create(pro_id=pro_id, api_id=api_id, case_desc=case_desc, case_name=case_name).case_id
    suite_list_data = data['suite_list']
    for suite_id in suite_list_data:
        CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite_id)
    return {
        "code": 1,
        "msg": "保存成功"
    }


def edit_case_info(data):
    case_id = data['case_id']
    pro_id = data['pro_id']
    api_id = data['api_id']
    case_desc = data['case_desc']
    case_name = data['case_name']
    Case.objects.all().filter(case_id=case_id).update(pro_id=pro_id, api_id=api_id, case_desc=case_desc,
                                                      case_name=case_name)
    CaseSuite.objects.all().filter(case_id=case_id).delete()
    suite_list_data = data['suite_list']
    for suite_id in suite_list_data:
        CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite_id)
    return {
        "code": 1,
        "msg": "保存成功"
    }


def edit_req(data):
    case_id = data['case_id']
    input_data = data['input_data']
    depnd_api_id = data['depnd_api_id']
    Case.objects.all().filter(case_id=case_id).update(input_data=input_data, is_set=1, depnd_api_id=depnd_api_id)
    return {
        "code": 1,
        "msg": "保存成功"
    }


def edit_resp(data):
    case_id = data['case_id']
    exp_data = data['exp_data']
    check_type = data['check_type']
    Case.objects.all().filter(case_id=case_id).update(exp_data=exp_data, check_type=check_type)
    return {
        "code": 1,
        "msg": "保存成功"
    }


def del_case(data):
    case_id = data['case_id']
    Case.objects.all().get(case_id=case_id).delete()
    CaseSuite.objects.all().filter(case_id=case_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }