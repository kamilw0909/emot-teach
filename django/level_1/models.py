from django.db import models

# Create your models here.

class Emotion(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField()

    def __str__(self):
        return self.name

class Question(models.Model):
    content = models.CharField(max_length=100)
    