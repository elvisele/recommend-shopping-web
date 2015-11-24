# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0039_puplationrecommend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoppingcart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('books', models.ForeignKey(to='books.Bookinfo')),
                ('userid', models.ForeignKey(to='books.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Shoppinginfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('books', models.ForeignKey(to='books.Bookinfo')),
                ('userid', models.ForeignKey(to='books.Person')),
            ],
        ),
    ]
