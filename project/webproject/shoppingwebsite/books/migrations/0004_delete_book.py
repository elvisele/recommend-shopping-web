# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_bookinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
