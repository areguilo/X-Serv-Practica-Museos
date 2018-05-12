# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0020_auto_20180512_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museum',
            name='museum_id',
        ),
    ]
