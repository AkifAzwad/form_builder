from django.db import models

# Create your models here.
class Api(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField()
    
    def __str__(self) -> str:
        return self.name