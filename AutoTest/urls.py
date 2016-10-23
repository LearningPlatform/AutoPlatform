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

    # 未写实体
    url(r'project/suite/list$', views.suite_list, name="获取套件列表"),
    url(r'project/suite/detail$', views.suite_detail, name="获取套件详情"),
    url(r'project/suite/create$', views.suite_create, name="创建套件"),
    url(r'project/suite/edit$', views.suite_edit, name="编辑修改套件"),
    url(r'project/suite/delete$', views.suite_del, name="删除套件"),
]