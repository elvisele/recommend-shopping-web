# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_delete_userrecommend'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecommend',
            fields=[
                ('userid', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('item', models.TextField()),
            ],
        ),
    ]
