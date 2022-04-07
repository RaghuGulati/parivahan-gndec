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
		View,
	)

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models.signals import post_save
from notifications.signals import notify
 #created in step 4

# Create your views here.
def pgb_navbar(request, empid):
	obj = PgBlock.objects.get(employee_id = empid)
	template = 'navbar.html'

	context = {
			"obj":obj,
			"objtype": obj.employee_id[0:3] 
	}

	return render(request, template, context)

class recommended_application_view(ListView):
	template_name = "application_form/application_form-list.html"
	app = []

	def get_queryset(self):
		self.pbg = get_object_or_404(PgBlock, employee_id = self.kwargs['empid'])
		self.appl = application_form.objects.filter(level = "PGB", urn__hostel_no = 0)
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.pbg.employee_id[0:3]
		context['obj'] = self.pbg
		context['app'] = self.appl
		context['type'] = "rec"
		context['heading'] = "Recommended"
		return context

def accept_form_application(request, empid, appid):
	template = 'ClerkOffice/accept.html'
	obj = PgBlock.objects.get(employee_id = empid)
	app_form = application_form.objects.get(unique_id = appid)
	user = User.objects.get(username = app_form.urn_id)
	app_form.level = "ARar"
	app_form.description = "Approved by Academics Department and passed to Assistant Registrar"
	notify.send(user, recipient=user, verb='Application Approved by Department and Passed to Academics Department')
	app_form.save()

	context = {
			"obj":obj,
			"objtype": obj.employee_id[0:3], 
	}


	return render(request, template, context)
	
'''
def accept_form_application(request, deptid, appid):
	template = "ClerkOffice/accept.html"
	app_form = application_form.objects.get(unique_id = appid)
	user = User.objects.get(username = app_form.urn_id)

	obj = ClerkOffice.objects.get(department_id = deptid)
	dept = Departments.objects.get(dept_id= deptid)

	app_form.level = "PGB"
	app_form.description = "Approved by Department and Passed to Academics Department"
	
	notify.send(user, recipient=user, verb='Application Approved by Department and Passed to Academics Department')
	app_form.save()

	context = {
			"obj":dept,
			"objtype": obj.clerk_id[0:3] 
	}

	return render(request, template, context)	

class recommended_application_view(ListView):
	template_name = "application_form/application_form-list.html"
	app = []

	def get_queryset(self):
		self.crt = get_object_or_404(ClerkOffice, department_id = self.kwargs['deptid'])
		self.dept = get_object_or_404(Departments, dept_id = self.kwargs['deptid'])
		self.app = application_form.objects.filter(status = "Accepted")
		self.appl = self.app.filter(level = "CLR", urn__hostel_no = 0)		
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.crt.clerk_id[0:3]
		context['obj'] = self.dept
		context['app'] = self.appl
		context['type'] = "rec"
		context['heading'] = "Recommended"
		return context
'''