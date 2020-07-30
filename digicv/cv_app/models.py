from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10,unique=True)
    email = models.URLField(unique=True)
    company = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.save()

    def __str__(self):
        return self.user_name
