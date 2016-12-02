from ...models import CheckModel
from ..tools import jsontool, functool


def get_check_list(data):
    pro_id = data["pro_id"]
    body = []
    test = CheckModel.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_check_detail(data):
    check_id = data['check_id']
    data1 = CheckModel.objects.all().get(check_id=check_id)
    data_json = jsontool.convert_to_dict(data1)
    del(data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def create_check(data):
    pro_id = data["pro_id"]
    check_name = data["check_name"]
    check_code = data["check_code"]
    check_desc = data['check_desc']
    CheckModel.objects.all().create(pro_id=pro_id,check_name=check_name,check_code=check_code,check_desc=check_desc)
    return {
        "code": 1,
        "msg": "创建成功",
    }


def edit_check(data):
    check_id = data["check_id"]
    check_name = data['check_name']
    check_desc = data['check_desc']
    check_code = data["check_code"]
    CheckModel.objects.all().filter(check_id=check_id).update(check_name=check_name,check_code=check_code,
                                                              check_desc=check_desc)
    return {
        "code": 1,
        "msg": "修改成功"
    }


def del_check(data):
    check_id = data["check_id"]
    CheckModel.objects.all().get(check_id=check_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def run_check(data):
    check_name = data['check_name']
    check_code = data["check_code"]
    result = functool.run_code(check_name,check_code)
    return {
        "data": result,
        "code": 1,
        "msg": "运行成功"
    }
