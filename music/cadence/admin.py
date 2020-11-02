from django.contrib import admin
from .models import Contact, Suserupload, Userprofile

# Register your models here.
admin.site.register((Contact, Suserupload, Userprofile))
