# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-10-18 06:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20181018_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]