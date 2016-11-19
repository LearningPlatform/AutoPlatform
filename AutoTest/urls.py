from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.to_index, name="渲染主页"),

    url(r'project/list$', views.pro_list, name="获取项目列表"),
    url(r'project/detail$', views.pro_detail, name="获取项目详情"),
    url(r'project/create$', views.pro_create, name="创建项目"),
    url(r'project/edit$', views.pro_edit, name="修改编辑项目"),
    url(r'project/delete$', views.pro_del, name="删除项目"),

    url(r'project/env/list$', views.env_list, name="获取环境列表"),
    url(r'project/env/detail$', views.env_detail, name="获取环境详情"),
    url(r'project/env/create$', views.env_create, name="创建环境"),
    url(r'project/env/edit$', views.env_edit, name="修改编辑环境"),
    url(r'project/env/delete$', views.env_del, name="删除环境"),
    url(r'project/env/varList$', views.env_var_list, name="获取特定环境下所有变量列表"),

    url(r'project/var/list$', views.var_list, name="获取变量列表"),
    url(r'project/var/detail$', views.var_detail, name="获取变量详情"),
    url(r'project/var/create$', views.var_create, name="创建变量"),
    url(r'project/var/edit$', views.var_edit, name="修改编辑变量"),
    url(r'project/var/delete$', views.var_del, name="删除变量"),

    url(r'project/module/list$', views.module_list, name="获取模块列表"),
    url(r'project/module/detail$', views.module_detail, name="获取模块详情"),
    url(r'project/module/create$', views.module_create, name="创建模块"),
    url(r'project/module/edit$', views.module_edit, name="编辑修改模块"),
    url(r'project/module/delete$', views.module_del, name="删除模块"),
    url(r'project/module/apiList$', views.module_api_list, name="获取模块下的接口列表"),
    url(r'project/module/caseList$', views.module_case_list, name="获取模块下的用例列表"),

    url(r'project/suite/list$', views.suite_list, name="获取套件列表"),
    url(r'project/suite/detail$', views.suite_detail, name="获取套件详情"),
    url(r'project/suite/create$', views.suite_create, name="创建套件"),
    url(r'project/suite/edit$', views.suite_edit, name="编辑修改套件"),
    url(r'project/suite/delete$', views.suite_del, name="删除套件"),
    url(r'project/suite/caseList$', views.suite_case_list, name="获取套件下的case列表"),

    url(r'project/api/list$', views.api_list, name="获取项目中的接口列表"),
    url(r'project/api/detail$', views.api_detail, name="获取接口详情"),
    url(r'project/api/create$', views.api_create, name="创建接口"),
    url(r'project/api/edit$', views.api_edit, name="编辑修改接口"),
    url(r'project/api/delete$', views.api_del, name="删除接口"),
    url(r'project/api/caseList$', views.api_case_list, name="获取接口下的case列表"),

    url(r'project/caseList$', views.case_list, name="获取项目中的case列表"),
    url(r'project/case/create$', views.case_create, name="创建case"),
    url(r'project/case/edit/info$', views.case_info_edit, name="编辑case的基本信息"),
    url(r'project/case/edit/req$', views.case_req_edit, name="编辑case的请求信息"),
    url(r'project/case/edit/resp$', views.case_resp_edit, name="编辑case的响应信息"),
    url(r'project/case/delete$', views.case_del, name="删除case"),

    url(r'project/case/run$', views.case_run, name="运行用例"),

    url(r'project/result/list$', views.result_list, name="获取项目的结果列表"),
    url(r'project/result/detailList$', views.result_detail_list, name="获取结果的详细信息列表"),
    url(r'project/result/caseDetail$', views.result_detail, name="获取单个用例运行结果的详细信息"),
    url(r'project/result/delete$', views.result_delete, name="删除结果"),

    url(r'project/dapi/list$', views.dapi_list, name="获取项目下的依赖接口列表"),
    url(r'project/dapi/detail$', views.dapi_detail, name="获取项目下的依赖接口列表"),
    url(r'project/dapi/create$', views.dapi_create, name="新建依赖接口"),
    url(r'project/dapi/edit$', views.dapi_edit, name="编辑依赖接口"),
    url(r'project/dapi/delete$', views.dapi_delete, name="编辑依赖接口"),


    url(r'project/func/create$', views.func_create, name="编辑依赖接口"),
    url(r'project/func/list$', views.func_list, name="编辑依赖接口"),
    url(r'project/func/detail$', views.func_detail, name="编辑依赖接口"),
    url(r'project/func/edit$', views.func_edit, name="编辑依赖接口"),
    url(r'project/func/delete$', views.func_delete, name="编辑依赖接口"),

]