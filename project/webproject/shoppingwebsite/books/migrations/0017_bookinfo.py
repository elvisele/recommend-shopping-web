# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_delete_bookinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('isbn', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('yesr_publication', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
    ]
