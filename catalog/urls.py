from django.urls import path
from django.views.decorators.cache import cache_page

from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ProductTemplateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, Category3ListView, Category4ListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('home/', ProductListView.as_view(), name='product_list'),
    path('form/', ProductCreateView.as_view(), name='product_form'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('category_3_list/', Category3ListView.as_view(), name='category_3_list'),
    path('category_4_list/', Category4ListView.as_view(), name = 'category_4_list'),
]
