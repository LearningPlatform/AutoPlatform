from ...models import DepndApi
from ..tools import strtool

import json
import requests


class Interface:
    def __init__(self, D_api_id, var_map):
        self.depnd_api_id = D_api_id
        self.var_map = var_map
        self.depnd_api = object
        self.url = ""
        self.param = ""
        self.resp = {}
        self.pick_param = {}
        self.setApi()
        self.setUrl()
        self.setReqParam()
        self.sendRequest()

    def setApi(self):
        self.depnd_api = DepndApi.objects.all().get(depnd_api_id=self.depnd_api_id)

    def setUrl(self):
        self.url = self.depnd_api.depnd_api_protocol + "://" + self.depnd_api.depnd_api_url
        while "{{" in self.url:
            a, b, str_param = strtool.str_replace(self.url, 1)
            self.url = self.url.replace(self.url[a:b], self.var_map[str_param])

    def setReqParam(self):
        self.param = self.depnd_api.depnd_api_param
        while "{{" in self.param:
            a, b, str_param = strtool.str_replace(self.param, 1)
            self.param = self.param.replace(self.param[a:b], self.var_map[str_param])
        while "$." in self.param:
            path = strtool.str_replace(self.param, 2)
            self.d_api = Interface(self.depnd_api.depnd_id,var_map=self.var_map)
            self.param = self.param.replace(path,str(self.d_api.get_param_value(path)))
        self.param = self.param.replace("\'", "\"")

    def sendRequest(self):
        if self.depnd_api.depnd_api_method == "post":
            if "headers" in self.var_map.keys():
                headers = json.loads(self.var_map["headers"])
                re = requests.post(self.url, data=self.param, headers=headers)
            else:
                re = requests.post(self.url, data=self.param)
        if self.depnd_api.depnd_api_method == "get":
            if "headers" in self.var_map.keys():
                headers = json.loads(self.var_map["headers"])
                self.param = json.loads(self.param)
                re = requests.get(self.url, params=self.param, headers=headers)
            else:
                re = requests.get(self.url, params=self.param)
        self.resp = re.json()

    def get_param_value(self, param_path):
        param_path = param_path[2:]
        param_path = param_path.split('.')
        param = self.resp
        for p in param_path:
            param = param[p]
        return param