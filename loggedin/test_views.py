import unittest
from django.test import TestCase, Client
from django.urls import reverse, resolve

class TestViews(unittest.TestCase):
    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")
         
    def test_confirm_login(self):
        self.assertEqual('loggedin'.logg(),'Register/Log_in.html')
    
    def test_confirm_islogin(self):
        self.assertTrue('Register/Log_in.html'.islogin())


if __name__ == '__main__':
    unittest.main()
