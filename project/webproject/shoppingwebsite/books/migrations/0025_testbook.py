# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_auto_20151104_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestBook',
            fields=[
                ('itemID', models.CharField(primary_key=True, serialize=False, max_length=50)),
            ],
        ),
    ]
