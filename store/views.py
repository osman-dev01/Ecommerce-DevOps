from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "store/home.html")

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})
