# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_delete_bookinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('isbn', models.CharField(max_length=50)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('yesr_publication', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
    ]
