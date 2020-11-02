# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180210_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seo_hidden_title_h2',
            field=models.CharField(null=True, max_length=125, default=None, help_text='Скрытый текст! Данный текст будет помещен в заголовок h2 карточки товара', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_hidden_title_h3',
            field=models.CharField(null=True, max_length=125, default=None, help_text='Скрытый текст! Данный текст будет помещен в заголовок h3 карточки товара', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_meta_desription',
            field=models.CharField(null=True, max_length=225, default=None, help_text='Данный текст будет отображен в meta теге description, в качестве значения атрибута content. Это поле необходимо для SEO продвижения', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_meta_keywords',
            field=models.CharField(null=True, max_length=225, default=None, help_text='Данный текст будет отображен в meta теге keywords, в квчестве значения атрибута content. Это поле необъодимо для SEO продвижения', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_title',
            field=models.CharField(null=True, max_length=100, default=None, help_text='Данный текст будет помещен в значение тега title. Значение этого поля будет отобображено во вкладке браузера. Это поле необходисо для SEO продвижения', blank=True),
        ),
    ]
