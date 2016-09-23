from django.db import models

class Project(models.Model):
    """
    项目表
    """
    pro_name = models.CharField(max_length=100, null=True)
    pro_desc = models.TextField(null=True)

class Env(models.Model):
    """
    项目环境表
    """
    pro_id = models.IntegerField(null=True)
    env_name = models.CharField(max_length=20, null=True)
    env_desc = models.TextField(null=True)

class Vars(models.Model):
    """
    全局变量基本信息表，保存变量名，类型，描述等共有信息
    """
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

class Model(models.Model):
    """
    项目模块表
    """
    pro_id = models.IntegerField(null=True)
    model_name = models.CharField(max_length=20, null=True)
    model_desc = models.TextField(null=True)

class Api(models.Model):
    """
    项目接口信息表
    """
    pro_id = models.IntegerField(null=True)
    model_id = models.IntegerField(null=True)
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
    case_name = models.CharField(max_length=20, null=True)
    pro_id = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)
    model_id = models.IntegerField(null=True)
    input_data = models.TextField(null=True)
    exp_data = models.TextField(null=True)
    check_type = models.IntegerField(null=True)
    case_desc = models.TextField(null=True)
    is_set = models.IntegerField(null=True)

class Suite(models.Model):
    """
    测试套件表
    """
    pro_id = models.IntegerField(null=True)
    suite_name = models.CharField(max_length=20, null=True)
    suite_desc = models.TextField(null=True)

class CaseSuite(models.Model):
    """
    测试套件表
    """
    pro_id = models.IntegerField(null=True)
    suite_id = models.IntegerField(null=True)
    case_id = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)

class Result(models.Model):
    """
    项目运行结果概述表
    """
    suite_id = models.IntegerField(null=True)
    opt_duration = models.IntegerField(null=True)
    pass_num = models.IntegerField(null=True)
    fail_num = models.IntegerField(null=True)
    apt_time = models.TimeField(null=True)

class ResultDetail(models.Model):
    """
    用例执行结果详情表
    """
    result_id = models.IntegerField(null=True)
    case_id = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)
    input_data = models.TextField(null=True)
    out_data = models.TextField(null=True)
    exp_data = models.TextField(null=True)
    is_pass = models.BooleanField()
    case_desc = models.TextField(null=True)