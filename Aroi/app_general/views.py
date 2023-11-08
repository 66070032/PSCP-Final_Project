from django.shortcuts import render
from django.http import HttpResponse
import random

import json

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def food(request):
    return render(request, 'app_general/food.html')

def drinks(request):
    return render(request, 'app_general/drinks.html')

def randomfood(request):
    print("Random Food Action")
    return render(request, 'app_general/randomfood.html')

def randomdrinks(request):
    return render(request, 'app_general/randomdrinks.html')

def random_food_action(request):
    json_data = open("app_general/static/data.json", "r", encoding="utf8")
    jsonData = json.load(json_data)

    shop_id = random.randint(0, len(jsonData))
    for i in jsonData[shop_id]:
        shop_name = i

    all_menu_price = jsonData[shop_id][shop_name]
    menu_id = random.randint(0, len(all_menu_price))
    for i in all_menu_price[menu_id]:
        menu_name = i
        menu_price = all_menu_price[menu_id][menu_name]

    print(shop_name, menu_name, menu_price)
    json_data.close()
    return render(request, 'app_general/randomfood.html')

def random_drinks_action(request):
    json_data2 = open("app_general/static/datadrinks.json", "r", encoding="utf8")
    jsonData2 = json.load(json_data2)

    shop_id2 = random.randint(0, len(jsonData2))
    for i in jsonData2[shop_id2]:
        shop_name2 = i

    all_menu_price = jsonData2[shop_id2][shop_name2]
    menu_id2 = random.randint(0, len(all_menu_price))
    for i in all_menu_price[menu_id2]:
        menu_name2 = i
        menu_price2 = all_menu_price[menu_id2][menu_name2]

    print(shop_name2, menu_name2, menu_price2)

    json_data2.close()
    return render(request, 'app_general/randomdrinks.html')