from django.test import Client, TestCase
from django.urls import reverse


class PagesTests(TestCase):
    """
    Test that view by default require authentication
    """

    def setUp(self):
        self.client = Client()

    def test_landing_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_about_page(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
