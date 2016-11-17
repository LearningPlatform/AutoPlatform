import os


def code_create(data):
    pro_id = data["pro_id"]
    code_name = data["code_name"]
    code_body = data["code_body"]
    if not os.path.exists("AutoTest/platform/customcode/code_"+str(pro_id)):
        os.mkdir("AutoTest/platform/customcode/code_"+str(pro_id))
    code_file = open("AutoTest/platform/customcode/code_"+str(pro_id)+"/"+code_name+".py", "w")
    code_file.write(code_body)
    code_file.close()