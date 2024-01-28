from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Currency ,ExchangeRate ,Account,AccountType,TransactionDetails
from .forms import StudentForm , CurrencyForm ,AccountTypeForm
from django.db.models import Q , Min, Max, Avg, Sum , F
from django.views import View

# Create your views here.

# def view(request):
#     if request.method=='GET':
#       account = Account.objects.all()
#       response = [
#           'Account'
#       ] 
#       return HttpResponse(account)
def view(request):
    #Currency.objects.create(code='YER',name='yemeni',local=True)
    #cur = Currency.objects.all().first()
    #ExchangeRate.objects.create(Currency = cur ,exchange_rate=1,max_exchange_rate=1,min_exchange_rate=1)
    #print(cur,'jjjjjjjjj')
    
    #currency = ExchangeRate.objects.values('exchange_rate','currency__name','currency__id')
    # currency = Currency.objects.values('id','name','exchangerate__exchange_rate')
    # client_trans = Account.objects.filter(name='client1').values('name','transactiondetails__debit','transactiondetails__credit')
    # transaction = TransactionDetails.objects.filter(~Q(account__number='001',transaction__date__gte='2024-01-05',account__name='client1')).aggregate(Sum('debit'),Sum('credit') )
    # #transaction = TransactionDetails.objects.values("account__name").annotate(sum_de=Sum('debit'),sum_cre=Sum('credit')).annotate(balance=F('debit')-F('credit'))
    # transaction = TransactionDetails.objects.values("account__name").annotate(sum_de=Sum('debit'),sum_cre=Sum('credit')).annotate(balance=F('sum_de')-F('sum_cre'))
    
    
    
    # print('######################')
    # print(transaction)
    # print('######################')
    
    # for cu in transaction:
    #     print(cu)

    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        print(request.POST.get('code'),'code')
        add = request.POST.get('')
        if form.is_valid():
            currency = form.save(commit=False)
            currency.local = False
            currency.save()
            # print(form.cleaned_data['number'],'view')
        else:
            print(form.errors)
             
    else: 
        form = CurrencyForm() 
          
    context = {
        'form' : form
        # 'transaction' : transaction,
        # 'currency' : currency
    }
    return render(request,'account_page.html',context)
 
 
 
 
        
class AbsView(View):
    form = None
    template_name = None
    
    def get(self, request, *args , **kwargs):
        
        account = Account.objects.first().get_balance()
        print('$$$$$$$$$$$$$$$')
        print(account)
        print('$$$$$$$$$$$$$$$')
        
        form = self.form() 
        context = {
            'form' : form
        }
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            self.save_modle(obj)
            
           
            
        else:
            print(form.errors)
        
        context = {
            'form' : form
        }
        return render(request,self.template_name,context)

    def save_modle(self,obj):
        obj.save()
class AccountTypeView1(AbsView):
    form = AccountTypeForm 
    template_name = 'account_page.html'
    
    def save_modle(obj):
        obj.save()
    
class CurrencyView(AbsView):
    form = CurrencyForm
    template_name = 'account_page.html' 
                

    #return HttpResponse('view1')

def view2(request,id):
    return HttpResponse('view2')
def view3(request,id,name):
    return HttpResponse('view3')
def view4(request,path):
    return HttpResponse('view4')


class AccountTypeView(View):
    def get(self, request, *args , **kwargs):
        account_types = AccountType.objects.all()
        form = AccountTypeForm()
        context = {
            'form' : form,
            'data' : account_types        }
        return render(request,'account_type.html',context)
    
    def post(self, request, *args , **kwargs):
        account_types = AccountType.objects.all()
        form = AccountTypeForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(type(form),'form_type')
            obj = form.save()
            #obj.name = 
            #form.save()
            print(type(obj),'form_type2')
            
    
        context = {
            'form' : form,
            'data' : account_types,
            #'cleaned_data' : cleaned_data

        }
        return render(request,'account_type.html',context)   
        
    
