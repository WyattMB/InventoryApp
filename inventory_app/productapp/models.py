from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    quantity = models.CharField(max_length=4)