from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Favorite

def products_view(request):
    products = Product.objects.all()

    return render(
        request,
        "products/products.html",
        {"products": products}
    )


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", {"form": form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:list')
    return render(request, {'product': product})

def favorites_view(request):
    favorite_ids = request.session.get('favorites', [])
    products = Product.objects.filter(id__in=favorite_ids)

    return render(request, 'products/favorites.html', {
        'products': products,
        'favorite_ids': favorite_ids,
    })


@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    fav, created = Favorite.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        fav.delete()

    return redirect(request.META.get("HTTP_REFERER", "/"))