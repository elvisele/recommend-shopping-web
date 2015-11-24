# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0023_bookinfo_userrecommend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('useridnum', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='image_url',
        ),
    ]
