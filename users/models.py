from django.contrib.auth.models import AbstractUser
from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date
from django.core.exceptions import ValidationError


USER_MIN_AGE = 9


def birth_date_validator(value):
    diff_yers = relativedelta(date.today(), value)
    if diff_yers < USER_MIN_AGE:
        raise ValidationError('User is underage')
    return value


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположение'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = [
        ("USER", "Пользователь"),
        ("ADMIN", "Админ"),
        ("MODERATOR", "Модератор")
        # ("Пользователь", USER),
        # ("Админ", ADMIN),
        # ("Модератор", MODERATOR),
    ]


# class User(models.Model):
#     first_name = models.CharField(verbose_name="Имя", max_length=60)
#     last_name = models.CharField(max_length=80)
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=30)
#     role = models.CharField(choices=UserRoles.choices, default= 'member', max_length=12)
#     age = models.CharField(max_length=60)
#     locations = models.ManyToManyField(Location)
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"



class User(AbstractUser):
    role = models.CharField(max_length=9, choices=UserRoles.choices, default="member")
    age = models.PositiveSmallIntegerField(null=True)
    locations = models.ManyToManyField(Location)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(validators=[birth_date_validator])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
               #self.username
