from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teachers')

    context = {
        'students': students,
        'object_list': Student.objects.all(),
    }





   return render(request, template, context)
