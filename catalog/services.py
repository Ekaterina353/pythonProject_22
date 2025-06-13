from django.core.cache import cache

from config.settings import CACHE_ENABLED
from .models import Category, Product


class ProductService:

    @staticmethod
    def get_category_list(category_id):
        product_list = Product.objects.filter(category=Category.objects.get(pk=category_id))
        return product_list


def get_products_from_cache():
    """Получает данные из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = 'product_list'
    product_list = cache.get(key)

    if product_list is not None:
        return product_list

    product_list = Product.objects.all()
    cache.set(key, product_list)
    return product_list
