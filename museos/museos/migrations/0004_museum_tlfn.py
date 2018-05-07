# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0003_auto_20180507_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='tlfn',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
