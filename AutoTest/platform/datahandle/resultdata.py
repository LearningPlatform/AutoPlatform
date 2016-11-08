from ...models import Result, ResultDetail, Case

from ..tools import jsontool


def get_result_list(data):
    pro_id = data["pro_id"]
    body = []
    test = Result.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_result_detail_list(data):
    result_id = data["result_id"]
    body_list = []
    result_detail_list = ResultDetail.objects.all().filter(result_id=result_id)
    for result_datail in result_detail_list:
        a = jsontool.class_to_dict(result_datail)
        b = jsontool.class_to_dict(Case.objects.all().get(case_id=a["case_id"]))
        var = dict(a, **b)
        del (var['_state'])
        body_list.append(var)
    return {
        "code": 1,
        "msg": "返回成功",
        "data": body_list
    }