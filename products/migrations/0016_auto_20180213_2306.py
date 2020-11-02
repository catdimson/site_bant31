# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_subscribers_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Телефон'),
        ),
    ]
