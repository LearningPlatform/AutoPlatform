from ...models import RecordCase, ResultDetail

from .case import CaseEntity


class RcdCase(CaseEntity):

    rcd_case = object

    def __init__(self, case_id, var_map, result_id):
        CaseEntity.__init__(self)
        self.result_id = result_id
        self.result_detail = ResultDetail.objects.create(result_id=self.result_id)
        self.rcd_case = RecordCase.objects.all().get(case_id=case_id)
        self.url = self.rcd_case.case_protocol + "://" + self.rcd_case.case_url
        self.param = self.rcd_case.input_data
        self.depnd_api_id = self.rcd_case.depnd_api_id
        self.api_method = self.rcd_case.case_method
        self.var_map = var_map
        self.handle_depnd_param()
        self.pro_id = self.rcd_case.pro_id
        self.exp_data = self.rcd_case.exp_data
        self.resp_type = self.rcd_case.resp_type
        self.schema = self.rcd_case.case_schema

    def save_result(self):
        CaseEntity.save_result(self)
        input_data = {
            "url": self.url,
            "body": self.param
        }
        self.result_detail.case_id = self.rcd_case.case_id
        self.result_detail.exp_data = self.rcd_case.exp_data
        self.result_detail.case_desc = self.rcd_case.case_desc
        self.result_detail.api_id = self.rcd_case.api_id
        self.result_detail.input_data = input_data
        self.result_detail.out_data = self.resp
        self.result_detail.is_pass = self.is_pass
        self.result_detail.case_type = 2
        self.result_detail.schema_check = self.schema_result
        self.result_detail.save()

    def get_passnum(self):
        return self.is_pass
