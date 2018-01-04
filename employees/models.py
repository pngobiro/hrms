from django.db import models
from django.utils import timezone


# Create your models here.

class Employee(models.Model):
    GENDER = ((1, 'Male'), (2, 'Female'), (3, 'Transgender'),)
    STATUS = ((1, 'inservice'), (2, 'dismissed'), (3, 'retired'), (4, 'suspended'), (5, 'deceased'))
    first_name = models.CharField(max_length=20, help_text="Employee First Name")
    middle_name = models.CharField(max_length=20, help_text="Employee Middle Name")
    last_name = models.CharField(max_length=20, help_text="Employee Surname Name")
    id_number = models.CharField(max_length=10, help_text="Passport or National Identification Number")
    pj_number = models.IntegerField(unique=True)
    nhif_number = models.CharField(max_length=20, unique=True)
    nssf_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.IntegerField(choices=GENDER)
    #email_address = models.EmailField(null=True,blank=True, unique=True)
    postal_address = models.CharField(max_length=10, help_text="Postal Adddress", blank=True, null=True)
    home_country = models.IntegerField()
    remarks = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='employees_profile_picture', blank=True, null=True)

    def __str__(self):
        return (" ".join([self.first_name, self.middle_name, self.last_name]))

    def full_name(self):
        return (" ".join([self.first_name, self.middle_name, self.last_name]))

    def age(self):
        return timezone.now().year - self.date_of_birth.year

    def current_designation(self):
        return self.employeedesignation.last

    def date_of_retirement(self):
        return self.date_of_birth.year + 55

    class Meta:
        ordering = ('pj_number',)


class Designation(models.Model):
    name = models.CharField(max_length=20, help_text="Designation Name", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class EmployeeDesignations(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    date_of_apppointment = models.DateField()
    remarks = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{} -{}".format(self.employee, self.designation)
