# 数据库处理工具
"""
@author:liujing
"""


def getFieldList(models, field='id'):
    """
    获取数据库中对应表的某一列
    :param models: 对应的的model
    :param field: 需要获取的列的名字，默认为id
    :return: 返回该字段的所有值，数据类型为list
    """
    return list(models.objects.values_list(field, flat=True))