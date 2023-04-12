from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


@login_required
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


@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products:product_detail', pk=pk)
    return render(request, 'update_product.html', {'form': form})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:index')
    return render(request, 'delete_product.html', {'product': product})
