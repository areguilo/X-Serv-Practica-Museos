# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0034_auto_20180520_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='size',
            field=models.CharField(max_length=3, default='15px'),
        ),
    ]
