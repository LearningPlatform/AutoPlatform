from django.core import serializers
import json

from InterfaceTest.models import Model

def creatModel(data):
    pro_id = data['pro_id']
    model_name = data['model_name']
    model_desc = data['model_desc']
    Model.objects.create(pro_id=pro_id,model_name=model_name,model_desc=model_desc)

def getModelList(data):
    pro_id = data['pro_id']
    body = []
    data = json.loads(serializers.serialize("json", Model.objects.all().filter(pro_id=pro_id)))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body