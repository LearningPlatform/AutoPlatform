import os, tempfile, sys, subprocess
from ...models import Functions


TEMP = tempfile.mkdtemp(suffix='_py', prefix='auto_')
EXEC = sys.executable


def test(func_id_list):
    write_code(func_id_list)
    print(get_return("get_md5_value",["000000"]))


def write_code(func_id_list):
    fpath = os.path.join(TEMP, '%s.py' % "func")
    func_file = open(fpath, 'w', encoding='utf-8', )
    for i in func_id_list:
        data = Functions.objects.all().get(func_id=i)
        func_file.write(data.func_code)
        func_file.write("\n\n")
    func_file.close()
    sys.path.append(TEMP)
    return fpath


def get_return(func_name, param):
    module = __import__("func", {}, {}, ['func'])
    func = getattr(module, func_name)
    len_param = len(param)
    if len_param == 0:
        return func()
    if len_param == 1:
        return func(param[0])
    if len_param == 2:
        return func(param[0],param[1])
    if len_param == 3:
        return func(param[0],param[1],param[2])
    if len_param == 4:
        return func(param[0],param[1],param[2],param[3])


def run_code(func_name,func_code):
    r = dict()
    try:
        fpath = write_py(func_name, func_code)
        r['output'] = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        r = dict(error='Exception', output=decode(e.output))
    except subprocess.TimeoutExpired as e:
        r = dict(error='Timeout', output='执行超时')
    except subprocess.CalledProcessError as e:
        r = dict(error='Error', output='执行错误')
    return r


def write_py(name, code):
    fpath = os.path.join(TEMP, '%s.py' % name)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    return fpath


def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')