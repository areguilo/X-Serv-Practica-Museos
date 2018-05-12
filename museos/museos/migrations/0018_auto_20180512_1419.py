# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0017_auto_20180512_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='museums',
        ),
        migrations.AddField(
            model_name='userdata',
            name='museums',
            field=models.OneToOneField(default=0, to='museos.Museum'),
            preserve_default=False,
        ),
    ]
