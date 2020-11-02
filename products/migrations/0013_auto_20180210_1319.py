# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20180210_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_h1',
            field=models.TextField(help_text='Данный текст будет помещен в заголовок h1 карточки товара. Если значение не указано, то заголовок будет браться из названия товара', blank=True, default=None, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_seo_hidden_text_after_h2',
            field=models.TextField(help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h2', blank=True, default=None, null=True, verbose_name='ТЭГ <p>. Скрытый текст, относящийся к <h2> (для SEO)'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_seo_hidden_title_h2',
            field=models.CharField(max_length=125, default=None, help_text='Скрытый текст! Данный текст будет помещен в заголовок h2 карточки товара', verbose_name='ТЭГ <h2>. Скрытый заголовок (для SEO)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_seo_meta_description',
            field=models.CharField(max_length=225, default=None, help_text='Данный текст будет отображен в meta теге description, в качестве значения атрибута content. Это поле необходимо для SEO продвижения', verbose_name='ТЭГ <meta description> (для SEO)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_seo_meta_keywords',
            field=models.CharField(max_length=225, default=None, help_text='Данный текст будет отображен в meta теге keywords, в квчестве значения атрибута content. Это поле необъодимо для SEO продвижения', verbose_name='ТЭГ <meta keywords>', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_seo_title',
            field=models.CharField(max_length=100, default=None, help_text='Данный текст будет помещен в значение тега title. Значение этого поля будет отобображено во вкладке браузера. Это поле необходисо для SEO продвижения', verbose_name='ТЭГ <title>', blank=True, null=True),
        ),
    ]
