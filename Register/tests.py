import unittest
from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.conf.urls import url
from django.test import  TestCase
from loggedin import urls


# Create your tests here.
class UrlTestCase(TestCase):
    def setUp(self):
        url.objects.create(name="login", page="loggedin")
        url.objects.create(name="Notlogged", page="loggedoff")

    def test_url_loggedin(self):
        login = url.objects.create(name="login")
        Notlogged = url.objects.create(name="Notlogged")

if __name__ == '__init__':
    unittest.init()

    def test_login_url_resolve(self):
        url_test = reverse('loggedin'),
        self.assertEquals(url_test, url.urlpatterns)
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    #def test_Confirm_log(self):
     #   url = reverse('courses')
      #  self.assertEquals(resolve(url).func, 'courses')

            #url(r'^register', views.register, name='Register'),
            #url(r'^reg', views.Reg, name='Reg'),
            #url(r'^logged', views.login, name='Logged'),
            #url(r'^courses', views.courses, name='Courses'),
            #url(r'^forgot', views.forgot, name='Forgot'),
            #url(r'^reset-password', views.resetp, name='Reset-Password'),
            #url(r'^(?P<STDN>[0-9]+)/announcement', views.astudent, name='stdn'),
            #url(r'^(?P<STDN>[0-9]+)/courses', views.courses, name='stdn'),
            #url(r'^(?P<STDN>[0-9]+)', views.dummy, name='sdtn'),
            #url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses, name='Staff'),
            #url(r'^staff(?P<Staff_No>[0-9]+)/announcement', views.astaff, name='Staff'),
            #url(r'^staff(?P<Staff_No>[0-9]+)/make_announcement', views.make, name='Staff'),
            #url(r'^staff(?P<Staff_No>[0-9]+)/made_announcement', views.makeAnnouncement, name='Staff'),
            #url(r'^staff(?P<Staff_No>[0-9]+)', views.staff, name='Staff'),

        #]

        #self.assertEquals(url_test, urls.urlpatterns)


#if __name__ == '__main__':
 #   unittest.main()

# def test_register_url_resolved(self):
#    url = reverse('register')

#   self.assertEquals(resolve(url).func, 'register')

# def test_Confirm_log(self):
#   url = reverse('courses')
#  self.assertEquals(resolve(url).func, 'courses')

# def test_forgot(self):
#    url = reverse('forgot')
#   self.assertEquals(resolve(url).func, 'forgot')



