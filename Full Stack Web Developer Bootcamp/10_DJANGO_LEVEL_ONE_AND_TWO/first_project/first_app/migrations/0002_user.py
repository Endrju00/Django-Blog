# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2021-06-10 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('second_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]