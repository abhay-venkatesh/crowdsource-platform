# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-09 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0157_address_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='handle',
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
    ]
