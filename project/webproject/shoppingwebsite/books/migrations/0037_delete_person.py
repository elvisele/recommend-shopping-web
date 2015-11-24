# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0036_auto_20151105_2004'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
