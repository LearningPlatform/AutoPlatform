from InterfaceTest.models import ProApi

class API:
    name = ""
    protocl = ""
    method = ""
    url = ""
    type = ""

    def __init__(self,id):
        api = ProApi.objects.all().get(id=id)
        self.name = api.api_name
        self.method = api.api_method
        self.protocl = api.api_protocol
        self.url = api.api_url
        self.type = api.api_type
