# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-12-02 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_fileupload_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='failed_phone_numbers_list',
            field=models.TextField(blank=True, null=True),
        ),
    ]
