from ...models import Api, Suite, CaseSuite, Case, RecordCase
from ..tools import jsontool


def get_api_list(data):
    """
    获取项目下的套件列表
    :return:
    """
    pro_id = data["pro_id"]
    body = []
    test = Api.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_api_detail(data):
    """
    获取单个模块详情
    :param data:
    :return:
    """
    api_id = data['api_id']
    data = Api.objects.all().get(api_id=api_id)
    data_json = jsontool.convert_to_dict(data)
    del(data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def create_api(data):
    """
    新建接口
    :param data:
    :return: 无
    """
    pro_id = data['pro_id']
    module_id = data['module_id']
    api_name = data['api_name']
    api_protocol = data['api_protocol']
    api_method = data['api_method']
    api_url = data['api_url']
    api_type = data['api_type']
    api_desc = data['api_desc']
    api_param = data['api_param']
    Api.objects.create(pro_id=pro_id, module_id=module_id, api_name=api_name, api_desc=api_desc, api_method=api_method
                       , api_param=api_param, api_protocol=api_protocol, api_url=api_url, api_type=api_type)
    return {
        "code": 1,
        "msg": "创建接口成功",
    }


def edit_api(data):
    """
    编辑接口
    :param data:
    :return: 无
    """
    pro_id = data['pro_id']
    api_id = data['api_id']
    module_id = data['module_id']
    api_name = data['api_name']
    api_protocol = data['api_protocol']
    api_method = data['api_method']
    api_url = data['api_url']
    api_type = data['api_type']
    api_desc = data['api_desc']
    api_param = data['api_param']
    Api.objects.all().filter(api_id=api_id).update(pro_id=pro_id, module_id=module_id, api_name=api_name, api_desc=api_desc, api_method=api_method
                       , api_param=api_param, api_protocol=api_protocol, api_url=api_url, api_type=api_type)
    return {
        "code": 1,
        "msg": "修改成功"
    }


def del_api(data):
    api_id = data["api_id"]
    Api.objects.all().get(api_id=api_id).delete()
    CaseSuite.objects.all().filter(api_id=api_id).delete()
    Case.objects.all().filter(api_id=api_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def get_api_case_list(data):
    api_id = data["api_id"]
    body = []
    test = Case.objects.all().filter(api_id=api_id)
    for a in test:
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        a["case_type"] = 1
        body.append(a)
    test2 = RecordCase.objects.all().filter(api_id=api_id)
    for b in test2:
        b = jsontool.class_to_dict(b)
        del (b['_state'])
        b["case_type"] = 2
        body.append(b)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }
