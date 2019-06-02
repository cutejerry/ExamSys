# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-18 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubjectsModel', '0005_auto_20190518_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='degree',
            field=models.PositiveSmallIntegerField(verbose_name='degree:\n0-easy;5-normal;10-hard'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'ADD'), (2, 'SUB'), (3, 'MUL'), (4, 'DIV'), (0, 'others')], default=0, max_length=1),
        ),
    ]
