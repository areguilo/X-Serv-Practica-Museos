# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0033_auto_20180520_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermuseum',
            old_name='museums',
            new_name='museum',
        ),
    ]
