from django.db import models

# Create your models here.
class Student(models.Model):
    sno = models.IntegerField()
    urn = models.IntegerField()
    crn = models.IntegerField()
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length = 50)
    aadhar_no = models.IntegerField()
    branch = models.CharField(max_length=20) 
    year = models.IntegerField()
    section = models.CharField(max_length=5)
    hosteler_or_dayscollar = models.CharField(max_length=50)
    photo = models.FileField(upload_to='pics')
    class_calculated =  models.CharField(max_length=50)


class CareTaker(models.Model):
     sno = models.IntegerField()
     unique_id = models.IntegerField()
     name = models.CharField(max_length=50)
     mobile = models.IntegerField()
     email = models.EmailField(max_length = 50)
     hostel_no = models.IntegerField()
     date_and_time = models.DateTimeField(auto_now=True)

class Advisor(models.Model):
    sno = models.IntegerField()
    unique_id = models.IntegerField()
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length = 50)
    calss_alloted = models.IntegerField()
    date_and_time = models.DateTimeField(auto_now=True)

class ClerkOffice(models.Model):
    sno = models.IntegerField()
    unique_id = models.IntegerField()
    hod_name = models.CharField(max_length=50)
    clerk_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length = 50)
    branch = models.CharField(max_length = 20)
    date_and_time = models.DateTimeField(auto_now=True)

class PgBlock(models.Model):
    sno = models.IntegerField()
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=50)
    head_name = models.CharField(max_length=50)
    head_id = models.IntegerField()
    date_and_time = models.DateTimeField(auto_now=True)