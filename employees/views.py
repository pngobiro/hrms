from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Employee
from django.views import generic



class EmployeesCreate(generic.CreateView):
    model = Employee
    fields = ['first_name','middle_name','last_name']

class EmployeesListView(generic.ListView):
    model = Employee
    paginate_by = 10
   

class EmployeesDetailView(generic.DetailView):
    model = Employee

class EmployeesTransfersView(generic.DetailView):
    model = Employee
    
    template_name = "employees/transfers.html"
    
class EmployeesPromotionsView(generic.TemplateView):
    model = Employee
    template_name = "employees/promotions.html"
    
class EmployeesLeavesView(generic.TemplateView):
    model = Employee
    template_name = "employees/leaves.html"

def dashboard(request):
     context = {}
     return render(request,"employees/dashboard.html",context)
    

def reports(request):
         context = {}
         return render(request,"employees/reports.html",context)
     

