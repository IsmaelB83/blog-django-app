# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [('posts', '0006_socialprofile'), ]

    operations = [migrations.AlterModelOptions(name='socialprofile', options={}, ),
        migrations.RemoveField(model_name='socialprofile', name='manually_edited', ),
        migrations.RemoveField(model_name='socialprofile', name='url', ),
        migrations.AddField(model_name='socialprofile', name='location', field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False, ), ]
