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

    





