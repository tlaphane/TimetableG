import unittest
from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve

#class TestViews(unittest.TestCase):
    #def test_details_function(self):
        #self.assertEqual("Account created!", "Account created!")

    #def test_confirm_login(self):
        #self.assertEqual('loggedin'.logg(), 'Register/Log_in.html')

    #def test_confirm_islogin(self):
        #self.assertTrue('Register/Log_in.html'.islogin())
class TestUrls(SimpleTestCase):
<<<<<<< HEAD

=======
>>>>>>> 3d4847838717bba30bd0d7a7d3238f63382503a1
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.confirm_log = reverse('confirm_log')
<<<<<<< HEAD

=======
        
>>>>>>> 3d4847838717bba30bd0d7a7d3238f63382503a1
    def test_views_logg_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

if __name__ == '__main__':
    unittest.main()
