# a=[{'type': '字符串', 'value': 'liujing3@supernano.com', 'name': 'username'}, {'type': '字符串', 'value': '000000', 'name': 'pwd'}]
# b={}
# for i in  a:
#     b[i['name']]=i['value']
# print(b)
import requests
str = "{\"username\": \"liujing3@supernano.com\", \"pwd\": \"000000\"}"
a = requests.post("http://oa.supernano.com/index.php?r=api/login/login",str)
print(a)