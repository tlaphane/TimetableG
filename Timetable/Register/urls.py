from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.login, name ='login'),
    url(r'^register', views.register, name ='register'),
    url(r'^reg', views.Reg, name='Reg'),
    url(r'^logged', views.login, name='Logged'),
    url(r'^courses', views.courses, name='courses'),
    url(r'^forgot', views.forgot, name='forgot'),
    url(r'^reset-password', views.resetp, name='reset'),
    url(r'^(?P<STDN>[0-9]+)/announcement', views.astudent, name='stdn'),
    url(r'^(?P<STDN>[0-9]+)/courses', views.courses, name='stdn'),
    url(r'^(?P<STDN>[0-9]+)', views.dummy, name='sdtn'),
    url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses, name='Staff'),
    url(r'^staff(?P<Staff_No>[0-9]+)/announcement', views.astaff, name='Staff'),
    url(r'^staff(?P<Staff_No>[0-9]+)/make_announcement', views.make, name='Staff'),
    url(r'^staff(?P<Staff_No>[0-9]+)/made_announcement', views.makeAnnouncement, name='Staff'),
    url(r'^staff(?P<Staff_No>[0-9]+)', views.staff, name='Staff'),
]

