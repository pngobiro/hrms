from django.db import models


# Create your models here.

class Employee(models.Model):
        GENDER = ((1, 'Male'),(2, 'Female'),(3, 'Transgender'),)
        first_name = models.CharField(max_length=20,help_text="Employee First Name")
        middle_name = models.CharField(max_length=20,help_text="Employee Middle Name")
        last_name = models.CharField(max_length=20,help_text="Employee Surname Name")
        id_number = models.CharField(max_length=10,help_text="Passport or National Identification Number")
        pj_number = models.IntegerField(unique= True)
        nhif_number = models.CharField(max_length=20,unique= True)
        nssf_number = models.CharField(max_length=20,unique= True)
        date_of_birth = models.DateField(verbose_name = "Date of Birth")
        gender = models.IntegerField(choices=GENDER)
        date_of_retirement = models.DateField(blank=True,null=True)

        def __str__(self):
            return (" ".join([self.first_name, self.middle_name, self.last_name]))

      
        

            
        def current_designation(self):
            self.employeedesignation.last

        class Meta:
           ordering = ('pj_number',)
           
           





class Designation(models.Model):
        name = models.CharField(max_length=20,help_text="Designation Name",unique= True)

        def __str__(self):
              return self.name

        class Meta:
            ordering = ('name',)

class EmployeeDesignations(models.Model):
         employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
         designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
         date_of_apppointment = models.DateField()
         remarks = models.CharField(max_length=250,blank=True,null=True)
         
         def __str__(self):
                return "{} -{}".format(self.employee,self.designation)
            





