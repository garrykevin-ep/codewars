from django.conf.urls import url

from . import views

app_name = 'quiz'

urlpatterns = [
    url(r'^(?P<test_id>[0-9]+)/(?P<pk>[0-9]+)/$',views.ans, name='ans'),
    url(r'^(?P<test_id>[0-9]+)/(?P<pk>[0-9]+)/disp/$',views.disp, name='display-question'),
    url(r'^(?P<test_id>[0-9]+)/create-status/',views.create_status, name = 'create-status'),
    url(r'^(?P<test_id>[0-9]+)/timer$',views.timer),   
]
