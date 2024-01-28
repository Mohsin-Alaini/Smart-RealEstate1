from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(verbose_name='name', max_length=50)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField('category name', max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField("product name", max_length=50, default = 'no-name')
    age = models.IntegerField()
    is_active = models.BooleanField(default = True)
    category = models.ManyToManyField(Category, verbose_name='category')
    
    def __str__(self):
        return self.name 

class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, verbose_name='product', on_delete=models.CASCADE)
    
