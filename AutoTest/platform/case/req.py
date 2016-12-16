from ..tools import strtool,functool
from ...models import Functions

import requests
import json


class ReqResp:

    pro_id = 0
    var_map = {}
    url = ""
    param = ""
    method = ""
    protocol = ""
    resp = {}

    resp_type = ""

    def __init__(self):
        pass

    def setUrl(self):
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
        if "headers" in self.var_map.keys():
            headers = json.loads(self.var_map["headers"])
            re = requests.request(method=self.method,url=self.url, data=self.param, headers=headers)
        else:
            re = requests.request(method=self.method, url=self.url, data=self.param)
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