from django.urls import path,include
from .views import *
app_name = 'semi_auto'
urlpatterns = [
    path('',getIndex,name='index'),
    path('/get_data',sendData,name='send_data')
]