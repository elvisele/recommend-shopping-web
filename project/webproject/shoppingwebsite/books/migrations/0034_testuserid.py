# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0033_bookinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUserid',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
