# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-06-09 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchCourse', '0003_auto_20160609_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedata',
            name='course_video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
