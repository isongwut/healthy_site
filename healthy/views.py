from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html', {
        'new_food_text': request.POST.get('food_text', ''),
    })

def save_select_food(request):
    return render(request, 'home.html')


