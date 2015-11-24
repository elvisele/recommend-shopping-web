# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_bookinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='isbn',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
