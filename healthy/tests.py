from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from healthy.views import home_page 
from django.template.loader import render_to_string
import re
from healthy.models import Food
 

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        expected_html = render_to_string('home.html')
        self.assertEqual(self.remove_csrf(response.content.decode()), self.remove_csrf(expected_html))
        self.assertTrue(response.content.startswith(b'<html>'))  
        self.assertIn(b'<title>healhty site</title>', response.content)  
        self.assertTrue(response.content.strip().endswith(b'</html>')) 

    
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['food_text'] = 'test'
        print('............................................')
        print(int(request.POST['food_text']))
        print('............................................')
        response = home_page(request)
        print(response.content.decode())
        self.assertIn('test', response.content.decode())
        expected_html = render_to_string(
                'home.html',
                 {'new_food_text':  'test'}
        )
        self.assertEqual(self.remove_csrf(response.content.decode()), self.remove_csrf(expected_html))

class FoodModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_food = Food()
        first_food.name = 'ข้าวผัด'
        first_food.calories = '500'
        first_food.number = 1
        first_food.select = True
        first_food.save()


        saved_items = Food.objects.all()
        self.assertEqual(saved_items.count(),1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.select, True)






