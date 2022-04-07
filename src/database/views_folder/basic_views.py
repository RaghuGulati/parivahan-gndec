#from django.shortcuts import render
from django.shortcuts import *
from database.models import *
from database.forms import *
from datetime import datetime
from django.db.models import *
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
	)
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.
def home_view(request):
	return render(request, "front.html")

def login(request):
	form = loginform(request.POST)
	if form.is_valid():
	   username = form.cleaned_data.get("uid")
	   password = form.cleaned_data.get("password")
	   login_as = form.cleaned_data.get("login_as")

	   u = User.objects.get(username = username)
	   if u.check_password(password) == True:
	       return redirect('/portal/'+str(login_as)+'/'+ str(username) + '/')
	   else:
	       return HttpResponse("Login with correct credentials")

	context = {"form" : form,}
	return render(request, "login.html", context)

def add_new_student(request):
	form = new_student(request.POST, request.FILES or None)
	obj = Student()
	
	if form.is_valid():
		obj.urn = int(form.cleaned_data.get("urn"))
		password = form.cleaned_data.get("password")
		confpass = form.cleaned_data.get("conf_password")
		obj.crn = int(form.cleaned_data.get("crn"))
		obj.name = form.cleaned_data.get("name")
		obj.mobile = form.cleaned_data.get("mobile")
		obj.parents_name = form.cleaned_data.get("fmname")
		obj.email = form.cleaned_data.get("email")
		obj.Address = form.cleaned_data.get("address")
		obj.gender = form.cleaned_data.get("gender")
		obj.aadhar_no = form.cleaned_data.get("aadhar_no")
		obj.branch = form.cleaned_data.get("branch")
		obj.year = form.cleaned_data.get("year")
		obj.section = form.cleaned_data.get("section")
		obj.residence = form.cleaned_data.get("residence")
		obj.photo = form.cleaned_data.get("photo")
		obj.class_calculated = "D" + str(obj.year) + str(obj.branch) + str(obj.section)
		
		if obj.residence == "Day Scholor":
			obj.hostel_no = 0

		else:
			obj.hostel_no = form.cleaned_data.get("hostel_no")

		if password == confpass:
			user = User.objects.create_user(username=obj.urn,
                                 email=obj.email,
                                 password=password)
			obj.save()

		else:
			return HttpResponse("<h1>password and confirmation password does not match</h1>")
	

		return redirect("/")

	template = "new.html"
	context = {"form" : form,}
	return render(request, template, context)

def add_new_care_taker(request):
	form = new_care_taker(request.POST, request.FILES or None)
	obj = CareTaker()
	crt_ct = CareTaker.objects.all().aggregate(Count('unique_id'))
	if form.is_valid():
		obj.unique_id = "CRT" + '{:03}'.format(crt_ct['unique_id__count'])	
		obj.name = form.cleaned_data.get("name")
		obj.mobile = form.cleaned_data.get("mobile")
		obj.email = form.cleaned_data.get("email")
		obj.hostel_no = form.cleaned_data.get("hostel_no")
		obj.department = form.cleaned_data.get("department")
		obj.save()
		return redirect("/")

	template = "new.html"
	context = {"form" : form,}
	return render(request, template, context)

def add_new_advisor(request):
	form = new_advisor(request.POST, request.FILES or None)
	
	obj = Advisor()
	crt_ct = Advisor.objects.all().aggregate(Count('unique_id'))
	if form.is_valid():
		obj.unique_id = "ADV" + '{:03}'.format(crt_ct['unique_id__count'])	
		obj.name = form.cleaned_data.get("name")
		obj.mobile = form.cleaned_data.get("mobile")
		obj.email = form.cleaned_data.get("email")
		obj.class_alloted = form.cleaned_data.get("class_alloted")
		obj.save()

		return redirect("/")
	
	template = "new.html"
	context = {"form" : form,}
	return render(request, template, context)
	
