import unittest
from django.test import TestCase, Client
from django.urls import reverse, resolve

class TestViews(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')

    def test_project_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Log_in.html')


if __name__ == '__main__':
    unittest.main()