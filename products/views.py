from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import JsonResponse

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
    ids = request.session.get('favorites', [])
    products = Product.objects.filter(id__in=ids)

    return render(request, 'products/favorites.html', {
        'products': products
    })


def toggle_favorite(request, product_id):
    request.session.setdefault('favorites', [])
    favorites = request.session['favorites']

    if product_id in favorites:
        favorites.remove(product_id)
        is_favorite = False
    else:
        favorites.append(product_id)
        is_favorite = True

    request.session.modified = True

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'is_favorite': is_favorite})

    return redirect(request.META.get('HTTP_REFERER', '/'))