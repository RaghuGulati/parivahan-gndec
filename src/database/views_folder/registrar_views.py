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

from django_filters.views import FilterView
from django_tables2.views import *
from database.filters import *
from django.db.models.signals import post_save
from notifications.signals import notify
from django.contrib.auth.models import User

from database.utils import render_to_pdf

# Create your views here.
def reg_navbar(request, uid):
	obj = registrar.objects.get(unique_id = uid)
	template = 'navbar.html'

	context = {
			"obj":obj,
			"objtype": obj.unique_id[0:3] 
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
		self.rar = get_object_or_404(registrar, unique_id = self.kwargs['uid'])
		self.appl = application_form.objects.filter(level = "ARar", urn__hostel_no = 0)
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['objtype'] = self.rar.unique_id[0:3]
		context['obj'] = self.rar
		context['app'] = self.appl
		context['type'] = "rec"
		context['heading'] = "Recommended"
		return context

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


class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		app_form = get_object_or_404(application_form, unique_id = self.kwargs['appid'])
		user = User.objects.get(username = app_form.urn_id)
		app_form.level = "Done"
		app_form.description = "Approved by assistant registrar"
	
		notify.send(user, recipient=user, verb='Application Approved by Assistant Registrar you can now collect it')
		app_form.save()
		data = {
						"application": app_form,
				}

		pdf = render_to_pdf('application_form/bus_pass_pdf.html', data)
		return HttpResponse(pdf, content_type='application/pdf')