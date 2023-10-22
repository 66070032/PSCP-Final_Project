from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')
def food(request):
    return render(request, 'app_general/food.html')
def drinks(request):
    return render(request, 'app_general/drinks.html')
def signin(request):
    return render(request, 'app_general/signin.html')
