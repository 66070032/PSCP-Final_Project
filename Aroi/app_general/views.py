from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')
def food(request):
    return render(request, 'app_general/food.html')
def drinks(request):
    return render(request, 'app_general/drinks.html')
def randomfood(request):
    return render(request, 'app_general/randomfood.html')
def randomdrinks(request):
    return render(request, 'app_general/randomdrinks.html')

def random_food():
    print("Random Food Action")
    return HttpResponse("Button clicked successfully.")
