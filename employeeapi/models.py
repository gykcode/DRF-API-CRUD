from django.db import models

# Create your models here.

# --Data Models--
class Employees(models.Model):
    employeeID = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    dateOfEmployment = models.DateTimeField(auto_now_add=True)

class Departments(models.Model):
    departmentID = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=200)

     