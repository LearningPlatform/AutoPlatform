# 字符串处理工具
"""
@author:liujing
"""


def byteToStr(byte, encoding="utf-8"):
    """
    将字节转换为字符串，默认为utf-8
    :param byte: 字节流
    :param encoding: 编码格式
    :return: 编码后的字符串
    """
    return str(byte, encoding=encoding)


def str_replace(str1, var_map):
    a = str1.find('{{')
    b = str1.find('}}')
    str = str1[a + 2:b]
    str1 = str1.replace(str1[a:b + 2], var_map[str])
    print(str1)
    return str1
