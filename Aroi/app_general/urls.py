from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food', views.food, name='food'),
    path('drinks', views.drinks, name='drinks'),
    path('randomfood', views.randomfood, name='randomfood'),
    path('randomdrinks', views.randomdrinks, name='randomdrinks'),
    path('random_food_action', views.random_food_action)
]