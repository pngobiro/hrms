from django.shortcuts import render
from .models import Employee

# Create your views here.
def list_employees(request):
    """
    Learning simple models

    """
    all_employees =  Employee.objects.all()
    context = {
            "all_employees" : all_employees,
    }
    return render(request,"list.html",context)