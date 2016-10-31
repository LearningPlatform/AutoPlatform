from ...models import Env, Project, Vars, VarValue, CaseSuite
from ..case.case import CaseEntity


import time


def get_run_info(data):
    env_id = data["env_id"]
    suite_id = data["suite_id"]
    var_map = get_env_var_map(env_id)
    case_list = get_run_case_id_list(suite_id)
    for a in case_list:
        c = CaseEntity(a, var_map)


def get_env_var_map(env_id):
    var_map = {}
    var_value_ob_list = VarValue.objects.all().filter(env_id=env_id)
    for a in list(var_value_ob_list):
        var = Vars.objects.all().get(var_id=a.var_id)
        var_map[var.var_name] = a.var_value
    return var_map


def get_run_case_id_list(suite_id):
    case_list = list(CaseSuite.objects.all().filter(suite_id=suite_id).values_list("case_id", flat=True))
    return case_list

