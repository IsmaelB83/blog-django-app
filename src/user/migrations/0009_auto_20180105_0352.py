# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 02:52
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0008_auto_20180105_0349'),
    ]
    
    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to=user.models.upload_location_author),
        ),
    ]
