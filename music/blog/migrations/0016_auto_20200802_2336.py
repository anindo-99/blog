# Generated by Django 3.0.7 on 2020-08-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200802_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
