
from ..case.dapi import Interface


def test(data):
    pick_param = {}
    for i in [1,2]:
        test = Interface(i, {"host":"oa.supernano.com"})
        test.set_pick_param()
        pick_param = dict(pick_param,**test.get_pick_param())
    print(pick_param)
    return {
        "msg": "test"
    }