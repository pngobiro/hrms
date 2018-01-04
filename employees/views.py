from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Employee
from django.views import generic


class EmployeeCreateView(generic.CreateView):
    model = Employee
    fields = ['first_name', 'middle_name', 'last_name', 'id_number', 'pj_number',
              'nhif_number', 'nssf_number', 'date_of_birth', 'gender', 'remarks']

    def get_success_url(self):
        return reverse("employees-list")


class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by = 20


class EmployeeDetailView(generic.DetailView):
    model = Employee


class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    template_name = "employees/employee_update_form.html"

    fields = ['first_name', 'middle_name', 'last_name', 'id_number', 'pj_number',
              'nhif_number', 'nssf_number', 'date_of_birth', 'gender', 'remarks']

    def get_success_url(self):
        return reverse("employees-list")


class EmployeeTransfersView(generic.TemplateView):
    model = Employee
    template_name = "employees/employee_transfers.html"



class EmployeeLeavesView(generic.TemplateView):
    model = Employee
    template_name = "employees/employee_leaves.html"


class EmployeeDocuments(generic.TemplateView):
    model = Employee
    template_name = "employees/employee_documents.html"


class EmployeePromotionsView(generic.TemplateView):
    model = Employee
    template_name = "employees/employee_promotions.html"


def dashboard(request):
    context = {}
    return render(request, "employees/dashboard.html", context)


def reports(request):
    context = {}
    return render(request, "employees/reports.html", context)
