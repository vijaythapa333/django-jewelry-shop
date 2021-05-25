from store.models import Category, Product
from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.

def home(request):
    categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'store/index.html', context)


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.exclude(id=product.id).filter(is_active=True, category=product.category)
    context = {
        'product': product,
        'related_products': related_products,

    }
    return render(request, 'store/detail.html', context)


def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'store/categories.html', {'categories':categories})


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(is_active=True, category=category)
    categories = Category.objects.filter(is_active=True)
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/category_products.html', context)


# Authentication Starts Here


def register(request):
    form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def register_save(request):
    form = RegistrationForm(request.POST)
    # Error on Saving Data / Might need to use Class Based Views
    if form.is_valid():
        messages.success(request, 'Congratulations! Registration Successful!')
        form.save()
    return render(request, 'account/register.html', {'form': form})


def login(request):
    return render(request, 'account/login.html')


def add_to_cart(request):
    return render(request, 'store/cart.html')


def cart(request):
    return render(request, 'store/cart.html')


def checkout(request):
    return render(request, 'store/checkout.html')





def shop(request):
    return render(request, 'store/shop.html')





def test(request):
    return render(request, 'store/test.html')
