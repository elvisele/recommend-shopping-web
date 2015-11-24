# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20151025_2319'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookinfo',
        ),
    ]
