from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Categories(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Location(models.Model):

    name = models.CharField(max_length=100, unique=True)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"



class User(AbstractUser):

    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30, null=True)
    # username = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    role = models.CharField(max_length=15)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


# class User_new(AbstractUser):
#     MALE = 'm'
#     FEMALE = 'f'
#     SEX = [(MALE, 'Male'), (FEMALE, 'Female')]
#
#     sex = models.CharField(max_length=1, choices=SEX, default=MALE)



class Ads(models.Model):

    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Selection(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Ads)



