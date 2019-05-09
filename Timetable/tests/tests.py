from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# Create your tests here.


class TestUrls(TestCase):
    def test_login_url_resolved(self):
        url = reverse('login')

        self.assertEquals(resolve(url).func, 'login')