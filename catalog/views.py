from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProductForm, ProductModeratorForm
from .models import Product, Category
from .services import ProductService


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        user = self.request.user
        return user == self.object.owner or user.has_perm('can_delete_product')


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class Category3ListView(ListView):
    model = Category
    template_name = "catalog/category_3_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = '3'
        context['product_list'] = ProductService.get_category_list(category_id)
        return context


class Category4ListView(ListView):
    model = Category
    template_name = "catalog/category_4_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = '4'
        context['product_list'] = ProductService.get_category_list(category_id)
        return context
