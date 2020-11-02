# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180210_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title_h1',
            field=models.TextField(help_text='Данный текст будет помещен в заголовок h1 карточки товара. Если значение не указано, то заголовок будет браться из названия товара', null=True, blank=True, verbose_name='Заголовок старицы', default=None),
        ),
    ]
