from django.core import serializers
import json

from InterfaceTest.models import Api

def creatApi(data):
    pro_id = data['pro_id']
    model_id = data['model_id']
    api_name = data['api_name']
    api_protocol = data['api_protocol']
    api_method = data['api_method']
    api_url = data['api_url']
    api_type = data['api_type']
    api_desc = data['api_desc']
    api_param = data['api_param']
    Api.objects.create(pro_id=pro_id,model_id=model_id,api_name=api_name,api_desc=api_desc,api_method=api_method
                       ,api_param=api_param,api_protocol=api_protocol,api_url=api_url,api_type=api_type)


def getApiList(data):
    model_id = data['model_id']
    body = []
    data = json.loads(serializers.serialize("json", Api.objects.all().filter(model_id=model_id)))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body

def getApiListAll(data):
    pro_id = data['pro_id']
    body = []
    data = json.loads(serializers.serialize("json", Api.objects.all().filter(pro_id=pro_id)))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body