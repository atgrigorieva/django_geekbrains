from django.urls import path
import mainapp.views as mainapp
from django.conf.urls import include, url

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('products/<int:id>/<str:name>',  mainapp.productPage, name='productPage'),
    #url(r'^products/(?P<pk>\d+)/$', mainapp.products, name='products'),


]
