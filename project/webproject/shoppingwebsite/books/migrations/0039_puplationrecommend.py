# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0038_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuplationRecommend',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('itemid', models.CharField(max_length=50)),
            ],
        ),
    ]
