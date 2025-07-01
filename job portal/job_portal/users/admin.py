from django.contrib import admin
from users.models import  JobApplication, contact

# Register your models here.

admin.site.register(JobApplication)
admin.site.register(contact)