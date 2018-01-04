from django.contrib import admin
from .models import Employee, Designation, EmployeeDesignations
from django.utils import timezone


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "pj_number", "gender", "age")

    def full_name(self, obj):
        return (" ".join([obj.first_name, obj.middle_name, obj.last_name]))

    def age(self, obj):
        return timezone.now().year - obj.date_of_birth.year

    list_filter = ("gender",)


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Designation)
admin.site.register(EmployeeDesignations)
