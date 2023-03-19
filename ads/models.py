from django.db import models

# Create your models here.
class Ads(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)


class Categories(models.Model):

    name = models.CharField(max_length=30)
