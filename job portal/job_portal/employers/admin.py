from django.contrib import admin
from .models import JobPost
# Register your models here.
admin.site.register(JobPost)

class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'type', 'posted_at', 'is_verified')
    list_filter = ('is_verified', 'posted_at')
    search_fields = ('title', 'company', 'location')