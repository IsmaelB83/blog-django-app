# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('sort', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('css_class', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['sort'],
            },
        ),
    ]
