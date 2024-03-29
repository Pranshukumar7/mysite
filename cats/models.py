from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator

class Breed(models.Model):
    name = models.CharField(max_length = 200,
    validators = [MinLengthValidator(2,"Breed must be greather than 1 character")] )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(max_length =200,
                validators = [MinLengthValidator(2,"Breed must be greather than 1 character")] )
    weight = models.FloatField()
    foods = models.CharField(max_length=300,default= "fish")
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.nickname
