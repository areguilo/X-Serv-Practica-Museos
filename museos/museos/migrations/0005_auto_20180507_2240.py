# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0004_museum_tlfn'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='fax',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museum',
            name='mail',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
