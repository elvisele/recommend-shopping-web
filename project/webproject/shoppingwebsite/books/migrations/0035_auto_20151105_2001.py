# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0034_testuserid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestBook',
        ),
        migrations.DeleteModel(
            name='TestUserid',
        ),
    ]
