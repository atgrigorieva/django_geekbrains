from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if basket:
        basket.quantity += 1
        basket.price_basket += product.price
        basket.save()
    else:
        basket = Basket(product=product, user=request.user)
        basket.quantity += 1
        basket.price_basket += product.price
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(product=product).first()

    if basket:
        if basket.quantity > 1:
            basket.quantity -= 1
            #print(basket.price_basket)
            basket.price_basket -= product.price
            basket.save()
        else:
            basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))