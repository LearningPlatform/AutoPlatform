
from ..case.dapi import Interface




def test(data):
    test = Interface(1 , {"host":"oa.supernano.com"})
    test.set_pick_param()
    print(test.get_pick_param())
    return {
        "msg": "test"
    }