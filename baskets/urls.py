from django.urls import path

from .views import basket, add_to_basket, delete_item

app_name = 'baskets'

urlpatterns = [
    path('', basket, name='basket'),
    path('<int:pk>/add-to-basket/', add_to_basket, name='add_to_basket'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
]
