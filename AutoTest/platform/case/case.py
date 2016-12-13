# from .dapi import Interface
# from ...models import CheckModel
# from .req import ReqResp
# from ..tools import strtool, functool
#
# import json
# from jsonschema import Draft4Validator
#
#
# class CaseEntity(ReqResp):
#
#     result_id = 0
#     result_detail = object
#     is_pass = 0
#     d_api = object
#     schema = {}
#     schema_result = 0
#     body_result = 0
#     check_type = 0
#
#     def __init__(self):
#         ReqResp.__init__(self)
#         pass
#
#     def handle_depnd_param(self):
#         while "$." in self.param:
#             path = strtool.str_replace(self.param, 2)
#             self.d_api = Interface(self.depnd_api_id, var_map=self.var_map)
#             self.d_api.run()
#             self.param = self.param.replace(path, str(self.d_api.get_param_value(path)))
#
#     def check_schema(self):
#         # 0-----未通过，1-----通过，2-----未检验
#         if self.schema != "" and self.schema != None:
#             self.schema = json.loads(self.schema)
#             self.schema_result = int(Draft4Validator(self.schema).is_valid(self.resp["response_data"]["body"]))
#         else:
#             self.schema_result = 2
#
#     def check_result(self):
#         if self.check_type == 0:
#             if json.dumps(self.resp["response_data"]["body"], ensure_ascii=False).find(self.exp_data) == -1:
#                 self.body_result = 0
#             else:
#                 self.body_result = 1
#         else:
#             check_name, check_code=self.setCheckCode()
#             result1 = functool.get_return(check_name,check_code)
#             if result1.find("True") !=-1:
#                 self.body_result = 1
#             else:
#                 self.body_result = 0
#
#     def save_result(self):
#         if self.resp_type != "json":
#             self.param = json.dumps(self.param)
#         self.param = json.loads(self.param)
#
#     def set_is_pass(self):
#         self.is_pass = self.schema_result and self.body_result
#
#     def get_is_pass(self):
#         return self.is_pass
#
#     def setCheckCode(self):
#         check_ob = CheckModel.objects.all().get(check_id=self.check_type)
#         check_name = check_ob.check_name
#         check_code = check_ob.check_code + '\nprint('+check_name+'(\"'+ str(self.resp["response_data"]["body"]) +'\",\"'+ self.exp_data + '\"))'
#         return check_name,check_code
