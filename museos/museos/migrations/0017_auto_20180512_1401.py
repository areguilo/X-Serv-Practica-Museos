# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0016_auto_20180512_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='museum',
        ),
        migrations.AddField(
            model_name='userdata',
            name='museums',
            field=models.ManyToManyField(to='museos.Museum'),
        ),
    ]
