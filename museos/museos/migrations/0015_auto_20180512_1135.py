# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0014_auto_20180512_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='username',
            new_name='user',
        ),
    ]
