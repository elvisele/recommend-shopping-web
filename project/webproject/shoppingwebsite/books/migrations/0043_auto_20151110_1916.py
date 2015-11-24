# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0042_shoppingcart_shoppinginfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppinginfo',
            old_name='userid',
            new_name='user',
        ),
    ]
