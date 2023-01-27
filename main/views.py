from django.shortcuts import render, redirect, HttpResponse

from .models import Student
from .forms import StudentForm


def index(request):
    student = Student.objects.all()
    return render(request, 'main/index.html', {'student': student})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            return HttpResponse('Error')

    form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'main/create_student.html', context)


def student_update(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('main:index')

        return HttpResponse('Error')

    form = StudentForm(instance=student)

    context = {
        'form': form
    }
    return render(request, 'main/create_student.html', context)


def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('main:index')
