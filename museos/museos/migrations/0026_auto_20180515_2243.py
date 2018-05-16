# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0025_auto_20180515_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='ACCESIBILIDAD',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='CODIGO_POSTAL',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='COORDENADA_X',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='COORDENADA_Y',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='EMAIL',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='FAX',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='LATITUD',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='LOCALIDAD',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='LONGITUD',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='PK',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='museum',
            name='TELEFONO',
            field=models.TextField(),
        ),
    ]
