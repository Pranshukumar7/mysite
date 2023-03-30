from django.db import models 
from django.core.validators import MinLengthValidator

class Make(models.Model):
    name = models.CharField(help_text = 'Enter a make (eg. Maruti)', max_length=50,
    validators = [MinLengthValidator(2,"Make must be long enough")])
    def __str__(self):
        return self.name

class Autos(models.Model):
    nickname = models.CharField(max_length=200,
        validators=[MinLengthValidator(2,"nickname should be long enough")]
        )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
    


#todo migrate to new database   
