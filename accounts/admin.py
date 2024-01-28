from django.contrib import admin
from .models import AccountType, Account, Currency, ExchangeRate, Transaction, TransactionDetails
# Register your models here.
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(Currency)
admin.site.register(ExchangeRate)

class TransactionDetailsAdmin(admin.TabularInline):
    model  = TransactionDetails
    extra  = 2
@admin.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    inlines = [TransactionDetailsAdmin]
        

    


