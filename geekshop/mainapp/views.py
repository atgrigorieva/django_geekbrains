from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import BasketSlot
import random

def main(request):
    return render(request, 'mainapp/index.html')

def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products

def products(request, pk=None):
    if pk or pk == 0:
        product_objects = Product.objects.all()
        if pk:
            get_object_or_404(ProductCategory, pk=pk)
            product_objects = Product.objects.filter(category=pk)
        context = {
            'categories': ProductCategory.objects.all(),
            'products': product_objects,
        }
        return render(request, 'mainapp/products.html', context)
    else:
        hot_product = get_hot_product()
        same_products = get_same_products(hot_product)


        context = {
            'categories': ProductCategory.objects.all(),
            'hot_product': hot_product,
            'same_products': same_products,
        }
        return render(request, 'mainapp/hot_product.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def common(request):
    return render(request, 'common/index.html')
