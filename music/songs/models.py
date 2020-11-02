from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Songpost(models.Model):
    sno = models.AutoField(primary_key=True)
    song_title = models.CharField(max_length=250)
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to='images')
    file = models.FileField(upload_to='musics')
    tags = models.CharField(max_length=500,default="")
    desc = models.TextField(max_length=2000,default="")
    plays = models.IntegerField(default=0)
    # sno = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    # slug = models.CharField(max_length=100)
    # content = models.TextField()
    # views = models.IntegerField(default=0)
    # timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.song_title + ' by ' + self.artist


# class Songuserpost(models.Model):
#     sno = models.AutoField(primary_key=True)
#     song_title = models.CharField(max_length=250)
#     artist = models.CharField(max_length=200)
#     album_title = models.CharField(max_length=300,default="")
#     genre = models.CharField(max_length=100,default="")
#     slug = models.CharField(max_length=100)
#     album_logo = models.ImageField(upload_to='images',default="")
#     music = models.FileField(upload_to='musics')
   
#     tag = models.CharField(max_length=100,default="")
#     desc = models.TextField(max_length=1000,default="")
#     def __str__(self):
#         return self.song_title + ' by ' + self.artist
