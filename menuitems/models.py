from django.db import models

# Create your models here.

class Menuitem(models.Model):
    item = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)


    def __str__(self):
        return self.item
  
