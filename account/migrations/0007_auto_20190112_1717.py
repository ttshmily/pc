# Generated by Django 2.1.4 on 2019-01-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20190112_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='用户账号'),
        ),
    ]
