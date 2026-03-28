from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student

@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard/index.html', {'students': students})

@login_required
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        return redirect('/')
    return render(request, 'dashboard/add.html')

@login_required
def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.save()
        return redirect('/')
    return render(request, 'dashboard/edit.html', {'student': student})

@login_required
def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('/')