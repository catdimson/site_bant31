# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(default=None, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='price_rep_item',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
    ]
