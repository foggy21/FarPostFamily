from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
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
