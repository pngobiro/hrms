from django.shortcuts import render
from .models import Employee
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def dashboard(request):
     context = {}
     return render(request,"employees/dashboard.html",context)
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


def list_employees(request):
    """
    Learning simple models

    """
    all_employees =  Employee.objects.all()
    context = {
            "all_employees" : all_employees,
    }
    return render(request,"employees/list.html",context)

def employee_edit(request, pk):
    pass