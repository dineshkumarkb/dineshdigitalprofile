from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=10,unique=True)
    user_email = models.URLField(unique=True)

    def __str__(self):
        return self.user_name
