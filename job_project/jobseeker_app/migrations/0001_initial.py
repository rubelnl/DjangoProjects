# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobpost_app', '0006_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekerReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('gender', models.IntegerField(max_length=1)),
                ('mobile', models.CharField(default='', max_length=14)),
                ('email', models.CharField(default='', max_length=200)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pass', models.CharField(max_length=20)),
                ('create_by', models.CharField(default='', max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_by', models.CharField(default='', max_length=20)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('industry', models.ManyToManyField(to='jobpost_app.Industry')),
            ],
        ),
    ]
