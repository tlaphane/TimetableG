from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.

class TestUrls(TestCase):
    def test_login_url_resolved(self):
        from django.urls import reverse
        url = reverse('login')

        from django.urls import resolve
        from Timetable.Register.views import login
        self.assertEquals(resolve(url).func, login)