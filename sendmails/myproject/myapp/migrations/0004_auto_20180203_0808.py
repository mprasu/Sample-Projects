# Generated by Django 2.0.2 on 2018-02-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180203_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
