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
from django_filters.views import FilterView
from django_tables2.views import *
from database.filters import *
from django.db.models.signals import post_save
from notifications.signals import notify
from django.contrib.auth.models import User

# Create your views here.
def dept_navbar(request, urno):
	obj = ClerkOffice.objects.get(department_id = urno)
	dept = Departments.objects.get(dept_id = urno)
	template = 'navbar.html'

	context = {
			"obj":dept,
			"objtype": obj.clerk_id[0:3] 
	}

	return render(request, template, context)

def dept_details(request, urno):
	obj = ClerkOffice.objects.get(department_id = urno)
	dd = Departments.objects.get(dept_id = urno)
	template = 'ClerkOffice/view_details.html'

	context = {
			"obj":dd,
			"clerk": obj,
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

class accepted_application_view(ListView):
	template_name = "application_form/application_form-list.html"

	def get_queryset(self):
		self.crt = get_object_or_404(ClerkOffice, department_id = self.kwargs['deptid'])
		self.dept = get_object_or_404(Departments, dept_id = self.kwargs['deptid'])
		self.app = []
		self.appl = application_form.objects.filter(urn__hostel_no = 0)
		for a in self.appl:
			if a.level == 'CLR' or a.level == 'PGB':
				self.app.append(a)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.crt.clerk_id[0:3]
		context['obj'] = self.dept
		context['app'] = self.app
		context['type'] = "acc"
		context['heading'] = "Accepted"
		return context	

class rejected_application_view(ListView):
	template_name = "application_form/application_form-list.html"

	def get_queryset(self):
		self.crt = get_object_or_404(ClerkOffice, department_id = self.kwargs['deptid'])
		self.dept = get_object_or_404(Departments, dept_id = self.kwargs['deptid'])
		self.app = []
		self.appl = application_form.objects.filter(urn__hostel_no = 0)
		for a in self.appl:
			if a.level == 'CLR' and a.status == 'Rejected':
				self.app.append(a)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.crt.clerk_id[0:3]
		context['obj'] = self.dept
		context['app'] = self.app
		context['type'] = "rej"
		context['heading'] = "Rejected"
		return context			

#This function displys the list of students of a
#particular department
class StudentListView(ListView):
	template_name = "Student/student_list.html"

	def get_queryset(self):
		self.clr = get_object_or_404(ClerkOffice, department_id = self.kwargs['deptid'])
		self.dept = get_object_or_404(Departments, dept_id = self.kwargs['deptid'])
		self.std = Student.objects.filter(branch = self.dept.dept_id)
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in the publisher
		context['objtype'] = self.clr.clerk_id[0:3]
		context['obj'] = self.dept
		context['std'] = self.std
		return context

def StudentDetailView(request, deptid, urno):
	template = "Student/student_detail.html"
	obj = ClerkOffice.objects.get(department_id = deptid)
	dept = Departments.objects.get(dept_id = deptid)
	context = {

			"student": Student.objects.get(urn = urno),
			"obj": dept,
			"objtype": obj.clerk_id[0:3] 
	}

	return render(request, template, context)

class AdvisorListView(ListView):
	template_name = "Advisor/advisor_list.html"

	def get_queryset(self):
		self.clr = get_object_or_404(ClerkOffice, department_id = self.kwargs['deptid'])
		self.dept = get_object_or_404(Departments, dept_id = self.kwargs['deptid'])
		self.adv = Advisor.objects.filter(department = self.kwargs['deptid'])
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in the publisher
		context['objtype'] = self.clr.clerk_id[0:3]
		context['obj'] = self.dept
		context['adv'] = self.adv
		return context	

def AdvisorDetailView(request, deptid, advid):
	template = "Advisor/advisor_detail.html"
	obj = get_object_or_404(ClerkOffice, department_id = deptid)
	dept = get_object_or_404(Departments, dept_id = deptid)

	context = {
			"advisor": Advisor.objects.get(unique_id = advid),
			"obj": dept,
			"objtype": obj.clerk_id[0:3] 
	}

	return render(request, template, context)		

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
