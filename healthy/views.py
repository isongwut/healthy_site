from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from healthy.models import Food,FoodList

def home_page(request):
    foods = Food.objects.all()
    return render(request, 'healthy/home.html', {
        'foods' : foods,
    })


def select_food(request):
    foods = Food.objects.all()
    calories_total = 0
    # clear
    if request.method == 'GET':
        FoodList.objects.all().delete()
        return render(request, 'healthy/home.html', {
        'foods' : foods,
        })
    # select 
    select = foods.get(pk = request.POST.get('food'))
    food_texts = select.name
    number_food = request.POST.get('number_food')
    calories = select.calories * int(number_food)
    FoodList.objects.create(name = food_texts,number = number_food, calories = calories )
    food_list = FoodList.objects.all()
    for i in FoodList.objects.all():
        calories_total += i.calories
    contex = {'foods' : foods, 'food_list' : food_list, 'calories_total' : calories_total}
    return render(request, 'healthy/select_food.html', contex)


    

    


