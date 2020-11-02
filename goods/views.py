from django.shortcuts import render
from products.models import * #Product и ProductImage
#from easy_thumbnails.files import get_thumbnailer

options = {'size': (100, 100), 'crop': True}

# Create your views here.


def get_flowers(request):

    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_after_filter = product_images.filter(product__category__id=1)
    # thumb_url = get_thumbnailer(product_images_after_filter.image).get_thumbnail(options).url

    return render(request, 'goods.html', locals())  # ф-ция locals() закидывает путь ко всем переменным


def get_bolls(request):

    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_after_filter = product_images.filter(product__category__id=2)

    return render(request, 'goods.html', locals())  # ф-ция locals() закидывает путь ко всем переменным


def get_boxes(request):

    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_after_filter = product_images.filter(product__category__id=3)

    return render(request, 'goods.html', locals())  # ф-ция locals() закидывает путь ко всем переменным


def get_baskets(request):

    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_after_filter = product_images.filter(product__category__id=4)

    return render(request, 'goods.html', locals())  # ф-ция locals() закидывает путь ко всем переменным


def get_additional(request):

    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_after_filter = product_images.filter(product__category__id=5)

    return render(request, 'goods.html', locals())  # ф-ция locals() закидывает путь ко всем переменным

