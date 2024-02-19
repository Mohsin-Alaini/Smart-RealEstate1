from django.db import models

#from mptt.models import MPTTModel,TreeForeignkey
# Create your models here.

# class Category(MPTTModel):
#     name = models.CharField(max_length=50)
#     slu = models.SlugField(max_length=100, unique = True)
#     is_active = models.BooleanField(default = False)
#     parent = TreeForeignkey("self", on_delete = models.PROTECT, related_name ="children", null = True , blank = True)
    
#     class MPTTMeta:
#         order_insertion_by = ["name"]
    
#     class Meta:
#         ordering = ["name"]
#         verbose_name_plural= _("categories")
        
#     def __str__(self):
#         return self.name
class Brand(models.Model):
    brand_id = models.PositiveIntegerField(primary_key = True , db_column= 'brand_id')
    name = models.CharField(verbose_name='name', max_length=50, unique= True)
    nickname= models.CharField(max_length=50)
    
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
    
