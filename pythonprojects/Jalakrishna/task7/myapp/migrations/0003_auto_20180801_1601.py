# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180727_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
