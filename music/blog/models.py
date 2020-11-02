from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Post(models.Model):
    
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    slug = models.CharField(max_length=100)
    content = models.TextField()
    views = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return  self.title + ' by ' + self.author
# class Blogupload(models.Model):
#     blog_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     bslug = models.CharField(max_length=100)
#     images = models.ImageField(default='')
#     content = models.TextField()
#     views = models.IntegerField(default=0)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title + ' by ' + self.author


class Blogcomment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + "...." + " by " + self.user.first_name
    
