# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0037_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('userid', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('location', models.CharField(max_length=100)),
                ('age', models.CharField(default='20', max_length=20)),
            ],
        ),
    ]
