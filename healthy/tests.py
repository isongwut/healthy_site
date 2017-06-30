from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from healthy.views import home_page 
from django.template.loader import render_to_string
import re
from healthy.models import Food,FoodList,Exercise
from healthy.views import home_page,about,detail_food,select_menu_page,select_food,bmr,exercise,cal_bmr,burn_calories,sum_calories
 
def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        expected_html = render_to_string('home.html')
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html))
        self.assertIn(b'<title>healhty site</title>', response.content)  

class SelectMenuTest(TestCase):

    def test_root_url_resolves_to_select_page_view(self):
        found = resolve('/select_food')  
        self.assertEqual(found.func, select_food)

    def test_saving_and_retrieving_items(self):
        first_menu = FoodList(name = 'ข้าวผัด',number_per_menu = 1,calories_per_menu = 557)
        first_menu.save()

        first_menu = FoodList(name = 'ขนมปังสังขยา',number_per_menu = 2,calories_per_menu = 460)
        first_menu.save()

        total_menu = FoodList.objects.all()
        self.assertEqual(total_menu.count(), 2)

        self.assertEqual(total_menu[0].name, 'ข้าวผัด') 
        self.assertEqual(total_menu[0].number_per_menu, 1)
        self.assertEqual(total_menu[0].calories_per_menu, 557)

        self.assertEqual(total_menu[1].name, 'ขนมปังสังขยา') 
        self.assertEqual(total_menu[1].number_per_menu, 2)
        self.assertEqual(total_menu[1].calories_per_menu, 460)

    def test_clear_items_after_GET(self):
        first_menu = FoodList(name = 'ข้าวผัด',number_per_menu = 1,calories_per_menu = 557)
        first_menu.save()

        total_menu = FoodList.objects.all()
        self.assertEqual(total_menu.count(), 1)

        self.assertEqual(total_menu[0].name, 'ข้าวผัด') 
        self.assertEqual(total_menu[0].number_per_menu, 1)
        self.assertEqual(total_menu[0].calories_per_menu, 557)
        
        request = HttpRequest()
        request.method = 'GET'

        response = select_food(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(total_menu.count(), 0)


class CalBMRTest(TestCase):

    def test_root_url_resolves_to_cal_bmr_page_view(self):
        found = resolve('/cal_bmr')  
        self.assertEqual(found.func, cal_bmr)

    def test_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['sex'] = 'Male'
        request.POST['height'] = 171
        request.POST['weight'] = 59
        request.POST['age'] = 21

        response = cal_bmr(request)


        contex = { 'sex' : request.POST['sex'],'height' : request.POST['height'],'weight' : request.POST['weight'],'age' : request.POST['age'],'bmr_value' : 1586, 'excess_calories' : -1586}
        expected_html = render_to_string('detail_bmr_less.html',contex)

        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html))
        self.assertEqual(response.status_code, 200)
        
    








