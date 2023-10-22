from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food', views.food, name='food'),
    path('drinks', views.drinks, name='drinks'),
    path('signin', views.signin, name='signin')
]