from django.db import models
from products.models import Product
from django.db.models.signals import post_save


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Статус закаха'
        verbose_name_plural = 'Статусы заказа'

    def __str__(self):
        return 'Статус %s' % self.name


#Заказ
class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # как будет отображаться каждая заявка (ссылочка)
    def __str__(self):
        return 'Заказ %s %s' % (self.id, self.status.name)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


#Товар в заказе
class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_rep_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price_rep_item * nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # как будет отображаться каждая заявка (ссылочка)
    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item1 = self.product.price #положили в переменную цену 1 продукта
        self.price_per_item = price_per_item1    #поместили цену в заказ одного товара
        self.total_price = self.nmb * self.price_rep_item   #цена нескольких одиннаковых товаров

        super(ProductInOrder, self).save(*args, **kwargs)
        order = self.order
        all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

        order_total_price = 0
        for item in all_products_in_order:
            order_total_price += item.total_price

        self.order.total_price = order_total_price
        self.order.save(force_update=True)

###
#def product_in_order_post_save(sender, instance, created, **kwargs):
#    order = instance.order
#    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
#
#    order_total_price = 0
#    for item in all_products_in_order:
#        order_total_price += item.total_price
#
#    instance.order.total_price = order_total_price
#    instance.order.save(force_update=True)  # создать не новую запись , а перезаписать существующую
#
#функция срабатывает после сохранения, она импортирована. Есть так же post_save функция и прочие
#post_save.connect(product_in_order_post_save, sender=ProductInOrder)
####


    # 1)переопределение сохранения в БД
    # def save(self, *args, **kwargs):
    #     super(Order, self).save(*args, **kwargs)


    # 2)функция срабатывает после сохранения, она импортирована. Есть так же post_save функция и прочие
    # к функции обращаемся через instance (вместо self)
    # def product_in_order_post_save(sender, instance, created, **kwargs):
    # post_save.connect(product_in_order_post_save, sender=ProductInOrder)