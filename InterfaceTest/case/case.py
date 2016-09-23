from django.core import serializers


from InterfaceTest.models import Case,Api
from ..request import req_http
import json

class CaseEntity:
    case=object
    protocol = "http://"
    method = ""
    url = ""
    param = ""
    param_json={}

    def __init__(self):
       pass

    def setCase(self,id):
        self.case = Case.objects.all().get(id=id)
        api_id = self.case.api_id
        api = Api.objects.all().get(id=api_id)
        self.method = api.api_method
        self.protocol = api.api_protocol.lower()
        self.url = api.api_url
        a = self.url.find('{')
        if a != -1:
            b = self.url.find('}')
            str1 = self.url[a + 1:b]
            str1 = str1.replace(str1, "oa.supernano.com")
            self.url = self.url.replace(self.url[a:b + 1], str1)
        self.param = self.case.input_data.replace('\'','\"')
        return self

    def run(self):
        req_http.post(self)
