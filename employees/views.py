from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Employee
from django.views import generic




class EmployeesCreateView(generic.CreateView):
    model = Employee
    fields = ['first_name','middle_name','last_name','id_number','pj_number',
              'nhif_number','nssf_number','date_of_birth','gender','remarks']

    
    def get_success_url(self):
        return reverse("employees-list")
   

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
     

