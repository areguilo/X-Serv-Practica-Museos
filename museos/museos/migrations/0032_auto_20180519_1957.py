# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0031_auto_20180519_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='size',
            field=models.CharField(max_length=3, default='9px'),
        ),
    ]
