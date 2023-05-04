from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm, RatingForm
from .models import Product, Category, Rating


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


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category = request.GET.get('category')
    if category:
        products = products.filter(category__name=category)
    sort = request.GET.get('sort')
    if sort == 'price-asc':
        products = products.order_by('price')
    elif sort == 'price-desc':
        products = products.order_by('-price')
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'index.html', {'products': products, 'categories': categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ratings = Rating.objects.filter(product=product)
    rating_form = RatingForm()

    avg_rating = ratings.aggregate(Avg('stars'))['stars__avg'] or 0
    avg_rating = round(avg_rating, 1)

    # Process the rating form submission
    if request.method == 'POST' and request.user.is_authenticated:
        form = RatingForm(request.POST)
        if form.is_valid():
            # Check if a rating already exists for the user and product
            existing_rating = Rating.objects.filter(user=request.user, product=product).first()

            if existing_rating:
                # Update the existing rating
                existing_rating.stars = form.cleaned_data['stars']
                existing_rating.save()
            else:
                # Save a new rating
                rating = form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()

            return redirect('products:product_detail', pk=product.pk)

    return render(request, 'product_detail.html',
                  {'product': product, 'ratings': ratings, 'rating_form': rating_form, 'avg_rating': avg_rating})

@login_required
@ staff_member_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products:product_detail', pk=pk)
    return render(request, 'update_product.html', {'form': form})


@login_required
@staff_member_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:index')
    return render(request, 'delete_product.html', {'product': product})
