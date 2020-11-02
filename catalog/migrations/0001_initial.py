# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=250, verbose_name='Вид цветов')),
                ('price', models.IntegerField(verbose_name='Цена одной штуки')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('in_stock', models.BooleanField(verbose_name='В наличии', default='True')),
            ],
            options={
                'verbose_name': 'Продукт',
                'db_table': 'Продукты',
                'verbose_name_plural': 'Все продукты',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Заявка',
                'db_table': 'Заявки по емэйл',
                'verbose_name_plural': 'Все заявки',
            },
        ),
    ]
