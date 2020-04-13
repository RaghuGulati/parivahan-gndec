from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    urn = models.IntegerField(primary_key = True)
    crn = models.IntegerField()
    name = models.CharField(max_length=50)
    parents_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length = 50)
    aadhar_no = models.CharField(max_length = 12)
    Address = models.CharField(max_length=50)
    branch = models.CharField(max_length=20) 
    year = models.IntegerField()
    section = models.CharField(max_length=5)
    residence = models.CharField(max_length=50)
    photo = models.FileField(upload_to='./student_photo/')
    class_calculated =  models.CharField(max_length=50)

class CareTaker(models.Model):
     unique_id = models.CharField(primary_key = True, max_length = 6)
     name = models.CharField(max_length=50)
     mobile = models.CharField(max_length = 10)
     email = models.EmailField(max_length = 50)
     hostel_no = models.IntegerField()

class Advisor(models.Model):
    unique_id = models.CharField(primary_key = True, max_length = 6)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 50)
    class_alloted = models.CharField(max_length = 50)

class Departments(models.Model):
	dept_id =  models.CharField(primary_key = True, max_length = 4)
	dept_name = models.CharField(max_length = 25)
	dept_hod = models.CharField(max_length = 25 )
	contact = models.CharField(max_length = 15)
	email = models.EmailField(max_length = 25)

class ClerkOffice(models.Model):
    clerk_id =  models.CharField(primary_key = True, max_length = 4)
    clerk_name = models.CharField(max_length=50)
    department_id = models.CharField(max_length = 20)

class PgBlock(models.Model):
    employee_id = models.CharField(primary_key = True, max_length = 4)
    employee_name = models.CharField(max_length=50)
    head_name = models.CharField(max_length=50)
    head_id = models.IntegerField()

class application_form(models.Model):
    unique_id = models.CharField(primary_key = True, max_length = 12)
    urn = models.ForeignKey('Student', on_delete = models.CASCADE)
    depo_name = models.CharField(max_length = 25)
    location_from = models.CharField(max_length = 25)
    location_to = models.CharField(max_length = 25)
    period_from = models.DateField()
    period_to = models.DateField()
    old_pass_no = models.CharField(max_length = 12)
    level = models.CharField(max_length = 25)
    status = models.CharField(max_length = 8, default = "Accepted")

	

	
