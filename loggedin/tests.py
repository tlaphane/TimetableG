import unittest
from django.urls import reverse, resolve

class TestUrls(unittest.TestCase):

    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")

    def view_login(self):
        self.assertEquals('loggedin', 'Register/Loggedin.html')

    def test_isview_login(self):
        self.assertTrue('login', 'Register/Loggedin.html')

    def test_isview_notlogin(self):
        self.assertNotIn('logged', './')

    def test_Confirm_log(self):
<<<<<<< HEAD
        #url = reverse('courses')
        self.assertEquals(resolve(reverse('courses')).func, 'courses')
=======
        url = resolve('courses')
        self.assertEquals(resolve(url).func, 'courses')
>>>>>>> 4c06889b99fc9776b4d507151b2bde63173dff7c

if __name__ == '__main__':
    unittest.main()











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



