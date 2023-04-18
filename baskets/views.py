from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Basket, BasketItem
from products.models import Product

@login_required
def basket(request):
    try:
        basket = request.user.basket
    except Basket.DoesNotExist:
        basket = Basket.objects.create(user=request.user)
    return render(request, 'basket.html', {'basket': basket})

def add_to_basket(request, pk):
    basket = Basket.objects.get(user=request.user)
    product = Product.objects.get(pk=pk)
    try:
        item = basket.items.get(product=product)
        item.quantity += 1
        item.save()
    except BasketItem.DoesNotExist:
        item = BasketItem(basket=basket, product=product, quantity=1)
        item.save()
    return redirect('baskets:basket')

def delete_item(request, pk):
    item = BasketItem.objects.get(pk=pk)
    item.delete()
    return redirect('baskets:basket')