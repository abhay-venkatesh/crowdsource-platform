# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0111_remove_project_task_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='task_time',
            field=models.DurationField(null=True),
        ),
    ]
