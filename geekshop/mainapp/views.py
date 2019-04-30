from django.shortcuts import render
from .models import ProductCategory, Product, Content

def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

def products(request, pk=None):
    context = {'products': Product.objects.filter(category=pk)}
    #context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def categories(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/categories.html', context)


def productPage(request, pk = None, name=None):
    context = {'product': Product.objects.filter(category=pk).get(name=name)}
    return render(request, 'mainapp/product-page.html', context)


def cooperation(request):
    return render(request, 'mainapp/cooperation.html')


def about_us(request):
    return render(request, 'mainapp/about_us.html')


def content(request, name=None):
    print(name)
    context = {'cont': Content.objects.get(name=name)}
    return render(request, 'mainapp/content.html', context)