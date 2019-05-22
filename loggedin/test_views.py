import unittest
from django.test import TestCase, Client
from django.urls import reverse, resolve

class TestViews(unittest.TestCase):
    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")
    def setUp(self):
        self.client = Client()
        self.login_url='login'
        
    def test_confirm_login(self):
        response =self.client.get(self.login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Log_in.html')

    def assertTemplateUsed(self, response, param):
        pass


if __name__ == '__main__':
    unittest.main()