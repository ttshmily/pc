# Generated by Django 2.1.4 on 2018-12-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20181229_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinformation',
            name='book_cover',
            field=models.ImageField(null=True, upload_to='book_cover', verbose_name='封面'),
        ),
    ]