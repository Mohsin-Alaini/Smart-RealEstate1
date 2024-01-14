from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view(request):
    return HttpResponse('view1')
def view2(request,id):
    return HttpResponse('view2')
def view3(request,id,name):
    return HttpResponse('view3')
# def view4(request):
#     return HttpResponse('view4')
