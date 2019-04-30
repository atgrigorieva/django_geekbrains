from django.db import models
from ckeditor.fields import RichTextField

class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    name = models.CharField(verbose_name='имя', max_length=255, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    short_desc = models.TextField(verbose_name='краткое описание продукта', blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    #descriptionHTML = RichTextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def get_absolute_url(self):
        return '/products/%i/%s'%(self.category_id, self.name)

    def __str__(self):
        return self.name + ' (' + self.category.name + ')'


class Content(models.Model):
    class Meta:
        verbose_name = 'Страницы контента'
        verbose_name_plural = 'Контент'
    name = models.CharField(verbose_name='имя', max_length=255, unique=True)
    description = RichTextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='content_images', blank=True)

    def __str__(self):
        return self.name