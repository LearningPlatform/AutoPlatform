from django.core import serializers
import json

from InterfaceTest.models import Project

def getAllPro():
    body = []
    data = json.loads(serializers.serialize("json", Project.objects.all()))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body

def getPro(data):
    pro_id = data['pro_id']
    data = Project.objects.all().get(id=pro_id)
    data_json = {
        "id": data.id,
        "pro_name": data.pro_name,
        "pro_desc": data.pro_desc
    }
    return data_json

def creatPro(data):
    name = data['pro_name']
    description = data['pro_desc']
    Project.objects.create(pro_name=name,pro_desc=description)

def editSavePro(data):
    pro_id = data['pro_id']
    pro = Project.objects.all().get(id=pro_id)
    pro.pro_name = data['pro_name']
    pro.pro_desc = data['pro_desc']
    pro.save()

def delPro(data):
    pro_id = data['pro_id']
    pro = Project.objects.all().get(id=pro_id)
    pro.delete()
