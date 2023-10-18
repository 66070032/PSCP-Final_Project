from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')
def food(request):
    return render(request, 'app_general/food.html')
def drinks(request):
    return render(request, 'app_general/drinks.html')
def yourdrinks(request):
    return render(request, 'app_general/yourdrinks.html')
def yourfood(request):
    return render(request, 'app_general/yourfood.html')