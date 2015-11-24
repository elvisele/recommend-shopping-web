# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('isbn', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('yesr_publication', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_id', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=20)),
            ],
        ),
    ]
