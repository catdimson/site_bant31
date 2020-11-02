from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):

    #list_display = ['name', 'email', 'phone'] #сам выбираешь, какие поля выводить в админке
    list_display = [field.name for field in Subscriber._meta.fields] #вывести все поля
    #field = [] #какие поля следует отобразить УЖЕ В САМОЙ ЗАЯВКЕ
    exclude = ['phone'] #какие поля следует скрыть УЖЕ В САМОЙ ЗАЯВКЕ
    list_filter = ('name', ) #Выбираем поле по которому фильтровать хотим
    search_fields = ['name', 'id'] #поля по которым фильтруем

    class Meta:
        model = Subscriber
        db_table = 'Интересненько'
# Register your models here.
admin.site.register(Product)
admin.site.register(Subscriber, SubscriberAdmin)