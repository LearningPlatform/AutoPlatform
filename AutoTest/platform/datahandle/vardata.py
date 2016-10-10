# 处理全局变量相关的请求

from ...models import Vars, Project, VarValue
from ..tools import dbtool, jsontool


def create_vars(data):
    """
    创建变量
    :param data:
    :return:
    """
    try:
        pro_id = data['pro_id']
        var_name = data['var_name']
        var_desc = data['var_desc']
        var_type = data['var_type']
        var_value_list = data['var_value']
        pro_id_list = dbtool.getFieldList(Project, 'id')
        if pro_id in pro_id_list:
            if var_name == '':
                return {
                    "code": 0,
                    "msg": "变量名不能为空！"
                }
            if var_type == '':
                return {
                    "code": 0,
                    "msg": "变量类型不能为空！"
                }
            var_id = Vars.objects.create(pro_id=pro_id, var_name=var_name,
                                         var_desc=var_desc, var_type=var_type).id
            for var_value in var_value_list:
                env_id = var_value['env_id']
                value = var_value['value']
                VarValue.objects.create(pro_id=pro_id, env_id=env_id, var_value=value, var_id=var_id)
            return {
                "code": 1,
                "msg": "创建变量成功！"
            }
        else:
            return {
                    "code": 0,
                    "msg": "参数错误，项目id不存在！"
                }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "创建失败，参数错误！"
        }


def get_var_of_env(data):
    """
    获取环境下的所有变量
    :param data:
    :return:
    """
