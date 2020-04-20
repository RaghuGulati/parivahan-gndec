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