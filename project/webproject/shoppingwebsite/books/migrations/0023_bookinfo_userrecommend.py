# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_auto_20151104_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('isbn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('yesr_publication', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserRecommend',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('item', models.TextField()),
            ],
        ),
    ]
