from django.urls import path,include
from .views import *
app_name = 'covid19'
urlpatterns = [
    path('',getIndex,name='index'),
    path('/result',getResult,name='result'),
    path('/predict',predictInfection,name='predict')
]