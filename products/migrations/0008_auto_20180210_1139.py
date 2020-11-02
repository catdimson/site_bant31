# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seo_hidden_text_after_h2',
            field=models.TextField(null=True, default=None, blank=True, help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h2'),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_hidden_text_after_h3',
            field=models.TextField(null=True, default=None, blank=True, help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h3'),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_hidden_title_h2',
            field=models.TextField(null=True, default=None, blank=True, help_text='Скрытый текст! Данный текст будет помещен в заголовок h2 карточки товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_hidden_title_h3',
            field=models.TextField(null=True, default=None, blank=True, help_text='Скрытый текст! Данный текст будет помещен в заголовок h3 карточки товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_meta_desription',
            field=models.TextField(null=True, default=None, blank=True, help_text='Данный текст будет отображен в meta теге description, в качестве значения атрибута content. Это поле необходимо для SEO продвижения'),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_meta_keywords',
            field=models.TextField(null=True, default=None, blank=True, help_text='Данный текст будет отображен в meta теге keywords, в квчестве значения атрибута content. Это поле необъодимо для SEO продвижения'),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_title',
            field=models.TextField(null=True, default=None, blank=True, help_text='Данный текст будет помещен в значение тега title. Значение этого поля будет отобображено во вкладке браузера. Это поле необходисо для SEO продвижения'),
        ),
        migrations.AddField(
            model_name='product',
            name='text_blockquote',
            field=models.TextField(null=True, default=None, blank=True, help_text='Данный текст будет помещен в тег blockquote карточки товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_h1',
            field=models.TextField(null=True, default=None, blank=True, help_text='Данный текст будет помещен в заголовок h1 карточки товара. Если значение не указано, то заголовок будет браться из названия товара'),
        ),
    ]
