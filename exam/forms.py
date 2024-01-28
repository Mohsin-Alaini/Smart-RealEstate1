from django import forms
from .models import Employee , EmployeeTask

class EmployeeForm(forms.ModelForm):
    
    class Meta :
        model = Employee
        fields = '__all__'

class EmployeeTaskFrom(forms.ModelForm):
    
    class Meta :
        model = EmployeeTask
        fields = '__all__'