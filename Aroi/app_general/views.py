from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')
def landing(request):
    return render(request, 'app_general/food.html')
def signin(request):
    return render(request, 'app_general/drinks.html')