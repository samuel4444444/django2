import django
from django.db import models
from datetime import date

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    # published_date = models.DateField(django.utils.timezone.now)


    def __str__(self):
        return self.title
