from django.db import models

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
