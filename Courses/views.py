from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponse, render, redirect
from .models import Courses
from Log_In.models import StudentsRegister, Lecturer, RegisteredStaffs, RegisteredStd
from Courses.models import Courses

from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def courses(request, STDN):
    print("inside function")

    user = RegisteredStd.objects.filter(Std_no=STDN)
    course = Courses.objects.all()

    context = {
        'user': user,
        'STDN': STDN,
        'course': course
    }
    print("inside function")

    for i in user:
        print(i.Course_Code)
    # simple_upload(request)

    return render(request, 'Register/Courses.html', context)


def StaffCourses(request, Staff_No):
    print("inside function")

    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)
    course = Courses.objects.all()

    print("below s")
    context = {
        # 'form': form,
        'user': user,
        'STDN': Staff_No,
        'course': course

    }
    print("inside function")

    for i in user:
        print(i.Course_Code)

    return render(request, 'Register/Courses.html', context)
