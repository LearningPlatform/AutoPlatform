from django.db import models


class Project(models.Model):
    """
    项目表
    """
    pro_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=100, null=True)
    pro_desc = models.TextField(null=True)


class Env(models.Model):
    """
    项目环境表
    """
    env_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    env_name = models.CharField(max_length=20, null=True)
    env_desc = models.TextField(null=True)


class Vars(models.Model):
    """
    全局变量基本信息表，保存变量名，类型，描述等共有信息
    """
    var_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    var_name = models.CharField(max_length=20, null=True)
    var_type = models.CharField(max_length=20, null=True)
    var_desc = models.TextField(null=True)


class VarValue(models.Model):
    """
    全局变量值表，每个值对应的项目，环境，变量id
    """
    pro_id = models.IntegerField(null=True)
    var_id = models.IntegerField(null=True)
    env_id = models.IntegerField(null=True)
    var_value = models.TextField(null=True)


class Module(models.Model):
    """
    项目模块表
    """
    module_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    module_name = models.CharField(max_length=20, null=True)
    module_desc = models.TextField(null=True)


class Api(models.Model):
    """
    项目接口信息表
    """
    api_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    module_id = models.IntegerField(null=True)
    api_name = models.CharField(max_length=20, null=True)
    api_protocol = models.CharField(max_length=10, null=True)
    api_method = models.CharField(max_length=10, null=True)
    api_url = models.CharField(max_length=50, null=True)
    api_type = models.CharField(max_length=20, null=True)
    api_desc = models.TextField(null=True)
    api_param = models.TextField(null=True)


class Case(models.Model):
    """
    项目用例表
    """
    case_id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=20, null=True)
    pro_id = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)
    module_id = models.IntegerField(null=True)
    input_data = models.TextField(null=True)
    exp_data = models.TextField(null=True)
    check_type = models.IntegerField(null=True)
    case_desc = models.TextField(null=True)
    is_set = models.IntegerField(null=True)
    depnd_api_id = models.IntegerField(null=True)
    case_schema = models.TextField(null=True)


class Suite(models.Model):
    """
    测试套件表
    """
    suite_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    suite_name = models.CharField(max_length=20, null=True)
    suite_desc = models.TextField(null=True)


class CaseSuite(models.Model):
    """
    测试套件表
    """
    case_suite_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    suite_id = models.IntegerField(null=True)
    case_id = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)
    case_type = models.IntegerField(null=True)


class Result(models.Model):
    """
    项目运行结果概述表
    """
    result_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    suite_id = models.IntegerField(null=True)
    pass_num = models.IntegerField(null=True)
    fail_num = models.IntegerField(null=True)
    start_time = models.IntegerField(null=True)
    end_time = models.IntegerField(null=True)
    report_name = models.CharField(max_length=30, null=True)


class ResultDetail(models.Model):
    """
    用例执行结果详情表
    """
    result_detail_id = models.AutoField(primary_key=True)
    result_id = models.IntegerField(null=True)
    case_id = models.IntegerField(null=True)
    case_type = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)
    input_data = models.TextField(null=True)
    out_data = models.TextField(null=True)
    exp_data = models.TextField(null=True)
    is_pass = models.IntegerField(null=True)
    schema_check = models.IntegerField(null=True)
    body_check = models.IntegerField(null=True)


class DepndApi(models.Model):
    """
    接口依赖，参数提取
    """
    depnd_api_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    depnd_api_name = models.CharField(max_length=20, null=True)
    depnd_api_protocol = models.CharField(max_length=10, null=True)
    depnd_api_method = models.CharField(max_length=10, null=True)
    depnd_api_url = models.CharField(max_length=50, null=True)
    depnd_api_type = models.CharField(max_length=20, null=True)
    depnd_api_desc = models.TextField(null=True)
    depnd_api_param = models.TextField(null=True)
    depnd_id = models.IntegerField(null=True)


class Functions(models.Model):
    """
    常用方法
    """
    func_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    func_name = models.CharField(max_length=30, null=True)
    func_code = models.TextField(null=True)
    func_desc = models.TextField(null=True)


class RecordCase(models.Model):
    """
    录制的case
    """
    case_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)
    module_id = models.IntegerField(null=True)
    case_protocol = models.CharField(max_length=5, null=True)
    case_url = models.TextField(null=True)
    case_method = models.TextField(null=True)
    case_header = models.TextField(null=True)
    input_data = models.TextField(null=True)
    exp_data = models.TextField(null=True)
    check_type = models.IntegerField(null=True)
    case_name = models.TextField(null=True)
    case_desc = models.TextField(null=True)
    depnd_api_id = models.IntegerField(null=True)
    resp_type = models.CharField(max_length=20, null=True)
    case_schema = models.TextField(null=True)


class CheckModel(models.Model):
    """
    验证器
    """
    check_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    check_name = models.CharField(max_length=20, null=True)
    check_code = models.TextField(null=True)
    check_desc = models.CharField(max_length=40, null=True)


class RunPlan(models.Model):
    """
    定时计划
    """
    plan_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(null=True)
    plan_name = models.TextField(null=True)
    plan_type = models.IntegerField(null=True)
    plan_interval = models.IntegerField(null=True)
    start_time = models.IntegerField(null=True)
    end_time = models.IntegerField(null=True)
    env_id = models.IntegerField(null=True)
    suite_id = models.IntegerField(null=True)
