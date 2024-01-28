from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce

# Create your models here.


class Currency(models.Model):
    code = models.CharField(verbose_name='رمز العملة', max_length=15)
    name = models.CharField(verbose_name='اسم العملة', max_length=50)
    local = models.BooleanField(verbose_name='عملة محلية', default=False)
    def __str__(self):
        return self.code
    class Meta:
        db_table = 'Currency'
    
class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    exchange_rate = models.FloatField(verbose_name='سعر الصرف')
    max_exchange_rate = models.FloatField(verbose_name='اعلى سعر صرف')
    min_exchange_rate = models.FloatField(verbose_name='ادتى سعر صرف')
    date = models.DateTimeField( auto_now_add=True)
    def __str__(self) -> str:
        return str(self.date) + ' -    ' + str(self.exchange_rate)
    
        
class AccountType(models.Model):
    name = models.CharField(verbose_name='نوع الحساب', max_length=50)
    descriptiom = models.CharField(verbose_name='الوصف', max_length=200)
    def __str__(self):
        return self.name
        
class Account(models.Model):
    STATUS_CHOICES = [
        (1, 'نشط'),
        (2, 'موقف'),
    ]
    number = models.CharField(verbose_name='رقم الحساب', max_length=15, blank=False, null=False)
    name = models.CharField(verbose_name='اسم الحساب', max_length=100, blank=False, null=False)
    status = models.IntegerField(verbose_name='الحالة', choices=STATUS_CHOICES, blank=False, null=False)
    type = models.ForeignKey(AccountType, verbose_name='نوع الحساب', on_delete=models.CASCADE)
    currency = models.ManyToManyField(Currency, verbose_name='العملات')
    def __str__(self):
        return self.name
    
    def get_balance(self):
        balance = TransactionDetails.objects.filter(account=self.id).aggregate(balance=Coalesce(Sum('debit'),0.0) - Coalesce(Sum('credit'),0.0))
        return balance
    
    
    
class Transaction(models.Model):
    number = models.CharField(verbose_name='رقم العملية', max_length=15)
    date = models.DateField(verbose_name='التاريخ')
    def __str__(self):
        return self.number + ' - ' + str(self.date)
    
    
class TransactionDetails(models.Model):
    account = models.ForeignKey(Account, verbose_name='الحساب', on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, verbose_name='العملة', on_delete=models.CASCADE)
    exchang_rate = models.FloatField(verbose_name='سعر التحويل')
    debit = models.FloatField(verbose_name='المبلغ المدين', blank=True, null=True)
    credit = models.FloatField(verbose_name='المبلغ الدائن', blank=True, null=True)
    note = models.TextField(verbose_name='ملاحظة', max_length=300)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    
    
    
    
    
    
    


# from django.db import models

# # Create your models here.

# class AccountType(models.Model):
#     name = models.CharField(verbose_name = 'النوع', max_length=30)
#     description = models.TextField(verbose_name = 'الوصف', max_length=150,null=True,blank=True)
    
#     def __str__(self):
#         return self.name
    

# class Account(models.Model):
    
#     STATUS_CHOICES = [
#         (1,'نشط'),
#         (2,'موقف')
#     ]
#     number = models.CharField(verbose_name = 'الرقم', max_length=15)
#     name = models.CharField(verbose_name = 'الاسم',max_length=50, null=False , blank= False)
#     account_type = models.ForeignKey(AccountType , on_delete= models.PROTECT)
#     status = models.IntegerField(verbose_name='الحالة',choices=STATUS_CHOICES)
#     def __str__(self):
#         return self.name