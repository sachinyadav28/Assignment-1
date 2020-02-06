from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student

def student_post(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})

def show(request):
    students = Student.objects.all()
    return render(request,'show.html',{'students':students})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request,'edit.html',{'student':student})

def update(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'student':student})

def delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect("/show")

    