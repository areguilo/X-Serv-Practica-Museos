# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0008_auto_20180510_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=32)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=16)),
                ('background', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='relation',
            name='museum',
        ),
        migrations.RenameField(
            model_name='museum',
            old_name='accesible',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='museum',
            old_name='mail',
            new_name='email',
        ),
        migrations.AddField(
            model_name='museum',
            name='accessibility',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='museos.User'),
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
        migrations.AddField(
            model_name='user',
            name='museum',
            field=models.ManyToManyField(to='museos.Museum'),
        ),
    ]
