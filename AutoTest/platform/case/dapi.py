from ...models import D_Api
from ..tools import strtool

import json
import requests


class Interface:

    def __init__(self, D_api_id, var_map):
        self.D_api_id = D_api_id
        self.var_map = var_map
        self.D_api = object
        self.url = ""
        self.param = ""
        self.resp = {}
        self.pick_param = {}
        self.selApi()
        self.setUrl()
        self.setReqParam()
        self.sendRequest()

    def selApi(self):
        self.D_api = D_Api.objects.all().get(D_api_id=self.D_api_id)

    def setUrl(self):
        self.url = self.D_api.D_api_protocol + "://" + self.D_api.D_api_url
        while "{{" in self.url:
            self.url = strtool.str_replace(self.url, self.var_map)

    def setReqParam(self):
        self.param = self.D_api.D_api_param
        while "{{" in self.param:
            self.param = strtool.str_replace(self.param, self.var_map)
        self.param = self.param.replace("\'", "\"")

    def sendRequest(self):
        if self.D_api.D_api_method == "post":
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
        if self.D_api.D_api_method == "get":
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

    def set_pick_param(self):
        pick_param_list = json.loads(self.D_api.D_pick_param)
        for pick_param in pick_param_list:
            param_path = pick_param["path"].split('.')
            param = self.resp["content"]
            for p in param_path:
                param = param[p]
                self.pick_param[pick_param["param_name"]]=param

    def get_pick_param(self):
        return self.pick_param
