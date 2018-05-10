# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0007_auto_20180510_1316'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRelation',
            new_name='Relation',
        ),
    ]
