import base64
import json
import os
from urllib import request
from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User as Person

# Create your models here.
class Interest(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Интерес"
        verbose_name_plural = "Интересы"
    
    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
    
    def __str__(self):
        return self.name

class User(models.Model):
    GENDER_CHOICES = (
            ('M', 'Мужчина'),
            ('F', 'Женщина'),
        )
    username = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images', blank=True, null=False, verbose_name="Фотография")
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[
        MaxValueValidator(75),
        MinValueValidator(18)
    ])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    interest = models.ManyToManyField(Interest)
    specialization = models.ForeignKey(Specialization, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return self.name
