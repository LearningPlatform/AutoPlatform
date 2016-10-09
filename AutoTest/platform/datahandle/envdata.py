# 处理环境相关的请求
"""
@author:liujing
"""

from django.core import serializers
import json

from ...models import Env


def getEnvList(data):
    try:
        pro_id = data['pro_id']
        body = []
        data = json.loads(serializers.serialize("json", Env.objects.all().filter(pro_id=pro_id)))
        for e in data:
            str1 = e['fields']
            str1['id'] = e['pk']
            body.append(str1)
        return {
            "code": 1,
            "msg": "获取环境列表成功",
            "data": body
        }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "参数错误"
        }
