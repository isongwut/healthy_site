from django.conf.urls import url

from . import views

app_name = 'healthy'
urlpatterns = [

    url(r'^$', views.home_page, name='home_page'), #  home_page

    url(r'^about$', views.about, name='about'),    #  about page
    
    url(r'^detail_food$', views.detail_food, name='detail_food'), #  detail_food page

    # select menu
    url(r'^select_menu_page$', views.select_menu_page, name='select_menu_page'), # none menu in foodlist
    
    url(r'^select_food$', views.select_food, name='select_food'),                # have menu in foodlist
    
    # BMR

    url(r'^bmr$', views.bmr, name='bmr'),             # bmr page receive value for calculate bmr

    url(r'^cal_bmr$', views.cal_bmr, name='cal_bmr'), # calculate bmr
    
    # exercise
    
    url(r'^cal_bmr/(?P<excess_calories>-?[0-9]+)/$', views.exercise, name='exercise'), # exercise page 

    url(r'^cal_bmr/(?P<excess_calories>-?[0-9]+)/burn/$', views.burn_calories, name='burn_calories'), # cal excess_calories for time burn

]
