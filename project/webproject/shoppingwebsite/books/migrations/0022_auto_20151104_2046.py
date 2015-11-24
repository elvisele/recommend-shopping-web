# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_userrecommend'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookinfo',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='UserRecommend',
        ),
    ]
