# Generated by Django 2.1.4 on 2019-01-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190106_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='create_date',
            field=models.TimeField(verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_date',
            field=models.TimeField(verbose_name='最后登录日期'),
        ),
    ]