from django.shortcuts import render
from Timetable.Courses.models import Courses
from Timetable.Log_In.models import RegisteredStd


# Create your views here.

def timetable(request, STDN):

    courses = Courses.objects.all()
    StudentRegisteredCoureses = RegisteredStd.objects.filter(Std_no = STDN)

    context = {
        'courses': courses,
        'StudentRegisteredCourses': StudentRegisteredCoureses

    }

