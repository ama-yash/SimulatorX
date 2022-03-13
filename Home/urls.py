from django.urls import include, path

from .views import *

app_name = "Home"
urlpatterns = [path("", getIndex, name="index")]
