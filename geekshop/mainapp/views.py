from django.shortcuts import render
from .models import ProductCategory, Product

def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

def products(request, pk=None):
    filter = {'products': Product.objects.filter(category=pk)}
    #context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', filter)


def categories(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/categories.html', context)


def productPage(request, name=None):
    filter = {'product': Product.objects.filter(name=name)}
    return render(request, 'mainapp/product-page.html', filter)


def cooperation(request):
    return render(request, 'mainapp/cooperation.html')


def about_us(request):
    return render(request, 'mainapp/about_us.html')