from django.db import models
from django.contrib.auth.models import User
from employers.models import JobPost
# Create your models here.



class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

