import os, tempfile, sys, subprocess


TEMP = tempfile.mkdtemp(suffix='_py', prefix='auto_')
EXEC = sys.executable


def test():
    print("ok")


def run_code(func_name,func_code):
    r = dict()
    try:
        fpath = write_py(func_name,func_code)
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