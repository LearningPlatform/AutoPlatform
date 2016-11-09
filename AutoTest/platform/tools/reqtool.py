import requests



def sendReq(type):
    if type == "post":
        return requests.post()