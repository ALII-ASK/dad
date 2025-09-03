from django.shortcuts import render
from .models import Teacher, Subject


def login(request):
    teachers = Teacher.objects.all().order_by('firstname', 'lastname')
    subjects = Subject.objects.all().order_by('subject_name')
    context = {'teachers': teachers, 'subjects': subjects}
    return render(request, "login.html", context)
    
