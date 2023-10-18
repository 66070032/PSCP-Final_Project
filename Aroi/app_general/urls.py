from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food', views.food, name='food'),
    path('drinks', views.drinks, name='drinks'),
    path('yourdrinks', views.yourdrinks, name='yourdrinks'),
    path('yourfood', views.yourfood, name='yourfood')
]