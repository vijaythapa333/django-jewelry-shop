from django.urls import path
from . import views


app_name = 'store'


urlpatterns = [
    path('', views.home, name="home"),
]
