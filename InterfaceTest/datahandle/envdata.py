from django.core import serializers
import json
from InterfaceTest.models import VarValue

from InterfaceTest.models import Env

def creatEnv(data):
    pro_id = data['pro_id']
    env_name = data['env_name']
    env_desc = data['env_desc']
    Env.objects.create(pro_id=pro_id,env_name=env_name,env_desc=env_desc)

def getAllEnv(data):
    pro_id = data['pro_id']
    body = []
    data = json.loads(serializers.serialize("json", Env.objects.all().filter(pro_id=pro_id)))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body

def delEnv(data):
    env_id = data['env_id']
    env = Env.objects.all().get(id=env_id)
    varvalue_list = VarValue.objects.all().filter(env_id=env_id)
    for varvalue in varvalue_list:
        varvalue.delete()
    env.delete()