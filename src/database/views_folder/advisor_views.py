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

from django.db.models.signals import post_save
from notifications.signals import notify
from django.contrib.auth.models import User
import markdown

# Create your views here.
def adv_navbar(request, urno):
	obj = Advisor.objects.get(unique_id = urno)
	template = 'navbar.html'

	context = {
			"obj":obj,
			"objtype": obj.unique_id[0:3] 
	}

	return render(request, template, context)

def advisor_details(request, urno):
	obj = Advisor.objects.get(unique_id = urno)
	template = 'Advisor/view_details.html'

	context = {
			"obj":obj,
			"objtype": obj.unique_id[0:3] 

	}

	return render(request, template, context)

#This function displys the list of students of the group alloted to a 
#particular advisor
class StudentListView(ListView):
	template_name = "Student/student_list.html"

	def get_queryset(self):
		self.advisor = get_object_or_404(Advisor, unique_id = self.kwargs['advisor'])
		self.std = Student.objects.filter(class_calculated = self.advisor.class_alloted)
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in the publisher
		context['objtype'] = self.advisor.unique_id[0:3]
		context['obj'] = self.advisor
		context['std'] = self.std
		return context

#This function displys the details of a particular student 
#of the group alloted to a particular advisor 
def StudentDetailView(request, advisor, urno):
	template = "Student/student_detail.html"
	obj = Advisor.objects.get(unique_id = advisor)
	context = {
			"student": Student.objects.get(urn = urno),
			"obj": obj,
			"objtype": obj.unique_id[0:3] 
	}

	return render(request, template, context)

class recommended_application_view(ListView):
	template_name = "application_form/application_form-list.html"
	app = []

	def get_queryset(self):
		self.crt = get_object_or_404(Advisor, unique_id = self.kwargs['advisor'])
		self.app = application_form.objects.filter(status = "Accepted")
		self.appl = self.app.filter(level = "ADV", urn__hostel_no = 0)
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.crt.unique_id[0:3]
		context['obj'] = self.crt
		context['app'] = self.appl
		context['type'] = "rec"
		context['heading'] = "Recommended"
		return context

def accept_form_application(request, advisor, appid):
	template = "Advisor/status.html"
	app_form = application_form.objects.get(unique_id = appid)
	user = User.objects.get(username = app_form.urn_id)

	obj = Advisor.objects.get(unique_id = advisor)

	app_form.level = "CLR"
	app_form.description = "Authenticated by Advisor and Passed to Clerk Office"
	notify.send(user, recipient=user, verb='Application approved by advisor and passed to department')
	app_form.save()

	context = {
			"obj":obj,
			"objtype": obj.unique_id[0:3], 
			"status": "Accepted",
			"type": "rec"
	}

	return render(request, template, context)

class accepted_application_view(ListView):
	template_name = "application_form/application_form-list.html"
	
	def get_queryset(self):
		self.app = []
		self.crt = get_object_or_404(Advisor, unique_id = self.kwargs['advisor'])
		self.appl = application_form.objects.filter(urn__hostel_no = 0)
		for a in self.appl:
			if a.level == 'CLR' or a.level == 'PGB':
				self.app.append(a)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.crt.unique_id[0:3]
		context['obj'] = self.crt
		context['app'] = self.app
		context['type'] = "acc"
		context['heading'] = "Accepted"
		return context

def reject_form_application(request, advisor, appid):
	template = "Advisor/reject.html"
	app_form = application_form.objects.get(unique_id = appid)
	#user = User.objects.get(username = app_form.urn_id)

	obj = Advisor.objects.get(unique_id = advisor)

	if request.method == "POST":
		app_form.description = request.POST.get("reject_reason")
		app_form.status = " Rejected"
		msg = 'Application rejected by advisor. Reason:' + markdown.markdown(app_form.description)
		#notify.send(user, recipient=user, verb=msg)
		app_form.save()

	context = {
			"obj":obj,
			"objtype": obj.unique_id[0:3], 
			"status": "Rejected",
			"type": "rec"
	}

	return render(request, template, context)		

class rejected_application_view(ListView):
	template_name = "application_form/application_form-list.html"
	
	def get_queryset(self):
		self.app = []
		self.crt = get_object_or_404(Advisor, unique_id = self.kwargs['advisor'])
		self.appl = application_form.objects.filter(urn__hostel_no = 0)
		for a in self.appl:
			if a.level == 'ADV' and a.status == 'Rejected':
				self.app.append(a)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.crt.unique_id[0:3]
		context['obj'] = self.crt
		context['app'] = self.app
		context['type'] = "rej"
		context['heading'] = "Rejected"
		return context


