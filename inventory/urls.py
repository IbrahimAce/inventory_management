from django.urls import path
from .views import ProductListView, ProductCreateView, CategoryListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),  # home now shows product list
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]
