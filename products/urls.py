from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [
 # Home page.
 path('', views.index, name='index'),
 path('add-product/', views.add_product, name='add_product'),
 path('product/<int:pk>/', views.product_detail, name='product_detail'),
 path('product/<int:pk>/update/', views.update_product, name='update_product'),
 path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)