# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-11 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180405_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='resume',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_src',
            field=models.IntegerField(choices=[(1, '微信授权用户'), (11, '游客用户'), (22, '普通用户'), (33, '机构用户')], db_index=True, default=11, help_text='用户来源', verbose_name='用户来源'),
        ),
    ]
