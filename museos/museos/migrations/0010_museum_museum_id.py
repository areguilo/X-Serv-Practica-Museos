# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0009_auto_20180510_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='museum_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
