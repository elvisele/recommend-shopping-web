# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0030_delete_testbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestBook',
            fields=[
                ('itemID', models.CharField(primary_key=True, max_length=50, serialize=False)),
            ],
        ),
    ]
