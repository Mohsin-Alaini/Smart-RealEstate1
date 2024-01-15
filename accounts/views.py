from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Account,AccountType

# Create your views here.

def view(request):
    if request.method=='GET':
      account = Account.objects.all()
      response = [
          'Account'
      ]
      return HttpResponse(account)
def view2(request,id):
    return HttpResponse('view2')
def view3(request,id,name):
    return HttpResponse('view3')
# def view4(request):
#     return HttpResponse('view4')
