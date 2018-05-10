# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0005_auto_20180507_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='accesible',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
