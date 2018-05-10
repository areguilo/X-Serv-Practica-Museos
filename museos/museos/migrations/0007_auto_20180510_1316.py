# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0006_museum_accesible'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=16)),
                ('background', models.CharField(max_length=32)),
                ('museum', models.ManyToManyField(to='museos.Museum')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='museum',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='museos.UserRelation'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
