# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 10:10
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('slug', models.CharField(default='', max_length=250)),
                ('description', models.CharField(default='', max_length=400)),
                ('create_by', models.CharField(default='', max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_by', models.CharField(default='', max_length=20)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
