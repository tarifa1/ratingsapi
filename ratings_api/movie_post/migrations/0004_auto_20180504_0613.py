# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-04 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_post', '0003_auto_20180504_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='user_rating',
            new_name='rating',
        ),
    ]
