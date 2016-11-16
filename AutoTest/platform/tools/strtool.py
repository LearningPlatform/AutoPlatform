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


def str_replace(str_re, str_type):
    if str_type == 1:
        a = str_re.find('{{')
        b = str_re.find('}}')
        str1 = str_re[a + 2:b]
        return a, b+2, str1
    if str_type == 2:
        a = str_re.find('$.')
        b_list = [str_re.find('"', a), str_re.find(',', a), str_re.find('}', a), str_re.find('\'', a)]
        b = len(str_re)
        for i in b_list:
            if 0 < i < b:
                b = i
        path = str_re[a:b]
        return path


