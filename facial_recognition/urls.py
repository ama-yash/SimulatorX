from django.urls import include, path

from .views import *

app_name = "facial_recognition"
urlpatterns = [
    path("", uploadImages, name="up_im"),
    path("predict", predictImage, name="pred"),
]
