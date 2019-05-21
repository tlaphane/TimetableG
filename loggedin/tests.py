from django.test import TestCase

# Create your tests here.
import unittest
from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.conf.urls import url

# Create your tests here.



class TestUrls(unittest.TestCase):

    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")

    def test_login_url_resolve(self):
        url_test = reverse('loggedin'),

        self.assertEquals(url_test, url.urlpatterns)

if __name__ == '__init__':
    unittest.init()

















#class TestUrls(unittest.TestCase):

   # def test_details_function(self):
        #self.assertEqual("Account created!", "Account created!")

#if __name__ == '__main__':
 #   unittest.main()

    #def test_login_url_resolve(self):
     #   url_test = reverse('loggedin'),

     #   self.assertEquals(url_test, url.urlpatterns)

    #def test_Confirm_log(self):
     #   url = reverse('courses')
      #  self.assertEquals(resolve(url).func, 'courses')

#if __name__ == '__main__.TestUrls':
    #unittest.main()

# def test_register_url_resolved(self):
#    url = reverse('register')

#   self.assertEquals(resolve(url).func, 'register')

# def test_Confirm_log(self):
#   url = reverse('courses')
#  self.assertEquals(resolve(url).func, 'courses')

# def test_forgot(self):
#    url = reverse('forgot')
#   self.assertEquals(resolve(url).func, 'forgot')



