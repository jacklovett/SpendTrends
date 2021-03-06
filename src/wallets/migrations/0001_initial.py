# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('currency', models.CharField(max_length=10)),
                ('initialBalance', models.DecimalField(decimal_places=2, default=0.0, max_digits=13, verbose_name='Initial Balance')),
                ('currentBalance', models.DecimalField(decimal_places=2, default=0.0, max_digits=13, verbose_name='Current Balance')),
                ('isActive', models.BooleanField(default=False, verbose_name='Active')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modifiedDate', models.DateTimeField(auto_now_add=True, verbose_name='Modified Date')),
            ],
        ),
    ]
