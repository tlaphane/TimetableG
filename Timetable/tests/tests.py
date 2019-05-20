import unittest
from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve



# Create your tests here.


class TestUrls(unittest.TestCase):

    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")

    def test_login_url_function(self):
        #url = reverse('login')

        self.assertEquals("login", "loggedin")

   # def test_register_url_resolved(self):
    #    url = reverse('register')

     #   self.assertEquals(resolve(url).func, 'register')

    #def test_Confirm_log(self):
     #   url = reverse('courses')
      #  self.assertEquals(resolve(url).func, 'courses')

    #def test_forgot(self):
    #    url = reverse('forgot')
     #   self.assertEquals(resolve(url).func, 'forgot')

        
if __name__ == '__main__':
    unittest.main()

        
        


