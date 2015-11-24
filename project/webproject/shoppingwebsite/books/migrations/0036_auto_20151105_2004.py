# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0035_auto_20151105_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='useridnum',
            new_name='userid',
        ),
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
    ]
