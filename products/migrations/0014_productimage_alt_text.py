# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180210_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='alt_text',
            field=models.CharField(max_length=200, blank=True, verbose_name='Альтернативный текст для изображения. Он будет отображаться, если картинка не подгрузилась. Необходим для SEO оптимизации', null=True, default=None),
        ),
    ]
