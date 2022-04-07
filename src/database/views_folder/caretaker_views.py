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

def crt_navbar(request, urno):
	obj = CareTaker.objects.get(unique_id = urno)
	template = 'navbar.html'

	context = {
			"obj":obj,
			"objtype":obj.unique_id[0:3]
	}

	return render(request, template, context)

def caretaker_details(request, urno):
	obj = CareTaker.objects.get(unique_id = urno)
	template = 'CareTaker/view_details.html'

	context = {
			"obj":obj,
			"objtype": obj.unique_id[0:3] 

	}

	return render(request, template, context)	

class stdlist(ListView):
	template_name = "Student/student_list.html"

	def get_queryset(self):
		self.crt = get_object_or_404(CareTaker, unique_id = self.kwargs['crt'])
		self.std = Student.objects.filter(hostel_no = self.crt.hostel_no)
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in the publisher
		context['objtype'] = self.crt.unique_id[0:3]
		context['obj'] = self.crt
		context['std'] = self.std
		return context	
