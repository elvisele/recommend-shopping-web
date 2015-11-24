# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0043_auto_20151110_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='userid',
            new_name='user',
        ),
    ]
