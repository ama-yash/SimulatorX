from django.urls import include, path

from .views import *

app_name = "man_sim"
urlpatterns = [
    path("", getIndex, name="index"),
    path("/result", getResult, name="result"),
    path("/predict", predictInfection, name="pred"),
]
