#from django.shortcuts import render
from django.shortcuts import *
from database.models import *
from database.forms import *
from datetime import datetime
from django.db.models import *
from django.views.generic import(
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
	)
from django.http import HttpResponse
import notifications as nf
from django.contrib.auth.models import User
import datetime

def student_navbar(request, urno):
	obj = Student.objects.get(urn = urno)
	template = 'Student/navbar.html'

	context = {
			"obj":obj,
			"nons":4,
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

	ct = application_form.objects.all().aggregate(Max('unique_id'))
	uid = int(ct['unique_id__max']) + 1
	form_obj = application_form.objects.filter(urn = urno)

	x = datetime.datetime.now().month

	if x >= 1 and x <= 3:
		y = datetime.date(2020, 1, 1)
		z = datetime.date(2020, 3, 31)

	elif x >= 4 and x <= 6:
		y = datetime.date(2020, 4, 1)
		z = datetime.date(2020, 6, 30)
	    
	elif x >= 7 and x <= 9:
		y = datetime.date(2020, 7, 1)
		z = datetime.date(2020, 9, 30)

	elif x >= 10 and x <= 12:
		y = datetime.date(2020, 10, 1)
		z = datetime.date(2020, 12, 31)

	for aobj in form_obj:
		if aobj.status == "Rejected":
			aobj.delete()

	if form_obj.exists():
		if (form_obj[0].level == '0' and form_obj[0].status == "To be Renewed"):
			if request.method == "POST":
				paas.unique_id = "888" + '{:03}'.format(uid)
				paas.urn = obj
				paas.depo_name = request.POST.get("depo")
				paas.location_from = request.POST.get("loc_from")
				paas.location_to = request.POST.get("loc_to")
				paas.period_from = y
				paas.period_to = z
				paas.old_pass_no = request.POST.get("oldpassno")
				paas.level = "ADV"
				paas.status = "Accepted"
				paas.description = "Form filled by student"
				paas.save()
		else:
			return HttpResponse("<h1>You have already applied for bus pass</h1>")
	else:
		if request.method == "POST":
				paas.unique_id = "888" + '{:03}'.format(uid)
				paas.urn = obj
				paas.depo_name = request.POST.get("depo")
				paas.location_from = request.POST.get("loc_from")
				paas.location_to = request.POST.get("loc_to")
				paas.period_from = y 
				paas.period_to = z
				paas.old_pass_no = request.POST.get("oldpassno")
				paas.level = "ADV"
				paas.status = "Accepted"
				paas.description = "Form filled by student"
				paas.save()

	context = {
			"obj": obj,
			}

	return render(request, template, context)

class display_notifications(ListView):
	template_name = "Student/notifications.html"

	def get_queryset(self):
		self.obj = get_object_or_404(Student, urn = self.kwargs['urno'])	
		self.user = User.objects.get(username = self.kwargs['urno'])
		self.notifics = nf.models.Notification.objects.filter(actor_object_id = self.user.id)
		self.notifics.mark_all_as_read()
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['obj'] = self.obj
		context['notifications'] = self.notifics

		return context

def complaint_advisor(request, urno):
	obj = Student.objects.get(urn = urno)
	template = "Student/complaint.html"
	complaint = student_complaint()

	if request.method == "POST":
		complaint.urn = obj
		complaint.complaint_message = request.POST.get("complaint")
		complaint.save()

	context = {
			"obj":obj,
	}

	return render(request, template, context)
