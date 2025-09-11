from django.shortcuts import render
from .models import Product

def home(request):
    # Fetch top 8 products as featured (customize as needed)
    from .models import Product
    featured_products = Product.objects.order_by('-stock')[:8]
    return render(request, "store/home.html", {"featured_products": featured_products})

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})
