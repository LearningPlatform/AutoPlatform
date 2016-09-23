from django.core import serializers
import json

from InterfaceTest.models import Case,CaseSuite

def creatCase(data):
    pro_id = data['pro_id']
    api_id = data['api_id']
    case_desc = data['case_desc']
    case_name = data['case_name']
    case_id = Case.objects.create(pro_id=pro_id, api_id=api_id, case_desc=case_desc,case_name=case_name).id
    suite_list_data = data['suite_list']
    for suite in suite_list_data:
        if suite['checked']:
            CaseSuite.objects.create(pro_id=pro_id, api_id=api_id, case_id=case_id, suite_id=suite['suite_id'])

def saveReq(data):
    param_json = {}
    param_list = data['input_data']
    for param in param_list:
        param_json[param['name']]=param['value']
    case_id = data['case_id']
    case = Case.objects.all().get(id=case_id)
    case.input_data = param_json
    case.save()

def getAllCase(data):
    pro_id = data['pro_id']
    body = []
    data = json.loads(serializers.serialize("json", Case.objects.all().filter(pro_id=pro_id)))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body

def getCaseByApi(data):
    api_id = data['api_id']
    body = []
    data = json.loads(serializers.serialize("json", Case.objects.all().filter(api_id=api_id)))
    for e in data:
        str1 = e['fields']
        str1['id'] = e['pk']
        body.append(str1)
    return body

def getCaseNameByApi(data):
    api_id = data['api_id']
    body = []
    data = Case.objects.all().filter(api_id=api_id)
    for e in data:
        str1 = {}
        str1['id'] = e.id
        str1['name'] = e.case_name
        str1['pro_id'] = e.api_id
        body.append(str1)
    return body

def getCaseInfo(data):
    case_id = data['case_id']
    data = json.loads(serializers.serialize("json", Case.objects.all().filter(id=case_id)))[0]
    body = data['fields']
    body['id'] = data['pk']
    return body

