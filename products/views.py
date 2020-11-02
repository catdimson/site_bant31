from django.shortcuts import render
from products.models import *
from .forms import SubscrubersForm

from django.core.mail import send_mail
from cms_site_bant31 import settings


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    form = SubscrubersForm(request.POST or None)
    # для принятия данных формой
    if request.method == "POST":
        if form.is_valid():  # определяем тип запроса, если POST то вывести форму чтобы django по умолчаню не заходила в нее,А только при отправке, тк работает с формой эта же вьюха, что и отображает шаблон
            id_good = product.id
            name_good = product.name
            price_good = product.price

            data = form.cleaned_data
            name = form.cleaned_data['name']
            phone = data['phone']
            comments = form.cleaned_data['comments']

            body = 'Имя: {}, \nНомер телефона: {}, \nКомментарий к заказу: {}. \n\nИдентификатор товара: {}, \nНазвание товара: {}, \nЦена товара: {}.'.format(name, phone, comments, id_good, name_good, price_good)

            new_form = form.save()  # чтоб в админке добавилась
            send_mail('Вам заявка', body, settings.EMAIL_HOST_USER, [settings.EMAIL_TO])

            return render(request, 'others/thanks.html')
    else:

        return render(request, 'products/product.html', locals())

