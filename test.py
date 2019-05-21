import unittest
from loggedin import views


class TestUrls(unittest.TestCase):

    def test_details_function(self):
        self.assertEqual("Account created!", "Account created!")

    def view_login(self):
        self.assertEquals('loggedin'.logg(), 'Register/Loggedin.html')

    def test_isview_login(self):
        self.assertTrue('loggedin'.islogg())
        self.assertFalse('LOGGEDIN'.islogg())

if __name__ == '__main__':
    unittest.main()