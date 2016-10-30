from ...models import Case, CaseSuite, Api


class CaseEntity:

    def __init__(self, case_id):
        self.case_id = case_id
        self.case = object
        self.api = object
        self.setCase()
        self.selApi()

    def setCase(self):
        self.case = Case.objects.all().get(case_id=self.case_id)

    def selApi(self):
        self.api = Api.objects.all().get(api_id=self.case.api_id)

    def run(self):
        pass
