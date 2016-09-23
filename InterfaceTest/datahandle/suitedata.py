from django.core import serializers
import json

from InterfaceTest.models import Suite

def creatSuite(data):
    pro_id = data['pro_id']
    suite_name = data['suite_name']
    suite_desc = data['suite_desc']
    Suite.objects.create(pro_id=pro_id,suite_name=suite_name,suite_desc=suite_desc)

def getSuiteList(data):
    pro_id = data['pro_id']
    body = []
    data = json.loads(serializers.serialize("json", Suite.objects.all().filter(pro_id=pro_id)))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body