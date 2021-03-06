from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
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


class EmployeeTransfersView(generic.DetailView):
    model = Employee
    template_name = "employees/employee_transfers.html"

class EmployeeCreateNewTransferView(generic.DetailView):
    model = Employee
    template_name = "employees/employee_create_transfer_form.html"


class EmployeeLeavesView(generic.DetailView):
    model = Employee
    template_name = "employees/employee_leaves.html"

class EmployeeCreateLeaveFormView(generic.DetailView):
    model = Employee
    template_name = "employees/employee_create_leave_form.html"


class EmployeeDocuments(generic.DetailView):
    model = Employee
    template_name = "employees/employee_documents.html"

class EmployeeAddNewDocument(generic.DetailView):
    model = Employee
    template_name = "employees/employee_new_document_form.html"


class EmployeePromotionsView(generic.DetailView):
    model = Employee
    template_name = "employees/employee_promotions.html"


class EmployeePromoteView(generic.DetailView):
    model = Employee
    template_name = "employees/employee_promote_form.html"




def dashboard(request):
    context = {}
    return render(request, "employees/dashboard.html", context)


def reports(request):
    context = {}
    return render(request, "employees/reports.html", context)
