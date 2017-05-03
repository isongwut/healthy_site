from django.conf.urls import url

from . import views

app_name = 'healthy'
urlpatterns = [

    url(r'^$', views.home_page, name='home_page'),
    
    url(r'^select_food$', views.select_food, name='select_food'),

    url(r'^cal_bmr$', views.cal_bmr, name='cal_bmr'),

    url(r'^exercise$', views.burn_calories, name='exercise'),

]
