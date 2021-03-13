from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from offer.models import Offer

# Create your models here.
class Cart(models.Model):
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    int_status = models.IntegerField() #0:Pending 1:Ordered 