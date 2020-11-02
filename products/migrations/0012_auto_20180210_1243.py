# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20180210_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seo_meta_desription',
            new_name='seo_meta_description',
        ),
    ]
