from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^accounts/$', views.accounts, name='accounts'),
    re_path(r'^views/$', views.views, name='views'),
    re_path(r'^subscribes/$', views.subscribes, name='subscribes'),
    ]