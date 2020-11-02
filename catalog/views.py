from django.shortcuts import render
from .forms import SubscrubersForm


def product(request):
    name = "Мы скоро откроемся"  # переменная
    current_date = '18.01.2018'
    form = SubscrubersForm(request.POST or None)
    # для принятия данных формой
    if request.method == "POST" and form.is_valid():  # определяем тип запроса, если POST то вывести форму чтобы django по умолчаню не заходила в нее,А только при отправке, тк работает с формой эта же вьюха, что и отображает шаблон
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']

        new_form = form.save()  # чтоб в админке добавилась

    return render(request, 'catalog.html', locals())

