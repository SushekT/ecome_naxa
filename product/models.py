from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    description = models.TextField()
    leather = models.PositiveIntegerField()
    polyster = models.PositiveIntegerField()
    Guarantee = models.PositiveIntegerField()


class ProductCategory(models.Model):
    product_category = models.CharField(max_length=20)