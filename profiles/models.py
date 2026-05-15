from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

# Create your models here.
