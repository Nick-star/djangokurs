from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'add_product.html', context)


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)
