from django.db import models
from products.models import Product

# Create your models here.
class Offer(models.Model):
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    int_offer_price = models.IntegerField()
    int_offer_percent = models.IntegerField()