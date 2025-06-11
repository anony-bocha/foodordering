from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
def home(request):
    return render(request, 'products/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, product_slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
