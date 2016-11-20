from ...models import Functions
from ..tools import jsontool, functool


def get_func_list(data):
    pro_id = data["pro_id"]
    body = []
    test = Functions.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_func_detail(data):
    func_id = data['func_id']
    functool.test(func_id)
    data = Functions.objects.all().get(func_id=func_id)
    data_json = jsontool.convert_to_dict(data)
    del(data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def create_func(data):
    pro_id = data["pro_id"]
    func_name = data["func_name"]
    func_code = data["func_code"]
    func_desc = data['func_desc']
    Functions.objects.all().create(pro_id=pro_id,func_name=func_name,func_code=func_code,func_desc=func_desc)
    return {
        "code": 1,
        "msg": "创建成功",
    }


def edit_func(data):
    func_id = data["func_id"]
    func_name = data['func_name']
    func_desc = data['func_desc']
    func_code = data["func_code"]
    Functions.objects.all().filter(func_id=func_id).update(func_name=func_name,func_code=func_code,func_desc=func_desc)
    return {
        "code": 1,
        "msg": "修改成功"
    }


def del_func(data):
    func_id = data["func_id"]
    Functions.objects.all().get(func_id=func_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def run_func(data):
    func_name = data['func_name']
    func_code = data["func_code"]
    result = functool.run_code(func_name,func_code)
    return {
        "data": result,
        "code": 1,
        "msg": "运行成功"
    }
