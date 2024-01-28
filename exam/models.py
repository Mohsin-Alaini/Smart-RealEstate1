from django.db import models

# Create your models here.


    
class EmployeeTask(models.Model):
    STATUS_CHOICES = [
        (1, 'Done'),
        (2, 'InProgress'),
        (3, 'ToDo')
    ]
    title = models.CharField(verbose_name = 'العنوان',max_length=25)
    description = models.CharField(verbose_name='الوصف', max_length=200)
    due_date = models.DateField(verbose_name = 'فترة')
    status = models.IntegerField(verbose_name='الحالة', choices=STATUS_CHOICES, blank=False, null=False)
    
    # def __str__(self):
    #     return self.title
    
    

class Employee(models.Model):
    first_name = models.CharField(verbose_name='الاسم ', max_length=50)
    last_name = models.CharField(verbose_name='اللقب', max_length=50)
    number = models.IntegerField(verbose_name = 'الرقم')
    email = models.EmailField(verbose_name = 'ايميل',max_length=50)
    hire_date = models.DateField(verbose_name = 'تاريخ ')
    task = models.ForeignKey(EmployeeTask,verbose_name='نوع المهمة', on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.first_name