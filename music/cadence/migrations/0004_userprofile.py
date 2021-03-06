# Generated by Django 3.0.7 on 2020-08-24 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('cadence', '0003_suserupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_pic', models.ImageField(default='default/user.png', upload_to='images')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
