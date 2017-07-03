from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from healthy.views import home_page 
from django.template.loader import render_to_string
import re
from healthy.models import Food,FoodList,Exercise
from healthy.views import home_page,about,detail_food,select_menu_page,select_food,bmr,exercise,cal_bmr,burn_calories,sum_calories
 
def remove_csrf(html_code):     # remove csrf from compared to template and response
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

class HomePageTest(TestCase):   # test home page

    def test_root_url_resolves_to_home_page_view(self): # test root url in system
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):      # test home page returns correct html
        request = HttpRequest()  
        response = home_page(request)                   # request go to home_page
        expected_html = render_to_string('home.html')   # render to string template home
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html)) # check template and response
        self.assertIn(b'<title>healhty site</title>', response.content)  # check title from response

class SelectMenuTest(TestCase): # test Select Menu

    def test_root_url_resolves_to_select_page_view(self): # test root url in system
        found = resolve('/select_food')  
        self.assertEqual(found.func, select_food)

    def test_saving_and_retrieving_items(self):         # test saving and retrieving items
        first_menu = FoodList(name = 'ข้าวผัด',number_per_menu = 1,calories_per_menu = 557)        # assign first menu
        first_menu.save()     # save first menu

        second_menu = FoodList(name = 'ขนมปังสังขยา',number_per_menu = 2,calories_per_menu = 460) # assign second menu
        second_menu.save()    # save second menu

        total_menu = FoodList.objects.all()            # call total selected menu to variable
        self.assertEqual(total_menu.count(), 2)        # check total selected menu = 2

        self.assertEqual(total_menu[0].name, 'ข้าวผัด')          # check name first menu = ข้าวผัด
        self.assertEqual(total_menu[0].number_per_menu, 1)      # check number_per_menu first menu = 1
        self.assertEqual(total_menu[0].calories_per_menu, 557)  # check calories_per_menu first menu = 557

        self.assertEqual(total_menu[1].name, 'ขนมปังสังขยา')    # check name first menu = ขนมปังสังขยา
        self.assertEqual(total_menu[1].number_per_menu, 2)      # check number_per_menu first menu = 2
        self.assertEqual(total_menu[1].calories_per_menu, 460)  # check calories_per_menu first menu = 460

    def test_clear_items_after_GET(self):             # test clear items after GET
        first_menu = FoodList(name = 'ข้าวผัด',number_per_menu = 1,calories_per_menu = 557) # assign first menu
        first_menu.save()      # save first menu

        total_menu = FoodList.objects.all()           # call total selected menu to variable
        self.assertEqual(total_menu.count(), 1)       # check total selected menu = 1

        self.assertEqual(total_menu[0].name, 'ข้าวผัด')          # check name first menu = ข้าวผัด
        self.assertEqual(total_menu[0].number_per_menu, 1)      # check number_per_menu first menu = 1
        self.assertEqual(total_menu[0].calories_per_menu, 557)  # check calories_per_menu first menu = 557
        
        request = HttpRequest()
        request.method = 'GET' # send request method GET

        response = select_food(request)               # request go to select_food

        self.assertEqual(response.status_code, 302)   # check return format redirec
        self.assertEqual(total_menu.count(), 0)       # check total selected menu after clear menu


class CalBMRTest(TestCase):   # Test Calculate BMR 

    def test_root_url_resolves_to_cal_bmr_page_view(self):  # test root url in system
        found = resolve('/cal_bmr')  
        self.assertEqual(found.func, cal_bmr)

    def test_POST_request(self):  # test request method POST send data to calculate BMR
        request = HttpRequest()
        request.method = 'POST'   # send request method GET
        request.POST['sex'] = 'Male' # send request method POST sex data
        request.POST['height'] = 171 # send request method POST height data
        request.POST['weight'] = 59  # send request method POST weight data
        request.POST['age'] = 21     # send request method POST age data

        response = cal_bmr(request)  # request go to cal_bmr

        contex = { 'sex' : request.POST['sex'],'height' : request.POST['height'],'weight' : request.POST['weight'],'age' : request.POST['age'],'bmr_value' : 1586, 'excess_calories' : -1586} # argument for template detail bmr
        expected_html = render_to_string('detail_bmr_less.html',contex)  # render to string template detail_bmr case don't selected menu

        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html)) # check template and response
        self.assertEqual(response.status_code, 200)    # check return format render
        
    








