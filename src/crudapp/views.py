from django.shortcuts import render,render
from database.models import Student
from database.forms import StudentForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        print('inside form')
        form = StudentForm(request.POST)
        print('form fetched ________')
        
        if form.is_valid():
            print('check the validity of form_____________')
            form.save()
            print('record saved ____________')
            return redirect("/crud/show")
        else:
            print('form not valid')
    else:
        form = StudentForm()
    return render(request,"crud_show.html",{'form' : form})

def show(request):
    stu = Student.objects.all()
    return render(request,"show.html",{'students':stu})