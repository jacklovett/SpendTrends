# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='walletId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wallets.Wallet', verbose_name='Wallet'),
        ),
    ]
