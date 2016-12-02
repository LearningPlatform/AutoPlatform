from ...models import Vars, VarValue, CaseSuite, Result
from ..case.mcase import MCase
from ..case.rcdcase import RcdCase
from ..tools import jsontool, functool
import time


def get_run_info(data):
    report_name = data["report_name"]
    pro_id = data["pro_id"]
    env_id = data["env_id"]
    suite_id = data["suite_id"]
    pass_num = 0
    fail_num = 0
    result = Result.objects.create(report_name=report_name, pro_id=pro_id, suite_id=suite_id)
    var_map = get_env_var_map(env_id)
    case_list = get_run_case_id_list(suite_id)
    start_time = int(time.time())
    for a in case_list:
        if a["case_type"]==1:
            c = MCase(a["case_id"], var_map, result.result_id)
        else:
            c = RcdCase(a["case_id"], var_map, result.result_id)
        c.run()
        c.check_schema()
        c.check_result()
        c.save_result()
        if c.get_passnum() == 1:
            pass_num += 1
        else:
            fail_num += 1
    end_time = int(time.time())
    result.start_time = start_time
    result.end_time = end_time
    result.pass_num = pass_num
    result.fail_num = fail_num
    result.save()
    result_json = jsontool.convert_to_dict(result)
    del (result_json['_state'])
    return {
        "code": 1,
        "msg": "运行完毕",
        "data": result_json
        }


def get_env_var_map(env_id):
    var_map = {}
    var_value_ob_list = VarValue.objects.all().filter(env_id=env_id)
    for a in list(var_value_ob_list):
        var = Vars.objects.all().get(var_id=a.var_id)
        var_map[var.var_name] = a.var_value
    return var_map


def get_run_case_id_list(suite_id):
    case_list_json = []
    case_ob_list = CaseSuite.objects.all().filter(suite_id=suite_id)
    for case_ob in case_ob_list:
        case_json = {
            "case_id":case_ob.case_id,
            "case_type":case_ob.case_type
        }
        case_list_json.append(case_json)
    return case_list_json

