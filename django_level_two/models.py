from django.db import models

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    category = models.ForeignKey(Topic, on_delete=True)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=True)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserAdded(models.Model):
    FirstName = models.CharField(max_length=264)
    LastName = models.CharField(max_length=264)
    Email = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.Email