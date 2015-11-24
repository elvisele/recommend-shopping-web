# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0040_shoppingcart_shoppinginfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='books',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='shoppinginfo',
            name='books',
        ),
        migrations.RemoveField(
            model_name='shoppinginfo',
            name='userid',
        ),
        migrations.DeleteModel(
            name='Shoppingcart',
        ),
        migrations.DeleteModel(
            name='Shoppinginfo',
        ),
    ]
