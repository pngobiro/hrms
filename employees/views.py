from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Employee

# Create your views here.

def dashboard(request):
     context = {}
     return render(request,"employees/dashboard.html",context)
    

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

def reports(request):
         context = {}
         return render(request,"employees/reports.html",context)
     
def detail(request, employee_id):
            employee = get_object_or_404(Employee, pk=employee_id)
            context = {"employee": employee,}
            return render(request, 'employees/detail.html',context)
