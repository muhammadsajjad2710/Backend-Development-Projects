from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=80)
    stock = models.PositiveIntegerField(default=0)
    price_cents = models.PositiveIntegerField()
