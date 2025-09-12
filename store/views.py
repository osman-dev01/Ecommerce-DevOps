from django.shortcuts import render
from .models import Product

def home(request):
    # Fetch top 3 products as featured
    featured_products = Product.objects.order_by('-stock')[:3]
    return render(request, "store/home.html", {"featured_products": featured_products})

def about(request):
    return render(request, "store/about.html")

def contact(request):
    from .models import ContactMessage
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            success = True
    return render(request, "store/contact.html", {"success": success})

def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})
