# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_remove_person_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecommend',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('item', models.TextField()),
            ],
        ),
    ]
