from django.test import TestCase

# Create your tests here.
import unittest
from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.conf.urls import url
from loggedin import urls, views

# Create your tests here.


class TestUrls(unittest.TestCase):

    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")

    def test_login_url_function(self):
        url_test = [
            url(r'^$', views.logg, name='login'),
            url(r'^forgot', views.forgot, name='Forgot'),
        ]
        self.assertEquals(url_test, urls.urlpatterns)

    def test_Confirm_log(self):
        url = reverse('courses')
        self.assertEquals(resolve(url).func, 'courses')

if __name__ == '__main__':
    unittest.main()

# def test_register_url_resolved(self):
#    url = reverse('register')

#   self.assertEquals(resolve(url).func, 'register')

# def test_Confirm_log(self):
#   url = reverse('courses')
#  self.assertEquals(resolve(url).func, 'courses')

# def test_forgot(self):
#    url = reverse('forgot')
#   self.assertEquals(resolve(url).func, 'forgot')



