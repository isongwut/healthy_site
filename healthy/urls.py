from django.conf.urls import url

from . import views

app_name = 'healthy'
urlpatterns = [

    url(r'^$', views.home_page, name='home_page'),
    
    url(r'^select_food/$', views.select_food, name='select_food'),

    #url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),

    #url(r'^(?P<topic_id>[0-9]+)/export_csv$', views.export_csv, name='export_csv'),

    #url(r'^(?P<topic_id>[0-9]+)/check_answers/$', views.check_answers, name='check_answers'),

    #url(r'^(?P<topic_id>[0-9]+)/check_answers/answer/$', views.answer, name='answer'),
]
