from django.urls import path,include
from .views import *
app_name = 'facial_recognition'
urlpatterns = [
    path('',uploadImages,name='up_im'),
    path('/predict',predictImage,name='pred')
]