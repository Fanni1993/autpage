# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=50)),
                ('card_content', models.CharField(max_length=200)),
            ],
        ),
    ]
