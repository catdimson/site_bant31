# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20180210_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, to='products.ProductCategory', verbose_name='Категория товара', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание, выводимое в карточке товара', default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(null=True, verbose_name='Цена товара со скидкой', default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(verbose_name='Активность', default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=200, verbose_name='Наименование товара', default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена товара без скидки', default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Количество', default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_hidden_text_after_h2',
            field=models.TextField(blank=True, help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h2', verbose_name='ТЭГ <p>. Скрытый текст, относящийся к <h2> (для SEO)', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_hidden_text_after_h3',
            field=models.TextField(blank=True, help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h3', verbose_name='ТЭГ <p>. Скрытый текст, относящийся к <h3> (для SEO)', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_hidden_title_h2',
            field=models.CharField(help_text='Скрытый текст! Данный текст будет помещен в заголовок h2 карточки товара', max_length=125, blank=True, verbose_name='ТЭГ <h2>. Скрытый заголовок (для SEO)', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_hidden_title_h3',
            field=models.CharField(help_text='Скрытый текст! Данный текст будет помещен в заголовок h3 карточки товара', max_length=125, blank=True, verbose_name='ТЭГ <h3>. Скрытый заголовок (для SEO)', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_meta_desription',
            field=models.CharField(help_text='Данный текст будет отображен в meta теге description, в качестве значения атрибута content. Это поле необходимо для SEO продвижения', max_length=225, blank=True, verbose_name='ТЭГ <meta description> (для SEO)', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_meta_keywords',
            field=models.CharField(help_text='Данный текст будет отображен в meta теге keywords, в квчестве значения атрибута content. Это поле необъодимо для SEO продвижения', max_length=225, blank=True, verbose_name='ТЭГ <meta keywords>', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_title',
            field=models.CharField(help_text='Данный текст будет помещен в значение тега title. Значение этого поля будет отобображено во вкладке браузера. Это поле необходисо для SEO продвижения', max_length=100, blank=True, verbose_name='ТЭГ <title>', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание, выводимое на странице категорий', default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='text_blockquote',
            field=models.TextField(blank=True, help_text='Данный текст будет помещен в тег blockquote карточки товара', verbose_name='ТЭГ <blockquote>. Скрытая цитата. (для SEO)', null=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_h1',
            field=models.TextField(blank=True, help_text='Данный текст будет помещен в заголовок h1 карточки товара. Если значение не указано, то заголовок будет браться из названия товара', verbose_name='Заголовок страницы', null=True, default=None),
        ),
    ]
