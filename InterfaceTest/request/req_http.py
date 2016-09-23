import requests,json

def get():
    pass

def post(case):
    a = requests.post(case.protocol+"://"+case.url, json=json.loads(case.param))
    print(a.json())