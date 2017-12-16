# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-16 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20171216_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('pj_number',)},
        ),
    ]
