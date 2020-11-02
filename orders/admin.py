from django.contrib import admin
from .models import *


#для того, чтобы добавлять фотки из ТОВАРА
#всегда писать сверху!!!
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder #111
    extra = 0 #доп ряды для добавления фоток


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields] #вывести все поля
    inlines = [ProductInOrderInline]  # 111

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]  # вывести все поля

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]  # вывести все поля

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)