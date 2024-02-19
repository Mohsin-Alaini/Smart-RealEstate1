# from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand
from django.db import IntegrityError


# Create your views here.

def new(request):
    
    try:
        Brand.objects.create(brand_id=5,name= 'New')   
    except IntegrityError:
        return HttpResponse("Sorry we can't add that ")
    
    return HttpResponse('Hi')


    
