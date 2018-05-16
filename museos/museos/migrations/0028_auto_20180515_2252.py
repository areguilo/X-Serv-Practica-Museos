# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0027_auto_20180515_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='NUM',
            field=models.TextField(),
        ),
    ]
