from django.urls import path
from .views import products_view, add_product, delete_product

app_name = "products"

urlpatterns = [
    path("", products_view, name="list"),
    path("add/", add_product, name='add_product'),
    path("delete/<int:pk>/", delete_product, name='delete_product'),
]
