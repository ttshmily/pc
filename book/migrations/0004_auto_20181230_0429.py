# Generated by Django 2.1.4 on 2018-12-30 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20181229_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinformation',
            old_name='title',
            new_name='book_title',
        ),
    ]