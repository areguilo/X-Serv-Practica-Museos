# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0030_auto_20180519_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermuseum',
            name='museums',
            field=models.ForeignKey(to='museos.Museum'),
        ),
    ]
