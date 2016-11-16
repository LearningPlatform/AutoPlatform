from ...models import Case, Api, ResultDetail
from .dapi import Interface

from .req import ReqResp
from ..tools import strtool

import json


class CaseEntity(ReqResp):

    result_id = 0
    result_detail = object
    case = object
    api = object
    is_pass = 0

    def __init__(self, case_id, var_map, result_id):
        ReqResp.__init__(self)
        self.result_id = result_id
        self.result_detail = ResultDetail.objects.create(result_id=self.result_id)
        self.case = Case.objects.all().get(case_id=case_id)
        self.api = Api.objects.all().get(api_id=self.case.api_id)
        self.url = self.api.api_url
        self.param = self.case.input_data
        self.api_protocol = self.api.api_protocol
        self.depnd_api_id = self.case.depnd_api_id
        self.api_method = self.api.api_method
        self.var_map = var_map
        self.handle_depnd_param()

    def handle_depnd_param(self):
        while "$." in self.param:
            path = strtool.str_replace(self.param, 2)
            self.d_api = Interface(self.depnd_api_id, var_map=self.var_map)
            self.d_api.run()
            self.param = self.param.replace(path, str(self.d_api.get_param_value(path)))

    def check_result(self):
        if json.dumps(self.resp["response_data"]["body"], ensure_ascii=False).find(self.case.exp_data) == -1:
            self.is_pass = 0
        else:
            self.is_pass = 1

    def save_result(self):
        if self.api.api_type != "json":
            self.param = json.dumps(self.param)
        self.param = json.loads(self.param)
        input_data = {
            "url": self.url,
            "body": self.param
        }
        self.result_detail.case_id = self.case.case_id
        self.result_detail.exp_data = self.case.exp_data
        self.result_detail.case_desc = self.case.case_desc
        self.result_detail.api_id = self.api.api_id
        self.result_detail.input_data = input_data
        self.result_detail.out_data = self.resp
        self.result_detail.is_pass = self.is_pass
        self.result_detail.save()

    def get_passnum(self):
        return self.is_pass
