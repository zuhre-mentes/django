from django.db import models
from django.contrib.auth.models import User



class cities(models.Model):
    name = models.CharField(max_length=100)



# cities/models.py


class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return self.name
