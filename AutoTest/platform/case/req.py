from ..tools import strtool,functool
from ...models import Functions

import requests
import json


class ReqResp:

    pro_id = 0
    var_map = {}
    url = ""
    param = ""
    api_method = ""
    api_protocol = ""
    resp = {}
    depnd_api_id = 0
    d_api = object

    def __init__(self):
        pass

    def setUrl(self):
        self.url = self.api_protocol + "://" + self.url
        while "{{" in self.url:
            a, b, str_param = strtool.str_replace(self.url, 1)
            self.url = self.url.replace(self.url[a:b], self.var_map[str_param])

    def setReqParam(self):
        while "{{" in self.param:
            a, b, str_param = strtool.str_replace(self.param, 1)
            self.param = self.param.replace(self.param[a:b], self.var_map[str_param])
        while "{$" in self.param:
            a, b, func_str_re, func_name = strtool.str_replace(self.param, 3)
            func_code = self.setFuncCode(func_name, func_str_re)
            self.param = self.param.replace(self.param[a:b], functool.get_return(func_name, func_code))
        self.param = self.param.replace("\'", "\"")

    def sendRequest(self):
        if self.api_method == "post":
            if "headers" in self.var_map.keys():
                headers = json.loads(self.var_map["headers"])
                re = requests.post(self.url, data=self.param, headers=headers)
            else:
                re = requests.post(self.url, data=self.param)
                print(re.request)
            self.resp = {
                "status_code": re.status_code,
                "response_data": {
                    "header": re.headers,
                    "body": re.json()
                }
            }
        if self.api_method == "get":
            if "headers" in self.var_map.keys():
                headers = json.loads(self.var_map["headers"])
                self.param = json.loads(self.param)
                re = requests.get(self.url, params=self.param, headers=headers)
            else:
                re = requests.get(self.url, params=self.param)
                print(re.request)
            self.resp = {
                "status_code": re.status_code,
                "response_data": {
                    "header": re.headers,
                    "body": re.json()
                }
            }

    def setFuncCode(self, func_name, func_str_re):
        func = Functions.objects.all().get(pro_id=self.pro_id, func_name=func_name)
        func_code = func.func_code + '\nprint('+ func_str_re + ')'
        return func_code

    def run(self):
        self.setUrl()
        self.setReqParam()
        self.sendRequest()