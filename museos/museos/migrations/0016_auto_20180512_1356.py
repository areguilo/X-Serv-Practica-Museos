# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0015_auto_20180512_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='museum',
            field=models.ForeignKey(default=0, to='museos.Museum'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='museos.UserData'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to='museos.UserData'),
        ),
    ]
