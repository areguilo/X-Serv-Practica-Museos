# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0032_auto_20180519_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='background',
            field=models.CharField(default='#e99292', max_length=32),
        ),
    ]
