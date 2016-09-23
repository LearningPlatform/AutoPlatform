from django.core import serializers
import json

from InterfaceTest.models import Vars, VarValue, Env

def creatVar(data):
    """
    创建变量
    :param data:
    :return:
    """
    pro_id = data['pro_id']
    var_name = data['var_name']
    var_desc = data['var_desc']
    var_type = data['var_type']
    var_id = Vars.objects.create(pro_id=pro_id, var_name=var_name
                        , var_desc=var_desc, var_type=var_type).id
    var_value = data['var_value']
    for var in var_value:
        env_id = var['currEnv']['id']
        value = var['value']
        VarValue.objects.create(pro_id=pro_id, env_id=env_id, var_value=value
                                , var_id=var_id)

def creatVarEvn(data):
    pro_id = data['pro_id']
    env_id = data['env_id']
    var_name = data['var_name']
    var_desc = data['var_desc']
    var_value = data['var_value']
    var_type = data['var_type']
    Vars.objects.create(pro_id=pro_id,env_id=env_id,var_name=var_name
                        ,var_desc=var_desc,var_type=var_type,var_value=var_value)


def getAllVar(data):
    pro_id = data['pro_id']
    body = []
    data = VarValue.objects.all().filter(pro_id=pro_id)
    var_id_list = []
    for i in data:
        var_id_list.append(i.var_id)
    var_id_list = list(set(var_id_list))
    for var_id in var_id_list:
        var_body = {}
        var_body['var_id'] = var_id
        data = Vars.objects.all().get(id=var_id)
        var_body['var_name'] = data.var_name
        var_body['var_type'] = data.var_type
        var_body['var_desc'] = data.var_desc
        body.append(var_body)
    print(body)
    return body


def getAllEvnVar(data):
    env_id = data['env_id']
    body = []
    data = json.loads(serializers.serialize("json", VarValue.objects.all().filter(env_id=env_id)))
    print(data)
    for e in data:
        str1 = e['fields']
        print(json.loads(serializers.serialize("json", Vars.objects.all().filter(id = e['fields']['var_id']))))
        str2 = json.loads(serializers.serialize("json", Vars.objects.all().filter(id = e['fields']['var_id'])))[0]['fields']
        body.append(dict(str1,**str2))
    return body

def getAllVarEnv(data):
    var_id = data['var_id']
    var_body = {}
    var_body['var_id'] = var_id
    data = Vars.objects.all().get(id=var_id)
    var_body['var_name'] = data.var_name
    var_body['var_type'] = data.var_type
    var_body['var_desc'] = data.var_desc
    var_value_list_ob = VarValue.objects.all().filter(var_id=var_id)
    var_value_list = []
    for var_value_ob in var_value_list_ob:
        env_id = var_value_ob.env_id
        env_name = Env.objects.all().get(id=env_id).env_name
        var_env_value = var_value_ob.var_value
        data_json = {
            "env_id": env_id,
            "env_name": env_name,
            "var_env_value": var_env_value
        }
        var_value_list.append(data_json)
    var_body['var_value'] = var_value_list
    print(var_body)
    return var_body

def getAllVarByVar(data):
    """
    通过变量分类，获取所有的变量
    :param data:
    :return:
    """
    var_list_body={}
    pro_id = data["pro_id"]
    var_list_body["pro_id"] = pro_id
    var_list = []
    data = VarValue.objects.all().filter(pro_id=pro_id)
    var_id_list = []
    for i in data:
        var_id_list.append(i.var_id)
    var_id_list = list(set(var_id_list))

    for var_id in var_id_list:
        var_body = {}
        var_body['var_id'] = var_id
        data = Vars.objects.all().get(id=var_id)
        var_body['var_name'] = data.var_name
        var_body['var_type'] = data.var_type
        var_body['var_desc'] = data.var_desc
        var_value_list_ob = VarValue.objects.all().filter(var_id=var_id)
        var_value_list=[]
        for var_value_ob in var_value_list_ob:
            env_id = var_value_ob.env_id
            env_name = Env.objects.all().get(id=env_id).env_name
            var_env_value = var_value_ob.var_value
            data_json = {
                "env_id":env_id,
                "env_name":env_name,
                "var_env_value":var_env_value
            }
            var_value_list.append(data_json)
        var_body['var_value'] = var_value_list
        print(var_body['var_value'])
        var_list.append(var_body)
    var_list_body["var_list"] = var_list
    return var_list_body

def delVar(data):
    var_id = data['var_id']
    var = Vars.objects.all().get(id=var_id)
    var.delete()
    varvalue_list = VarValue.objects.all().filter(var_id=var_id)
    for varvalue in varvalue_list:
        varvalue.delete()



