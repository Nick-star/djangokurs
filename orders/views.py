from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from baskets.models import Basket
from .models import Order, OrderItem, ShippingAddress

@login_required
def checkout(request):
    basket = Basket.objects.get(user=request.user)
    items = basket.items.all()
    total_price = sum(item.product.price * item.quantity for item in items)
    return render(request, 'checkout.html', {'total_price': total_price})

@login_required
def create_order(request):
    if request.method == 'POST':
        basket = Basket.objects.get(user=request.user)
        items = basket.items.all()

        # Create Order
        order = Order(user=request.user)
        order.save()

        # Create OrderItems
        for item in items:
            order_item = OrderItem(order=order, product=item.product, quantity=item.quantity)
            order_item.save()

        # Create ShippingAddress
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address_line1 = request.POST.get('address_line1')
        address_line2 = request.POST.get('address_line2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')

        shipping_address = ShippingAddress(order=order, first_name=first_name, last_name=last_name,
                                           address_line1=address_line1, address_line2=address_line2,
                                           city=city, state=state, postal_code=postal_code, country=country)
        shipping_address.save()

        # Empty the Basket
        items.delete()

        return redirect('orders:checkout_success')

    return redirect('orders:checkout')

@login_required
def checkout_success(request):
    return render(request, 'checkout_success.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.orderitem_set.all()
    return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})