# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0010_museum_museum_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=32)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=16)),
                ('background', models.CharField(max_length=32)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='museum',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='museum',
            name='accessibility',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userrelation',
            name='museum',
            field=models.ForeignKey(to='museos.Museum'),
        ),
        migrations.AddField(
            model_name='userrelation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
