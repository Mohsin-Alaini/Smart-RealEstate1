from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee , EmployeeTask
from .forms import EmployeeForm , EmployeeTaskFrom
from django.views import View

# Create your views here.


class AbsView(View):
    form = None
    template_name = None
    
    def get(self, request, *args , **kwargs):
        
        # employee = Employee.objects.first().get_balance()
        # print('$$$$$$$$$$$$$$$')
        # print(account)
        # print('$$$$$$$$$$$$$$$')
        
        form = self.form() 
        context = {
            'emp' : form
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
            'emp' : form
        }
        return render(request,self.template_name,context)

    def save_modle(self,obj):
        obj.save()
        
        
        
class EmployeeView(AbsView):
    form = EmployeeForm 
    template_name = 'employee_page.html' 
    
    def save_modle(obj):
        obj.save()
    
class EmployeeTaskView(AbsView):
    form = EmployeeTaskFrom
    template_name = 'employee_page.html' 