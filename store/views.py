from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request, 'store/index.html')


def cart(request):
    return render(request, 'store/cart.html')


def checkout(request):
    return render(request, 'store/checkout.html')


def detail(request):
    return render(request, 'store/detail.html')


def shop(request):
    return render(request, 'store/shop.html')


def test(request):
    return render(request, 'store/test.html')
