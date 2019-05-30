from django.conf.urls import url
from Register import views


urlpatterns = [

    url(r'^$', views.login, name='login'),

    url(r'^register', views.register, name='register'),

    url(r'^reg', views.Reg, name='Reg'),

    url(r'^logged', views.login, name='confirm_log'),

    url(r'^forgot', views.forgot, name='forgot'),

    url(r'^(?P<STDN>[0-9]+)/courses', views.courses, name='course'),

    url(r'^(?P<STDN>[0-9]+)', views.dummy, name='dum'),

    url(r'^staff(?P<Staff_No>[0-9]+)', views.staff, name='s'),

]