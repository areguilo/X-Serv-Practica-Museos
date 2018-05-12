# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0022_auto_20180512_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=32)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=16)),
                ('background', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserMuseum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('museums', models.OneToOneField(to='museos.Museum')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user')),
            ],
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='museums',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='museos.UserMuseum'),
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
        migrations.AddField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(to='museos.UserMuseum'),
        ),
    ]
