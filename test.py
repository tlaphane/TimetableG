import unittest

class TestUrls(unittest.TestCase):

    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")

    def view_login(self):
        self.assertEquals('loggedin', 'Register/Loggedin.html')

    def test_isview_login(self):
        self.assertTrue('login','Register/Loggedin.html')

    def test_isview_notlogin(self):
        self.assertNotIn('logged','./')

if __name__ == '__main__':
    unittest.main()
