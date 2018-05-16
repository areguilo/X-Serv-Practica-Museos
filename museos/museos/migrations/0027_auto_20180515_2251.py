# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0026_auto_20180515_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museum',
            old_name='PK',
            new_name='ID_ENTIDAD',
        ),
    ]
