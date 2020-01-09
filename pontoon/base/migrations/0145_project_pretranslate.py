# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0144_remove_userprofile_use_translate_next"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="pretranslation_enabled",
            field=models.BooleanField(
                default=False,
                help_text="\n        Pretranslate project strings using automated sources\n        like translation memory and machine translation.\n        ",
            ),
        ),
    ]