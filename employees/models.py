from django.db import models

# Create your models here.

class Employee(models.Model):
    GENDER = ((1, 'Male'),(2, 'Female'),(3, 'Transgender'),)
    
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_number = models.CharField(max_length=10)
    pj_number = models.IntegerField()
    nhif_number = models.CharField(max_length=20)
    nssf_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices=GENDER)
    date_of_retirement = models.DateField(blank=True,null=True)
    
