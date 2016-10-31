from ...models import Case, CaseSuite, Api
from ..tools import strtool


class CaseEntity:

    def __init__(self, case_id, var_map):
        self.case_id = case_id
        self.var_map = var_map
        self.url = ""
        self.param = ""
        self.case = object
        self.api = object
        self.setCase()
        self.selApi()
        self.setUrl()
        self.setReqParam()

    def setCase(self):
        self.case = Case.objects.all().get(case_id=self.case_id)

    def selApi(self):
        self.api = Api.objects.all().get(api_id=self.case.api_id)

    def setUrl(self):
        self.url = self.api.api_protocol + "://" + self.api.api_url
        while "{{" in self.url:
            self.url = strtool.str_replace(self.url, self.var_map)

    def setReqParam(self):
        self.param = self.case.input_data
        while "{{" in self.param:
            self.param = strtool.str_replace(self.param, self.var_map)
        print(self.param)

    def run(self):
        pass
