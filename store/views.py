from django.shortcuts import render
from .models import Product

def home(request):
    # Fetch top 3 products as featured
    featured_products = Product.objects.order_by('-stock')[:3]
    return render(request, "store/home.html", {"featured_products": featured_products})

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})
