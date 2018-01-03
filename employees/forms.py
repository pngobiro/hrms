from django.db import models
from .models import Employee

class EmployeeForm(models.Model):
   
   
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name','id_number']
    