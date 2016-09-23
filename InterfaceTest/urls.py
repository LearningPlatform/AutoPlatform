from django.conf.urls import url
from InterfaceTest import views


urlpatterns = [
    url(r'test/$', views.test),
    url(r'test1/$', views.test1),

    url(r'^$', views.to_index),
    url(r'pro_list/$', views.pro_get_all),
    url(r'pro_get/$', views.pro_get),
    url(r'pro_save/$', views.pro_save),
    url(r'pro_del/$', views.pro_del),
    url(r'env_save/$', views.env_save),
    url(r'env_del/$', views.env_del),
    url(r'env_list/$', views.env_get_all),
    url(r'env_varlist/$', views.pro_get_envVar),
    url(r'var_list/$', views.var_get_all),
    url(r'var_save/$', views.var_save),
    url(r'var_del/$', views.var_del),
    url(r'var_envlist/$', views.pro_get_varEvn),
    url(r'var_envListAll/$', views.pro_get_varEvn_all),

    url(r'model_save/$', views.model_save),
    url(r'model_list/$', views.model_get),

    url(r'suite_save/$', views.suite_save),
    url(r'suite_list/$', views.suite_get),

    url(r'api_save/$', views.api_save),
    url(r'api_listModel/$', views.api_get),
    url(r'api_listPro/$', views.api_get_all),

    url(r'case_saveInfo/$', views.case_info_save),
    url(r'case_listofApi/$', views.case_namelist_api),
    url(r'case_info/$', views.case_info),
    url(r'case_saveReq/$', views.case_req_save),

    url(r'run/$', views.run_case),

]