from ...models import RecordCase, CaseSuite, DepndApi
from ..tools import jsontool
import requests


def get_anyproxy_resp(data):
    host = data["host"]
    port = data["port"]
    req_id = data["req_id"]
    url = "http://"+host+":"+str(port)+"/fetchBody?id="+str(req_id)
    re = requests.get(url)
    return re.json()


def create_rcd_case(data):
    pro_id = data["pro_id"]
    api_id = data["api_id"]
    module_id = data["module_id"]
    case_url = data["case_url"]
    case_method = data["case_method"]
    case_protocol = data["case_protocol"]
    case_header = data["case_header"]
    input_data = data["input_data"]
    exp_data = data["exp_data"]
    check_type = data["check_type"]
    case_name = data["case_name"]
    case_desc = data["case_desc"]
    depnd_api_id = data["depnd_api_id"]
    resp_type = data["resp_type"]
    suite_list_data = data['suite_list']
    case_schema = data['case_schema']
    case_id = RecordCase.objects.create(
        pro_id=pro_id, api_id=api_id, module_id=module_id, case_desc=case_desc, case_url=case_url,
        exp_data=exp_data, case_header=case_header, input_data=input_data,
        case_method=case_method, case_name=case_name, case_protocol=case_protocol,
        check_type=check_type, depnd_api_id=depnd_api_id, resp_type=resp_type,case_schema=case_schema).case_id
    for suite_id in suite_list_data:
        CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite_id, case_type=2)
    return {
        "code": 1,
        "msg": "创建成功",
        "data": {
            "case_id": case_id
        }
    }


def edit_rcd_case(data):
    case_id = data["case_id"]
    pro_id = data["pro_id"]
    api_id = data["api_id"]
    module_id = data["module_id"]
    case_url = data["case_url"]
    case_method = data["case_method"]
    case_protocol = data["case_protocol"]
    case_header = data["case_header"]
    input_data = data["input_data"]
    exp_data = data["exp_data"]
    check_type = data["check_type"]
    case_name = data["case_name"]
    case_desc = data["case_desc"]
    depnd_api_id = data["depnd_api_id"]
    resp_type = data["resp_type"]
    suite_list_data = data['suite_list']
    case_schema = data['case_schema']
    RecordCase.objects.filter(case_id=case_id).update(
        pro_id=pro_id, api_id=api_id, module_id=module_id, case_desc=case_desc, case_url=case_url,
        exp_data=exp_data, case_header=case_header, input_data=input_data,
        case_method=case_method, case_name=case_name, case_protocol=case_protocol,
        check_type=check_type, depnd_api_id=depnd_api_id, resp_type=resp_type,case_schema=case_schema)
    CaseSuite.objects.all().filter(case_id=case_id,case_type=2).delete()
    for suite_id in suite_list_data:
        CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite_id, case_type=2)
    return {
        "code": 1,
        "msg": "编辑成功",
    }


def del_rcd_case(data):
    case_id = data['case_id']
    RecordCase.objects.all().get(case_id=case_id).delete()
    CaseSuite.objects.all().filter(case_id=case_id, case_type=2).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def get_rcd_detail(data):
    case_id = data["case_id"]
    data_case = jsontool.convert_to_dict(RecordCase.objects.all().get(case_id=case_id))
    del (data_case['_state'])
    if data_case["depnd_api_id"] != 0:
        depnt_api = jsontool.convert_to_dict(DepndApi.objects.all().get(depnd_api_id=data_case["depnd_api_id"]))
        del (depnt_api['_state'])
        data_case["depnt_api"] = depnt_api
    suite_list = list(CaseSuite.objects.all().filter(case_id=case_id,case_type=2).values_list("suite_id", flat=True))
    data_case["suite_list"] = suite_list
    data_case["case_type"] = 2
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_case
    }
