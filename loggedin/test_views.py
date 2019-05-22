import unittest
from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from django.views import *

#class TestViews(unittest.TestCase):
    #def test_details_function(self):
        #self.assertEqual("Account created!", "Account created!")

    #def test_confirm_login(self):
        #self.assertEqual('loggedin'.logg(), 'Register/Log_in.html')

    #def test_confirm_islogin(self):
        #self.assertTrue('Register/Log_in.html'.islogin())
class TestUrls(SimpleTestCase):

    def test_views_logg_is_resolved(self):
        url = reverse("r'^$'")
        print(resolve(url))

if __name__ == '__main__':
    unittest.main()
