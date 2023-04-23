from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Basket, BasketItem
from products.models import Product
from django.http import JsonResponse


@login_required
def basket(request):
    try:
        basket = request.user.basket
    except Basket.DoesNotExist:
        basket = Basket.objects.create(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in basket.items.all())
    return render(request, 'basket.html', {'basket': basket, 'total_price': total_price})


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


@login_required
def increase_item(request, pk):
    item = BasketItem.objects.get(pk=pk)
    item.quantity += 1
    item.save()
    return JsonResponse({'status': 'success'})


@login_required
def decrease_item(request, pk):
    item = BasketItem.objects.get(pk=pk)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    return JsonResponse({'status': 'success'})
