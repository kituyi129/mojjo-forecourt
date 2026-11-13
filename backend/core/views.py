from django.shortcuts import render , get_object_or_404
from .models import Products


# Display all products
def products(request):

    products= Products.objects.all()

    contexts = {
        "products": products,
    }
    return render(request, "index.html", contexts)


# Display individual product details
def products_details(request, slug):
    product = get_object_or_404(Products, Slug=slug)
    return render(request,"details.html", {"product":product})
    
        