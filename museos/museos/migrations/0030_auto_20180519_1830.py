# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0029_auto_20180516_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='color',
        ),
        migrations.AlterField(
            model_name='preference',
            name='background',
            field=models.CharField(max_length=32, default='green'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='size',
            field=models.IntegerField(default=9),
        ),
    ]
