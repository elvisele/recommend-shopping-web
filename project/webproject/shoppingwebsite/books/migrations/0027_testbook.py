# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_delete_testbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('itemID', models.CharField(max_length=50)),
            ],
        ),
    ]
