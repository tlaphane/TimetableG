import smtplib

from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from Announcements.models import Announcements
from Courses.models import Courses
from Log_In.models import Lecturer,RegisteredStaffs, RegisteredStd, StudentsRegister
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from Announcements.forms import AnnouncementsForm

# Create your views here.
def makeAnnouncement(request, Staff_No):

    Subject = request.POST['Title']
    Course_Code = request.POST.get('Course Code')

    Content = request.POST['message']



    a = Announcements()
    q = Courses.objects.get(Course_Code=Course_Code[-8:])
    a.Course_Code = q

    p = Lecturer.objects.get(Lect_No=Staff_No)
    a.Lect_No = p

    a.Title = Subject
    a.Content = Content

    a.save()


    TO = []
    arr = RegisteredStd.objects.filter(Course_Code=Course_Code[-8:])
    print(arr)
    for i in arr:
        #print(i.Std_no)
        j = StudentsRegister.objects.filter(Student_No=i.Std_no)
        print(j)
        for k in j:
            print(k.Email)
            if k.Email not in TO:
                TO.append(k.Email)
    print(TO)




    print(Course_Code)

    send_mail(Subject, Content, 'timetablegen@gmail.com', TO, fail_silently=False)

    print('email sent')

    print("Done")
    return render(request, 'Register/Announcement.html')

def make(request,Staff_No):
    print(Staff_No)
    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)

    print(user)
    context = {
        'user': user,
        'STDN': Staff_No,

    }
    return render(request, 'Register/Make_Announcement.html',context)

def upload(request,Staff_No):
    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)
    if request.method == 'POST':
        form = AnnouncementsForm(request.POST or None,request.FILES or None)
        if form.is_valid():

            Subject = request.POST['Title']
            Course_Code = request.POST['Course_Code']

            Content = request.POST['Content']

            PDF = str(request.FILES.get('pdf',False))

            if PDF=="False":
                PDF=""
            else:
                PDF='http://127.0.0.1:8000/media/announcements/pdfs/'+ PDF



            TO = []
            arr = RegisteredStd.objects.filter(Course_Code=Course_Code[-8:])
            print(arr)
            for i in arr:
                # print(i.Std_no)
                j = StudentsRegister.objects.filter(Student_No=i.Std_no)
                print(j)
                for k in j:
                    print(k.Email)
                    if k.Email not in TO:
                        TO.append(k.Email)
            print(TO)

            print(Course_Code)

            send_mail(Subject, Content + '\n'+ '\n' + PDF, 'timetablegen@gmail.com', TO, fail_silently=False)
            print(PDF)
            print('email sent')
            form.save()



            context = {
                'user': user,
                'STDN': Staff_No,

            }
            # return redirect('Register/Try.html')
            return render(request, 'Register/Announcement.html',context)
    else:
        form = AnnouncementsForm()

    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)
    context = {
        'form': form,
        'STDN': Staff_No,
        'user': user,

    }
    return render(request, 'Register/Try.html', context)