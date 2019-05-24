from django.db import models
from mainapp.models import Product
from authapp.models import ShopUser


class BasketSlot(models.Model):
    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзина'

    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    user = models.ForeignKey(ShopUser, verbose_name='пользователь', on_delete=models.CASCADE, related_name='basket')
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)
    created = models.DateTimeField(verbose_name='создано', auto_now_add=True)

    def __str__(self):
        return self.user.username + '-' + self.product.name

@property
def product_cost(self):
    return self.product.price * self.quantity
    #
    # product_cost = property(get_product_cost)

@property
def total_quantity(self):
    "return total quantity for user"
    _items = BasketSlot.objects.filter(user=self.user)
    _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
    return _totalquantity

@property
def total_cost(self):
    "return total cost for user"
    _items = BasketSlot.objects.filter(user=self.user)
    _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
    return _totalcost
