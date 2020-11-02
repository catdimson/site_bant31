from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^$', views.goods, name='goods'),
    url(r'^goods_flowers/', views.get_flowers, name='goods_flowers'),
    url(r'^goods_bolls/', views.get_bolls, name='goods_bolls'),
    url(r'^goods_baskets/', views.get_baskets, name='goods_baskets'),
    url(r'^goods_boxes/', views.get_boxes, name='goods_boxes'),
    url(r'^goods_additional/', views.get_additional, name='goods_additional'),
]