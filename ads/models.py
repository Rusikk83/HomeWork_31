from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from ads.validators.user_validators import check_birth_date, check_email


# Create your models here.


class Categories(models.Model):

    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=10, unique=True,  validators=[MinLengthValidator(5)]) #unique=True,

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

    role = models.CharField(max_length=15, default='member')
    age = models.IntegerField(null=True)
    location = models.IntegerField(null=True)#models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(validators=[check_birth_date], null=True)
    email = models.EmailField(unique=True, null=True, validators=[check_email])

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Ads(models.Model):

    name = models.CharField(validators=[MinLengthValidator(10)], null=False, blank=False, max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"



