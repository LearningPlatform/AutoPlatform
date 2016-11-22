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
    # 替换全局变量
    if str_type == 1:
        a = str_re.find('{{')
        b = str_re.find('}}')
        str1 = str_re[a + 2:b]
        return a, b+2, str1
    # 替换依赖接口值
    if str_type == 2:
        a = str_re.find('$.')
        b_list = [str_re.find('"', a), str_re.find(',', a), str_re.find('}', a), str_re.find('\'', a)]
        b = len(str_re)
        for i in b_list:
            if 0 < i < b:
                b = i
        path = str_re[a:b]
        return path
    # 替换常用方法返回值
    if str_type == 3:
        a = str_re.find('{$')
        b = str_re.find('$}')
        str1 = str_re[a + 2:b]
        str_func_name = str1[0:str1.find('(')]
        return a, b + 2, str1, str_func_name
    # if str_type == 4:
    #     a = str_re.find('{$')
    #     b = str_re.find('$}')
    #     str1 = str_re[a + 2:b]
    #     str_func_name = str1[0:str1.find('(')]
    #     str_func_param = str1[str1.find('(') + 1:-1].split(',')
    #     for index, param in enumerate(str_func_param):
    #         if param.find("\'") != -1 or param.find("\"") != -1:
    #             str_func_param[index] = str_func_param[index][1:-1]
    #         else:
    #             if param.find('.') != -1:
    #                 str_func_param[index] = float(param)
    #             else:
    #                 str_func_param[index] = int(param)
    #     return a, b + 2, str_func_name, str_func_param


