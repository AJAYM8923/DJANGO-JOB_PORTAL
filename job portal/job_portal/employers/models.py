from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class JobPost(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    salary = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=200)
    description = models.TextField()
    responsibilities = models.TextField()
    skills = models.CharField(max_length=300)
    deadline = models.DateField()
    posted_at = models.DateTimeField(auto_now_add=True)
      
    is_verified = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.title} at {self.company}"
