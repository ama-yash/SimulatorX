from django.urls import include, path

from .views import *

app_name = "covid19"
urlpatterns = [
    path("", getIndex, name="index"),
    path("/result", getResult, name="result"),
    path("/predict", predictInfection, name="predict"),
]
