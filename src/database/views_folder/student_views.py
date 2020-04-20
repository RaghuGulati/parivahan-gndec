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

def student_navbar(request, urno):
	obj = Student.objects.get(urn = urno)
	template = 'Student/navbar.html'

	context = {
			"obj":obj,
	}

	return render(request, template, context)

def student_details(request, urno):
	obj = Student.objects.get(urn = urno)
	template = 'Student/view_details.html'

	context = {
			"obj":obj,
	}

	return render(request, template, context)

def prtc_form_application(request, urno):
	obj = Student.objects.get(urn = urno)
	paas = application_form()

	template = "Student/prtc_form.html"

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
			paas.description = "Form filled by student"
			paas.save()

	context = {
			"obj": obj,
			}

	return render(request, template, context)