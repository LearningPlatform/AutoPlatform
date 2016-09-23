from django.core import serializers
from ..case import case as case
from ..models import Case

import json

def run(data):
    api_id = data['api_id']
    case_list = Case.objects.all().filter(api_id=api_id)
    for case1 in case_list:
        a = case.CaseEntity()
        a.setCase(case1.id)
        a.run()