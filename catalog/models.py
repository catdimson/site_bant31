from django.db import models

# Create your models here.

# Товар
class Product(models.Model):
    class Meta():
        db_table = 'Продукты'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Все продукты'

    product_name = models.CharField(max_length=250, verbose_name='Вид цветов')
    price = models.IntegerField(verbose_name='Цена одной штуки')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    quantity = models.IntegerField(verbose_name='Количество')
    in_stock = models.BooleanField(default='True', verbose_name='В наличии')

# Подписчики
class Subscriber(models.Model):
    class Meta():
        db_table = 'Заявки по емэйл'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Все заявки'

    email = models.EmailField()
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)

#как будет отображаться каждая заявка ()
    def __str__(self):
        return self.email