from django.shortcuts import render

# Create your views here.

def home_view(request):
	return render(request, "home.html")

def student_view(request):
	return render(request,"student.html")

def caretaker_view(request):
	return render(request,"caretaker.html")

def advisor_view(request):
	return render(request,"advisor.html")

def hod_view(request):
	return render(request,"hod.html")

def pgblock_view(request):
	return render(request,"pgblock.html")

def prtc_view(request):
	return render(request,"prtc.html")