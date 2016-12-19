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


