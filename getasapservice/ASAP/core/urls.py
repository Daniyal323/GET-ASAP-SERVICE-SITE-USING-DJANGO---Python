from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('service/', product_list_view, name="service"),
    path('category/', category_list_view, name="category"),
    path('category-product/<cid>', category_product_list_view, name="category-product-list")
]