from typing import Any
from django import forms 
from accounts.models import Currency , AccountType ,Account

class StudentForm(forms.Form):
    number = forms.IntegerField(label='number',max_value=1000,min_value=1)
    name = forms.CharField(label='name',max_length=20)
    
    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')
        cleaned_data['number'] = 200
        print(cleaned_data,'clean_data')
        return cleaned_data
    
    def clean_number(self):
        cleaned_data = super().clean()
        if cleaned_data['number'] >= 1 and cleaned_data['number'] <= 20 :
            return cleaned_data['number']
        
        else:
            self.add_error('number','the value must be more than 0 and less than or equel 20 .')
    
class CurrencyForm(forms.ModelForm):
    additional_field = forms.CharField(label='حقل اضافي', required=True,initial='255')
    #code = forms.CharField(label='code',widget=forms.NumberInput,required=True)
    
    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['code'].label = 'الكود'
        self.fields['code'].initial = 'yer'
        self.fields['code'].disabled = True 
    
    class Meta:
        model=Currency
        fields = '__all__'
        # [ 
        #     'code',
        #     'name',
        #     'local'
        # ]
        
class AccountTypeForm(forms.ModelForm):
    
    class Meta:
        model = AccountType
        fields = '__all__'
        
class AccountForm(forms.ModelForm):
    
    def clean_name(self):
        
        cleaned_data = self.cleaned_data
        name = cleaned_data['name']
        name = cleaned_data.get('name')
        # self.add_error('name','kdcjn')
        return name
    
    class Meta :
        model = Account
        fields = '__all__'