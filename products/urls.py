from django.urls import path
from .views import products_view, add_product, delete_product, toggle_favorite, favorites_view

app_name = "products"

urlpatterns = [
    path("", products_view, name="list"),
    path("add/", add_product, name='add_product'),
    path("delete/<int:pk>/", delete_product, name='delete_product'),
    path('favorites/toggle/<int:product_id>/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', favorites_view, name='favorites'),
]
