
from ..case.dapi import Interface


def test(data):
    test = Interface(1, {"host":"oa.supernano.com"})
    print(test.get_param_value("data.pro_name"))

    return {
        "msg": "test"
    }