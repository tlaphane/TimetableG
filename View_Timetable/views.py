from django.shortcuts import render
from Courses.models import Courses
from Log_In.models import RegisteredStd, RegisteredStaffs


# Create your views here.

def timetable(request, STDN):
    courses = Courses.objects.all()
    StudentRegisteredCoureses = RegisteredStd.objects.filter(Std_no=STDN)

    context = {
        'courses': courses,
        'StudentRegisteredCourses': StudentRegisteredCoureses

    }

    return render(request, 'Register/Timetable.html', context)


def timetableStaff(request, Staff_No):
    courses = Courses.objects.all()
    StudentRegisteredCoureses = RegisteredStaffs.objects.filter(Staff_no=Staff_No)

    context = {
        'courses': courses,
        'StudentRegisteredCourses': StudentRegisteredCoureses

    }

    return render(request, 'Register/Timetable.html', context)
