from django.urls import path
from . import views


app_name = 'store'


urlpatterns = [
    path('', views.home, name="home"),
    path('product/detail/', views.detail, name="detail"),
    path('shop/', views.shop, name="shop"),

    path('product/test/', views.test, name="test"),

    path('product/cart/', views.cart, name="cart"),
    path('product/checkout/', views.checkout, name="checkout"),
]
