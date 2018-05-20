# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0035_auto_20180520_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='size',
            field=models.CharField(default='12px', max_length=3),
        ),
    ]
