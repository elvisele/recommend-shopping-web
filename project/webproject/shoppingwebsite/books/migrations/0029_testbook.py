# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0028_delete_testbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestBook',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('itemID', models.CharField(max_length=50)),
            ],
        ),
    ]
