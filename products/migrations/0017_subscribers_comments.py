# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20180213_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='comments',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Комментарий к заказу'),
        ),
    ]
