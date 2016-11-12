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
        self.selApi()
        self.setUrl()
        self.setReqParam()
        self.sendRequest()

    def selApi(self):
        self.depnd_api = DepndApi.objects.all().get(depnd_api_id=self.depnd_api_id)

    def setUrl(self):
        self.url = self.depnd_api.depnd_api_protocol + "://" + self.depnd_api.depnd_api_url
        while "{{" in self.url:
            self.url = strtool.str_replace(self.url, self.var_map)

    def setReqParam(self):
        self.param = self.depnd_api.depnd_api_param
        while "{{" in self.param:
            self.param = strtool.str_replace(self.param, self.var_map)
        print(self.param)
        while "$." in self.param:
            a = self.param.find('$.')
            b_list = [self.param.find('"', a),self.param.find(',', a),self.param.find('}', a)]
            b = len(self.param)
            print(b_list)
            for i in b_list:
                if 0 < i < b:
                    b = i
            path = self.param[a:b]
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
        print(self.resp)

    def get_param_value(self, param_path):
        param_path = param_path[2:]
        param_path = param_path.split('.')
        param = self.resp
        for p in param_path:
            param = param[p]
        return param