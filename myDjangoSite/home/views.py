from django.shortcuts import render
from products.models import ProductImage

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_pizza = products_images.filter(product__category__id=1)
    products_images_bakery = products_images.filter(product__category__id=2)
    return render(request, 'home/home.html', locals())
