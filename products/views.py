from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

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

