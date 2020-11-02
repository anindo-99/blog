# Generated by Django 3.0.7 on 2020-07-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogupload',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('btitle', models.CharField(max_length=100)),
                ('bauthor', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('bimages', models.ImageField(default='', upload_to='')),
                ('bcontent', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]