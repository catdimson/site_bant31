from django.contrib import admin
from .models import *


#для того, чтобы добавлять фотки из ТОВАРА
class ProductImageInline(admin.TabularInline):
    model = ProductImage #111
    extra = 0 #доп ряды для добавления фоток


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]  # вывести все поля


    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # вывести все поля
    inlines = [ProductImageInline] #111

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]  # вывести все поля

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)


class SubscribersAdmin(admin.ModelAdmin):

    #list_display = ['name', 'email', 'phone'] #сам выбираешь, какие поля выводить в админке
    list_display = [field.name for field in Subscribers._meta.fields] #вывести все поля
    field = ['*'] #какие поля следует отобразить УЖЕ В САМОЙ ЗАЯВКЕ
    #exclude = [''] #какие поля следует скрыть УЖЕ В САМОЙ ЗАЯВКЕ
    list_filter = ('name', ) #Выбираем поле по которому фильтровать хотим (фильтр справа)
    search_fields = ['name', 'phone', ] #поля по которым фильтруем (поля по тоторым будет работать поиск)

    class Meta:
        model = Subscribers
        db_table = 'Интересненько'
# Register your models here.
admin.site.register(Subscribers, SubscribersAdmin)