from django.shortcuts import render
from .models import ProductCategory, Product, Content
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if sum(list(map(lambda basket: basket.quantity, basket))) == 0:
        quantity = 1
    else:
        quantity = sum(list(map(lambda basket: basket.quantity, basket)))
    print(basket[0])
    price_basket = sum(list(map(lambda basket: basket.price_basket, basket)))


    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
            'quantity': quantity,
            'price_basket': price_basket
        }

        return render(request, 'mainapp/products_list.html', content)


    '''Старый вариант кода'''
    #context = {'products': Product.objects.filter(category=pk)}
    # return render(request, 'mainapp/products.html', context)


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