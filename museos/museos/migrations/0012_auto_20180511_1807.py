# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0011_auto_20180511_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrelation',
            name='user',
        ),
        migrations.AddField(
            model_name='userrelation',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
