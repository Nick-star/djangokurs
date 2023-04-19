from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create-order/', views.create_order, name='create_order'),
    path('checkout-success/', views.checkout_success, name='checkout_success'),
    path('order-history/', views.order_history, name='order_history'),
]
