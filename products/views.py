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

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('product_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})
