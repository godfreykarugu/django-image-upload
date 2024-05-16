from django.db import models


    

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price =models.IntegerField()
    product_description = models.TextField(blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images/', default='')

    def __str__(self):
        return self.product_name