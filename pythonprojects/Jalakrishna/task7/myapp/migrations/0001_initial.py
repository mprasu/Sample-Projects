# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Email_id', models.EmailField(max_length=80)),
                ('Password', models.CharField(max_length=20)),
                ('ConfirmPassword', models.CharField(max_length=20)),
                ('Phonenumber', models.IntegerField()),
                ('Location', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
