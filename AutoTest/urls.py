from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.to_index),
    url(r'project/list/$', views.pro_list),
    url(r'project/detail/$', views.pro_detail),
    url(r'project/create/$', views.pro_create),
    url(r'project/edit/$', views.pro_edit),
    url(r'project/delete/$', views.pro_del),
]