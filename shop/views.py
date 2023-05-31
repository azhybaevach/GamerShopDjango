from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()[:2]
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def product(request):
    prods = Product.objects.all()
    return render(request, 'product.html', {'products': prods})


def remot(request):
    return render(request, 'remot.html')


def video(request):
    return render(request, 'video.html')


def get_product(request, id):
    product_detail = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product_detail})


