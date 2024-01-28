from django.urls import path
from accounts import views
from .views import EmployeeView , EmployeeTaskView

urlpatterns = [
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('employeetask/', EmployeeTaskView.as_view(), name='employeetask'),
 
]
