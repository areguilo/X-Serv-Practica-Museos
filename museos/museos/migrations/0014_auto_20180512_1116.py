# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0013_auto_20180511_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('museum', models.ForeignKey(to='museos.Museum')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=16)),
                ('background', models.CharField(max_length=32)),
                ('username', models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userrelation',
            name='museum',
        ),
        migrations.RemoveField(
            model_name='userrelation',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserRelation',
        ),
    ]
