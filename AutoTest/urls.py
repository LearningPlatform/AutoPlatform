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


]