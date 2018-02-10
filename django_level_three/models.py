from django.db import models

# Create your models here.
class newuser(models.Model):
    FirstName = models.CharField(max_length=264)
    LastName = models.CharField(max_length=264)
    Email = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.Email