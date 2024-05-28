from django.urls import path
from .views import ListProductsView, DetailDeleteUpdateCreateView, ListCategoryView, DetailDeleteUpdateCreateCategoryView

urlpatterns = [
    path('list_products/', ListProductsView.as_view(), name='list_products'),
    path('products_all/<int:pk>', DetailDeleteUpdateCreateView.as_view(), name='products_all'),
    path('category_list/', ListCategoryView.as_view(), name='category_list'),
    path('category_all/<int:pk>', DetailDeleteUpdateCreateCategoryView.as_view(), name='category_all'),
]