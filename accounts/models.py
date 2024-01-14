from django.db import models

# Create your models here.

class AccountType(models.Model):
    name = models.CharField(verbose_name = 'النوع', max_length=30)
    description = models.TextField(verbose_name = 'الوصف', max_length=150,null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class Account(models.Model):
    
    STATUS_CHOICES = [
        (1,'نشط'),
        (2,'موقف')
    ]
    number = models.CharField(verbose_name = 'الرقم', max_length=15)
    name = models.CharField(verbose_name = 'الاسم',max_length=50, null=False , blank= False)
    account_type = models.ForeignKey(AccountType , on_delete= models.PROTECT)
    status = models.IntegerField(verbose_name='الحالة',choices=STATUS_CHOICES)
    def __str__(self):
        return self.name