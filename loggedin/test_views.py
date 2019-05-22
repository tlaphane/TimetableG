import unittest
from django.test import TestCase, Client
from django.urls import reverse, resolve

class TestViews(unittest.TestCase):
    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")
         
    def test_confirm_login(self):
        self.assertEqual('login','Register/Log_in.html')


if __name__ == '__main__':
    unittest.main()