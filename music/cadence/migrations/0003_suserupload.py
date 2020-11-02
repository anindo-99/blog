# Generated by Django 3.0.7 on 2020-07-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadence', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suserupload',
            fields=[
                ('suserno', models.AutoField(primary_key=True, serialize=False)),
                ('images', models.ImageField(upload_to='images')),
                ('song', models.FileField(upload_to='songs')),
                ('stitle', models.CharField(max_length=100)),
                ('sdesc', models.TextField()),
            ],
        ),
    ]
