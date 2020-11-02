from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' + self.first_name + '-' + self.email
class Suserupload(models.Model):
    suserno = models.AutoField(primary_key=True)
    images = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='songs')
    stitle = models.CharField(max_length=100)
    sdesc = models.TextField()
    

class Userprofile(models.Model):
    user = models.OneToOneField(User,primary_key=True,blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images',default = 'default/user.png')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    
    phone = models.CharField(max_length=10,null=True,blank=True)
    

    def __str__(self):
        return str(self.user)
