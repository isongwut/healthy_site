from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from healthy.models import Food,FoodList,Exercise
from django.shortcuts import get_object_or_404
from django import forms


def home_page(request):  		# home page
    FoodList.objects.all().delete()     # clear data in list menu
    return render(request, 'home.html') # render template home

def about(request):                      # about page 
    return render(request, 'about.html') # render template about

def detail_food(request):                              # detail food page 
    contex = {'foods' : Food.objects.all()}            # argument(food) of send to template
    return render(request, 'detail_food.html',contex)  # render template detail_food

def select_menu_page(request):                              # select_menu_page                     
    contex = {'foods' : Food.objects.all()}                 # argument(food) of send to template
    return render(request, 'select_food_page.html', contex) # render template select_food_page

def select_food(request):     # function select menu
    calories_total = 0        # set start value of calories_total
    
    # clear
    if request.method == 'GET':                 # when request method GET
        FoodList.objects.all().delete()         # clear data in list menu
        contex = {'foods' : Food.objects.all()} # argument(food) of send to template
        return redirect('/select_menu_page')    # redirect back to url /select_menu_page

    # select 
    try:
        select = Food.objects.get(name = request.POST.get('food')) # Get object menu from model Food
        number_food = request.POST.get('number_food')              # number of menu at select
    except (KeyError, Food.DoesNotExist):                          # error not select menu
        contex = {'foods' : Food.objects.all(), 'error_message' : 'Error : You may forget to enter the menu'}  # argument of send to template
        return render(request, 'select_food_page.html', contex) # render template select_food_page
    else:
        food_texts = select.name                                   # name menu at select
        calories = select.calories * int(number_food)              # calculate calories and number

        FoodList.objects.create(name = food_texts,number_per_menu = number_food , calories_per_menu = calories) # save nemu select to model FoodList(database)
    
        # calories total
        calories_total = sum_calories(FoodList.objects.all())      # calculate calories total from FoodList
     
        contex = {'foods' : Food.objects.all(), 'foodList_select' : FoodList.objects.all(), 'calories_total' : calories_total} # argument of send to template
        return render(request, 'select_food.html', contex)         # render template select_food for show table menu select

def sum_calories(foodList):      # function sum_calories for FoodList
    calories_total = 0       
    for food in foodList:        # for all data in FoodList
        calories_total += food.calories_per_menu   # sum calories
    return calories_total        # return value

def bmr(request):                              # bmr page
    return render(request, 'cal_bmr.html')     # render template cal_bmr for receive data calculate BMR
 
def cal_bmr(request):                   # function sum_calories for FoodList
    bmr = 0                             # set zero BMR value each one
    calories_select_total = 0           # set zero calories_select_total for select menu
    excess_calories = 0                 # set zero excess_calories for go to calculate burn_calories
    foods = Food.objects.all()          # all menu 
    exercises = Exercise.objects.all()  # all exercises

    # calories total
    calories_select_total = sum_calories(FoodList.objects.all()) # calculate calories total from FoodList

    # cal bmr
    try:
        sex = request.POST.get('sex')              # receive sex value from method post
        if(sex == None):        # none sex data
            return render(request, 'cal_bmr.html',{'error_message' : 'Error : You not entered sex data'}) # render template cal_bmr show error
        height = int(request.POST.get('height'))   # receive height int value from method post
        weight = int(request.POST.get('weight'))   # receive weight int value from method post
        age = int(request.POST.get('age'))         # receive age int value from method post
    except ValueError:         # on error
        return render(request, 'cal_bmr.html', {'error_message' : 'Error : You entered incomplete data'}) # render template cal_bmr show error
    else:
        if sex == 'Male' :                                       # case sex value = Male
            bmr = int(66+((13.7*weight)+(5*height)-(6.8*age)))   # calculate BMR value for male
        else:                                                    # case sex value = Female
            bmr = int(665+((9.6*weight)+(1.8*height)-(4.7*age))) # calculate BMR value for female

        # excess_calories
        excess_calories = calories_select_total-bmr     # excess_calories from difference calories_select_total-bmr

        if(excess_calories < 1):                                   # if excess_calories < 1
            contex = { 'sex' : sex,'height' : height,'weight' : weight,'age' : age,'bmr_value' : bmr, 'excess_calories' : excess_calories}
            return render(request, 'detail_bmr_less.html', contex) # render template detail_bmr_less 
        else:                                                      # if excess_calories >= 1 
            contex = { 'sex' : sex,'height' : height,'weight' : weight,'age' : age,'bmr_value' : bmr, 'excess_calories' : excess_calories}
            return render(request, 'detail_bmr.html', contex)      # render template detail_bmr 

def exercise(request,excess_calories):              # exercise page
    contex = {'exercises' : Exercise.objects.all(),'excess_calories' : excess_calories}  # argument of send to template
    return render(request, 'exercise.html',contex)  # render template exercise


def burn_calories(request,excess_calories):         # function burn_calories for check type exercise at select        
    exercises = Exercise.objects.all()              # all exercises
    select = exercises.get(pk = request.POST.get('exercise')) # type exercise at select
    contex = { 'exercises' : exercises,'exercise_select' : select, 'excess_calories' : excess_calories} # argument of send to template
    return render(request, 'exercise.html', contex) # render template exercise


   


    
    

    


