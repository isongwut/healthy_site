from django.shortcuts import render
from django.http import HttpResponse
from healthy.models import Food

def home_page(request):
    name_foods = Food.objects.all()
    return render(request, 'home.html', {
        'new_food_text': request.POST.get('food_text', ''),
        'name_foods' : name_foods,
    })

    


