# Generated by Django 3.0.7 on 2020-07-09 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200709_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogupload',
            old_name='slug',
            new_name='bslug',
        ),
    ]
