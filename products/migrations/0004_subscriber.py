# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180204_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Заявки по емэйл',
                'verbose_name_plural': 'Все заявки',
                'verbose_name': 'Заявка',
            },
        ),
    ]
