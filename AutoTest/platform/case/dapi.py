from ...models import DepndApi
from .req import ReqResp
from ..tools import strtool


class Interface(ReqResp):
    case = object
    depnd_api = object

    def __init__(self, D_api_id, var_map):
        ReqResp.__init__(self)
        self.depnd_api_id = D_api_id
        self.depnd_api = DepndApi.objects.all().get(depnd_api_id=self.depnd_api_id)
        self.url = self.depnd_api.depnd_api_url
        self.param = self.depnd_api.depnd_api_param
        self.api_protocol = self.depnd_api.depnd_api_protocol
        self.depnd_api_id = self.depnd_api.depnd_id
        self.api_method = self.depnd_api.depnd_api_method
        self.var_map = var_map
        self.handle_depnd_param()
        self.pro_id = self.depnd_api.pro_id

    def handle_depnd_param(self):
        while "$." in self.param:
            path = strtool.str_replace(self.param, 2)
            self.d_api = Interface(self.depnd_api_id, var_map=self.var_map)
            self.d_api.run()
            self.param = self.param.replace(path, str(self.d_api.get_param_value(path)))

    def get_param_value(self, param_path):
        param_path = param_path[2:]
        param_path = param_path.split('.')
        param = self.resp["response_data"]["body"]
        for p in param_path:
            param = param[p]
        return param
