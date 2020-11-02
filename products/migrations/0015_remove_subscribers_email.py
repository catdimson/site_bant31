# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_productimage_alt_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribers',
            name='email',
        ),
    ]
