from ..tools import strtool

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
        # self.var_map = var_map
        # self.d_api = Interface(self.depnd_api_id, var_map=self.var_map)

    def setUrl(self):
        self.url = self.api_protocol + "://" + self.url
        while "{{" in self.url:
            a, b, str_param = strtool.str_replace(self.url, 1)
            self.url = self.url.replace(self.url[a:b], self.var_map[str_param])

    def setReqParam(self):
        while "{{" in self.param:
            a, b, str_param = strtool.str_replace(self.param, 1)
            self.param = self.param.replace(self.param[a:b], self.var_map[str_param])
        self.param = self.param.replace("\'", "\"")

    def sendRequest(self):
        if self.api_method == "post":
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
        if self.api_method == "get":
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

    def run(self):
        self.setUrl()
        self.setReqParam()
        self.sendRequest()