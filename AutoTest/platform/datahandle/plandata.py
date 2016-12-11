from . import rundata
from ...models import RunPlan
from ..tools import plantool,jsontool

import time


def get_plan_list(data):
    pro_id = data["pro_id"]
    body = []
    test = RunPlan.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_plan_detail(data):
    plan_id = data["pro_id"]
    data = RunPlan.objects.all().get(plan_id=plan_id)
    data_json = jsontool.convert_to_dict(data)
    del (data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def add_job(data, scheduler):
    plan_name = data["plan_name"]
    plan_type = data["plan_type"]
    plan_interval = data["plan_interval"]
    start_time = time.mktime(time.strptime(data["start_time"],'%Y-%m-%d %H:%M:%S'))
    end_time = time.mktime(time.strptime(data["end_time"],'%Y-%m-%d %H:%M:%S'))
    env_id = data["env_id"]
    suite_id = data["suite_id"]
    pro_id = data["pro_id"]
    scheduler_ob = RunPlan.objects.create(plan_name=plan_name, plan_type=plan_type, plan_interval=plan_interval,
                                          start_time=start_time, end_time=end_time, env_id=env_id, suite_id=suite_id,
                                          pro_id=pro_id)
    plantool.set_scheduler(scheduler,scheduler_ob)
    return {
        "code": 1,
        "msg": "添加完毕"
    }


def remove_job(data, scheduler):
    plan_id = data["plan_id"]
    RunPlan.objects.get(plan_id=plan_id).delete()
    sche = scheduler.get_job("plan_"+str(plan_id))
    if sche is None:
        pass
    else:
        scheduler.remove_job("plan_"+str(plan_id))
    return {
        "code": 1,
        "msg": "删除成功"
    }


def edit_plan(data, scheduler):
    plan_id = data["plan_id"]
    plan_name = data["plan_name"]
    plan_type = data["plan_type"]
    plan_interval = data["plan_interval"]
    start_time = time.mktime(time.strptime(data["start_time"], '%Y-%m-%d %H:%M:%S'))
    end_time = time.mktime(time.strptime(data["end_time"], '%Y-%m-%d %H:%M:%S'))
    RunPlan.objects.filter(plan_id=plan_id).update(
        plan_name=plan_name, plan_type=plan_type, plan_interval=plan_interval,start_time=start_time, end_time=end_time)
    scheduler_ob = RunPlan.objects.get(plan_id=plan_id)
    sche = scheduler.get_job("plan_" + str(plan_id))
    if sche is None:
        pass
    else:
        plantool.modify_scheduler(scheduler,scheduler_ob)
    return {
        "code": 1,
        "msg": "修改成功"
    }
