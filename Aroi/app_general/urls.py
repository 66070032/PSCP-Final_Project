from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food', views.landing, name='food'),
    path('drinks', views.signin, name='drinks')
]