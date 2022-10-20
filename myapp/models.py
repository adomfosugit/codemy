from django.db import models

# Create your models here.
class Bakery(models.Model):
    name = models.CharField('Product name', max_length = 120)
    Description = models.CharField('Description' , max_length = 300)
    Price = models.FloatField(' price', blank = False, default= 1.0)
    product_image = models.ImageField(null = True, blank= False, upload_to = 'images/' )
