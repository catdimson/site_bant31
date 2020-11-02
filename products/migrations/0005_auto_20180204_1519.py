# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_subscriber'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='subscriber',
            table='Заявки по email',
        ),
    ]
