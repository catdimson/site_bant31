# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180204_1519'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber',
            new_name='Subscribers',
        ),
        migrations.AlterModelTable(
            name='subscribers',
            table='Заявки по e_mail',
        ),
    ]
