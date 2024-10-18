from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date} at {self.time}"