from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from healthy.models import Food,FoodList,Exercise


def home_page(request):
    FoodList.objects.all().delete()
    return render(request, 'healthy/home.html')

def about(request):
    return render(request, 'healthy/about.html')

def select_menu_page(request):
    contex = {'foods' : Food.objects.all(), 'foodList_select' : FoodList.objects.all(), 'calories_total' : sum_calories(FoodList.objects.all())}
    return render(request, 'healthy/select_food.html', contex)

def select_food(request):
    foods = Food.objects.all()
    calories_total = 0
    # clear
    if request.method == 'GET':
        FoodList.objects.all().delete()
        contex = {'foods' : Food.objects.all(), 'foodList_select' : FoodList.objects.all(), 'calories_total' : sum_calories(FoodList.objects.all())}
        return render(request, 'healthy/select_food.html', contex)

    # select 
    select = foods.get(name = request.POST.get('food'))
    food_texts = select.name
    number_food = request.POST.get('number_food')
    calories = select.calories * int(number_food)
    FoodList.objects.create(name = food_texts,number_per_menu = number_food , calories_per_menu = calories)
    
    # calories total
    calories_total = sum_calories(FoodList.objects.all())

    contex = {'foods' : foods, 'foodList_select' : FoodList.objects.all(), 'calories_total' : calories_total}
    return render(request, 'healthy/select_food.html', contex)

def bmr(request):
    return render(request, 'healthy/cal_bmr.html')

def exercise(request,excess_calories):
    contex = {'exercises' : Exercise.objects.all(),'excess_calories' : excess_calories}
    return render(request, 'healthy/exercise.html',contex)

def cal_bmr(request):
    bmr = 0
    calories_select_total = 0
    excess_calories = 0
    foods = Food.objects.all()
    exercises = Exercise.objects.all()

    # calories total
    calories_select_total = sum_calories(FoodList.objects.all())

    # cal bmr
    sex = request.POST.get('sex')
    height = int(request.POST.get('height'))
    weight = int(request.POST.get('weight'))
    age = int(request.POST.get('age'))
    if sex == 'Male' :
        bmr = int(66+((13.7*weight)+(5*height)-(6.8*age)))
    else:
        bmr = int(665+((9.6*weight)+(1.8*height)-(4.7*age)))

    # excess_calories
    excess_calories = calories_select_total-bmr

    if(excess_calories < 1):
        contex = { 'sex' : sex,'height' : height,'weight' : weight,'age' : age,'bmr_value' : bmr, 'excess_calories' : excess_calories, 'exercises' : exercises}
        return render(request, 'healthy/detail_bmr_less.html', contex)
    else:
        contex = { 'sex' : sex,'height' : height,'weight' : weight,'age' : age,'bmr_value' : bmr, 'excess_calories' : excess_calories, 'exercises' : exercises}
        return render(request, 'healthy/detail_bmr.html', contex)

def burn_calories(request,excess_calories):
    exercises = Exercise.objects.all()
    select = exercises.get(pk = request.POST.get('exercise'))
    contex = { 'exercises' : exercises,'exercise_select' : select, 'excess_calories' : excess_calories}
    return render(request, 'healthy/exercise.html', contex)


def sum_calories(foodList):
    calories_total = 0
    for food in foodList:
        calories_total += food.calories_per_menu
    return calories_total     


    
    

    


