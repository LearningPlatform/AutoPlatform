from ...models import Case, CaseSuite, Api, Result, ResultDetail, DepndApi
from ..tools import strtool
from .dapi import Interface

import requests
import json


class CaseEntity:

    def __init__(self, case_id, var_map, result_id):
        self.case_id = case_id
        self.var_map = var_map
        self.url = ""
        self.param = ""
        self.case = object
        self.api = object
        self.resp = {}
        self.is_pass = 0
        self.result_id = result_id
        self.result_detail = ResultDetail.objects.create(result_id=self.result_id)
        self.setCase()
        self.selApi()
        self.setUrl()
        self.setReqParam()
        self.sendRequest()
        self.check_result()
        self.result_detail.save()

    def setCase(self):
        self.case = Case.objects.all().get(case_id=self.case_id)
        self.result_detail.case_id = self.case_id
        self.result_detail.exp_data = self.case.exp_data
        self.result_detail.case_desc = self.case.case_desc

    def selApi(self):
        self.api = Api.objects.all().get(api_id=self.case.api_id)
        self.result_detail.api_id = self.api.api_id

    def setUrl(self):
        self.url = self.api.api_protocol + "://" + self.api.api_url
        while "{{" in self.url:
            self.url = strtool.str_replace(self.url, self.var_map)

    def setReqParam(self):
        self.param = self.case.input_data
        while "{{" in self.param:
            self.param = strtool.str_replace(self.param, self.var_map)
        while "$." in self.param:
            a = self.param.find('$.')
            b = self.param.find('"',a)
            path = self.param[a:b]
            self.d_api = Interface(self.case.depnd_api_id,var_map=self.var_map)
            self.param = self.param.replace(path,str(self.d_api.get_param_value(path)))
        self.param = self.param.replace("\'", "\"")
        print(self.param)
        self.result_detail.input_data = self.param

    def sendRequest(self):
        # 使用json
        # re = requests.post(self.url, json=json.loads(self.param))
        if self.api.api_method == "post":
            if "headers" in self.var_map.keys():
                headers = json.loads(self.var_map["headers"])
                re = requests.post(self.url, data=self.param, headers=headers)
            else:
                re = requests.post(self.url, data=self.param)
            self.resp = {
                "header": re.headers,
                "status_code": re.status_code,
                "content": re.json()
            }
        if self.api.api_method == "get":
            if "headers" in self.var_map.keys():
                headers = json.loads(self.var_map["headers"])
                self.param = json.loads(self.param)
                re = requests.get(self.url, params=self.param, headers=headers)
            else:
                re = requests.get(self.url, params=self.param)
            self.resp = {
                "header": re.headers,
                "status_code": re.status_code,
                "content": re.json()
            }
        self.result_detail.out_data = self.resp

    def check_result(self):
        if json.dumps(self.resp["content"], ensure_ascii=False).find(self.case.exp_data) == -1:
            self.is_pass = 0
        else:
            self.is_pass = 1
        self.result_detail.is_pass = self.is_pass

    def run(self):
        pass

    def get_passnum(self):
        return self.is_pass
