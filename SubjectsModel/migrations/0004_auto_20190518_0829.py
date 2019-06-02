# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-18 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SubjectsModel', '0003_auto_20190518_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='degree',
            field=models.PositiveSmallIntegerField(verbose_name='0-easy;10-hard'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='exam_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SubjectsModel.Exam'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(choices=[(1, 'ADD'), (2, 'SUB'), (3, 'MUL'), (4, 'DIV'), (0, 'others')], default=0, max_length=1),
        ),
    ]