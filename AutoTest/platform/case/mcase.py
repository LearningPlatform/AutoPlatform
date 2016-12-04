from ...models import Case, Api, ResultDetail

from .req import ReqResp
from .case import CaseEntity


class MCase(CaseEntity, ReqResp):

    case = object

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
        self.pro_id = self.case.pro_id
        self.url = self.api_protocol + "://" + self.url
        self.exp_data = self.case.exp_data
        self.resp_type = self.api.api_type
        self.schema = self.case.case_schema
        self.check_type = self.case.check_type

    def save_result(self):
        CaseEntity.save_result(self)
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
        self.result_detail.case_type = 1
        self.result_detail.schema_check = self.schema_result
        self.result_detail.save()
