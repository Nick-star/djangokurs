from django.urls import path

from .views import basket, add_to_basket, delete_item, increase_item, decrease_item

app_name = 'baskets'

urlpatterns = [
    path('', basket, name='basket'),
    path('<int:pk>/add-to-basket/', add_to_basket, name='add_to_basket'),
    path('delete_item/<int:pk>/', delete_item, name='delete_item'),
    path('increase/<int:pk>/', increase_item, name='increase_item'),
    path('decrease/<int:pk>/', decrease_item, name='decrease_item'),
]
