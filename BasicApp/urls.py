from django.conf.urls import url
from BasicApp import views

app_name = 'BasicApp'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]
