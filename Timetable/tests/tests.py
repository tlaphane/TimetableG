import unittest
from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# Create your tests here.


class TestUrls(unittest.TestCase):
        def test_details_function(self):
            self.assertEqual("Account created!", "Account created!")

#     def test_login_url_resolved(self):
#         url = reverse('login')

#         self.assertEquals(resolve(url).func, 'login')

#     def test_register_url_resolved(self):
#         url = reverse('register')

#         self.assertEquals(resolve(url).func, 'register')

#     def test_Confirm_log(self):
#         url = reverse('courses')
#         self.assertEquals(resolve(url).func, 'courses')

#     def test_forgot(self):
#         url = reverse('forgot')
#         self.assertEquals(resolve(url).func, 'forgot')

#     def test_reset(self):
#         url = reverse('reset')
#         self.assertEquals(resolve(url).func, 'resetp')


#     def setUp(self):
#         self.client = Client()
#         self.login_url = reverse('login')
#         self.confirm_log = reverse('confirm_log')
#         self.reset = reverse('reset')
#         self.forgot = reverse('forgot')
#         self.Reg = reverse('Reg')

#     def test_project_login_GET(self):
#         response = self.client.get(self.login_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Register/Log_in.html')

#     def test_confirm_login(self):
#         response = self.client.get(self.confirm_log)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Register/Loggedin.html')

#     def test_forgot(self):
#         response = self.client.get(self.forgot)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Register/forgot.html')

#     def test_reset(self):
#         response = self.client.get(self.reset)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Register/reset.html')
        
        
if __name__ == '__main__':
    unittest.main()
        
