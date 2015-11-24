# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_bookinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
    ]
