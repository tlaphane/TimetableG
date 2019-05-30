from django.core.mail import send_mail
from django.shortcuts import HttpResponse, render, redirect
from .models import RegisteredStd, Login, RegisteredStaffs, Courses

stdnum = 1


def login(request):
    context = {
        'staff': RegisteredStaffs.objects.all(),
        'students': RegisteredStd.objects.all(),
    }
    return render(request, 'Register/Log_in.html', context)


def dummy(request, STDN):
    try:
        kep = request.POST.get('uname', False)
        stdin = int(request.POST.get('uname', False))
        stdnum = stdin
        pswin = request.POST.get('psw', False)
    except RegisteredStd.DoesNotExist:
        if (kep):
            return render(request, 'Register/Log_in.html', {'error_message': "Wrong username or password", })
        else:
            return render(request, 'Register/Log_in.html')
    else:
        return render(request, 'Register/Loggedin.html', {'STDN': STDN})


def loginconfirm(request):
    stdin = int(request.POST.get('uname', False))
    pswin = request.POST.get('psw', False)
    try:
        user = RegisteredStd.objects.get(Student_No=stdin, Password=pswin)
    except RegisteredStd.DoesNotExist:
        user = None
    if user:
        return render(request, 'Register/Loggedin.html')
    else:
        return render(request, 'Register/Loggedin.html')


def forgot(request):
    return render(request, 'Register/forgot.html')


def register(request):
    return render(request, 'Register/register.html')


def resetp(request):
    return render(request, 'Register/reset.html')


def Reg(request):
    std = request.POST.get('stdnum', False)
    na = request.POST.get('na', False)
    email = request.POST.get('email', False)
    cellnum = request.POST.get('cellnum', False)
    psw = request.POST.get('psw', False)

    a = RegisteredStd()
    a.Std_no = int(std)
    a.Name = na
    a.Email = email
    a.Password = psw
    a.Cellphone_No = int(cellnum)
    a.save()

    return render(request, 'Register/Log_in.html')


def courses(request, STDN):
    user = RegisteredStd.objects.filter(Std_no=STDN)
    course_code =Courses.objects.filter(Course_code=Course_code)
    context = {
        'user': user,
        'STDN': STDN,
    }
    return render(request, 'Register/Coursers.html', context)


def reset(request):
    try:
        psw = request.POST['newpsw']
        stdin = int(request.POST.get('uname'))
        email = request.POST.get('emailadd')
        user = RegisteredStd.object.get(Student_No=stdin, Email=email)
        user.Password = psw
        user.save()

    except RegisteredStd.DoesNotExist:
        user = None
    if user:
        return render(request, 'Register/congrats.html')
    else:
        return render(request, 'Register/reset.html', {'error_message': "Wrong email or Student"})


def logged(request):
    return render(request, 'Register/Loggedin.html')


def forgotpassword(request):
    try:
        stdin = int(request.POST.get('uname', False))
        email = request.POST.get('emailadd', False)
    except RegisteredStd.DoesNotExist:
        if (stdin):
            return render(request, 'Register/forgot.html', {'error_message': "Wrong username or password,"})
        else:
            return render(request, 'Register/forgot.html')
    else:
        subject = 'Reset your password'
        message = 'Your password is '
        from_email = 'tlaphane@gmail.com'
        to_list = ['tlaphane@gmail.com']

        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return render(request, 'Register/Log_in.html')


def staff(request, Staff_No):
    try:
        kep = request.POST.get('uname', False)
        stdin = int(request.POST.get('uname', False))
        stdnum = stdin
        pswin = request.POST.get('psw', False)
        user1 = RegisteredStaffs.object.filter(Staff_No=Staff_No)

    except RegisteredStd.DoesNotExist:
        if (kep):
            return render(request, 'Register/Log_in.html', {'error_message': "Wrong username or password,"})
        else:
            return render(request, 'Register/Log_in.html')
