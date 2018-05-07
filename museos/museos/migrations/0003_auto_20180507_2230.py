# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0002_auto_20180507_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=16)),
                ('background', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('size', models.IntegerField()),
                ('museum', models.ManyToManyField(to='museos.Museum')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='museos.User'),
        ),
    ]
