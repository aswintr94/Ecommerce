from django.db import models

# Create your models here.
class Product(models.Model):
    str_brand = models.CharField(max_length=255, blank=True, null=True)
    str_model = models.CharField(max_length=255, blank=True, null=True)
    str_ram = models.CharField(max_length=255, blank=True, null=True)
    str_memory = models.CharField(max_length=255, blank=True, null=True)
    str_camera = models.CharField(max_length=255, blank=True, null=True)
    str_battery = models.CharField(max_length=255, blank=True, null=True)
    str_processor = models.CharField(max_length=255, blank=True, null=True)
    int_price = models.IntegerField()
    img_image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.str_model