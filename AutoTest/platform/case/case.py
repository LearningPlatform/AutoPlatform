from .dapi import Interface

from .req import ReqResp
from ..tools import strtool

import json


class CaseEntity(ReqResp):

    result_id = 0
    result_detail = object
    is_pass = 0
    d_api = object

    def __init__(self):
        ReqResp.__init__(self)
        pass

    def handle_depnd_param(self):
        while "$." in self.param:
            path = strtool.str_replace(self.param, 2)
            self.d_api = Interface(self.depnd_api_id, var_map=self.var_map)
            self.d_api.run()
            self.param = self.param.replace(path, str(self.d_api.get_param_value(path)))

    def check_result(self):
        if json.dumps(self.resp["response_data"]["body"], ensure_ascii=False).find(self.exp_data) == -1:
            self.is_pass = 0
        else:
            self.is_pass = 1

    def save_result(self):
        if self.resp_type != "json":
            self.param = json.dumps(self.param)
        self.param = json.loads(self.param)

    def get_passnum(self):
        return self.is_pass
