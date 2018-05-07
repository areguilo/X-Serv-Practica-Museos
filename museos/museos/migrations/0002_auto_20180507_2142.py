# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.TextField()),
                ('user', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('province', models.TextField()),
                ('postal_code', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Museo',
        ),
        migrations.DeleteModel(
            name='Pages',
        ),
        migrations.AddField(
            model_name='comment',
            name='museum',
            field=models.ForeignKey(to='museos.Museum'),
        ),
    ]
