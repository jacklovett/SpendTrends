# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('isIncome', models.BooleanField(default=False, verbose_name='Income')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modifiedDate', models.DateTimeField(auto_now_add=True, verbose_name='Modified Date')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=13)),
                ('transactionDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Transaction Date')),
                ('comments', models.TextField(blank=True, null=True)),
                ('isPending', models.BooleanField(default=False, verbose_name='Pending Transaction')),
                ('isRecurring', models.BooleanField(default=False, verbose_name='Recurring Transaction')),
                ('isIncome', models.BooleanField(default=False, verbose_name='Income')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modifiedDate', models.DateTimeField(auto_now_add=True, verbose_name='Modified Date')),
                ('categoryId', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='transactions.Category', verbose_name='Category')),
            ],
        ), 
    ]
