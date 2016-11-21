from ..tools import strtool,functool

import requests
import json


class ReqResp:

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
            a, b, func_name, func_param = strtool.str_replace(self.param, 3)
            self.param = self.param.replace(self.param[a:b], functool.get_return(func_name,func_param))
        self.param = self.param.replace("\'", "\"")

    def sendRequest(self):
        if self.api_method == "post":
            if "headers" in self.var_map.keys():
                headers = json.loads(self.var_map["headers"])
                re = requests.post(self.url, data=self.param, headers=headers)
            else:
                re = requests.post(self.url, data=self.param)
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
            self.resp = {
                "status_code": re.status_code,
                "response_data": {
                    "header": re.headers,
                    "body": re.json()
                }
            }

    def run(self):
        self.setUrl()
        self.setReqParam()
        self.sendRequest()