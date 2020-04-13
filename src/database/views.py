#from django.shortcuts import render
from django.shortcuts import *
from .models import *
from .forms import *
from datetime import datetime
from django.db.models import *

# Create your views here.
def home_view(request):
	return render(request, "home.html")

def add_new_student(request):
	form = new_student(request.POST, request.FILES or None)
	obj = Student()
	
	if form.is_valid():
		obj.urn = int(form.cleaned_data.get("urn"))
		obj.crn = int(form.cleaned_data.get("crn"))
		obj.name = form.cleaned_data.get("name")
		obj.mobile = form.cleaned_data.get("mobile")
		obj.parents_name = form.cleaned_data.get("fmname")
		obj.email = form.cleaned_data.get("email")
		obj.Address = form.cleaned_data.get("address")
		obj.aadhar_no = form.cleaned_data.get("aadhar_no")
		obj.branch = form.cleaned_data.get("branch")
		obj.year = form.cleaned_data.get("year")
		obj.section = form.cleaned_data.get("section")
		obj.residence = form.cleaned_data.get("residence")
		obj.photo = form.cleaned_data.get("photo")
		obj.class_calculated = "D" + str(obj.year) + str(obj.branch) + str(obj.section)
		obj.save()

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

def prtc_form_application(request, urno):
	obj = Student.objects.get(urn = urno)
	paas = application_form()

	template = "prtc_form.html"

	ct = application_form.objects.all().aggregate(Count('unique_id'))


	if obj.residence == "Hosteler":
		return redirect("/")

	else:
		if request.method == "POST":
			paas.unique_id = "888" + '{:03}'.format(ct['unique_id__count'])
			paas.urn = obj
			paas.depo_name = request.POST.get("depo")
			paas.location_from = request.POST.get("loc_from")
			paas.location_to = request.POST.get("loc_to")
			paas.period_from = request.POST.get("period_from")
			paas.period_to = request.POST.get("period_to")
			paas.old_pass_no = request.POST.get("oldpassno")
			paas.level = "CRT"
			paas.status = "Accepted"
			paas.save()

	context = {
			"obj": obj,
			}

	return render(request, template, context)


