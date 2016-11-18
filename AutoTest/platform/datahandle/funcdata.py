from ...models import Functions
from ..tools import jsontool


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
    Functions.objects.all().create(pro_id=pro_id,func_name=func_name,func_code=func_code)
    return {
        "code": 1,
        "msg": "创建成功",
    }