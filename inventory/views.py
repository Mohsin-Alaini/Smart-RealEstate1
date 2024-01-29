# from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand


# Create your views here.

def new(request):
    Brand.objects.create(brand_id=2,name= 'Puma')
    
    return HttpResponse('Hi')

    
