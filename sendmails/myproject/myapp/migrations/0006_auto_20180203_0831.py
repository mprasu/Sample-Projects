# Generated by Django 2.0.2 on 2018-02-03 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180203_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserInfo'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
