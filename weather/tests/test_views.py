from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import login

from django.core.exceptions import PermissionDenied
from datetime import date

from ..models import Forecast
from users.models import WeatherAppUser


class ForecastViewsTests(TestCase):
    """
    Test that view by default require authentication
    """

    def setUp(self):
        self.client = Client()
        self.auth_login_url = reverse('account_login')

        self.forecast = Forecast.objects.create(
            forecast_date=date.today(),
            min_temp=1,
            max_temp=5,
            rainfall_mm=10,
            wind_km=10,
            city='Cape Town'
        )

        # Users
        self.user_regular = WeatherAppUser.objects.create_user(
            "regular",
            email="test@gmail.com",
            password="random password",
        )

        self.user_superuser = WeatherAppUser.objects.create_user(
            "superuser",
            email="super@gmail.com",
            password="random password",
            is_superuser=True,
        )

    def test_forecast_list_unauth(self):
        url = reverse('weather:forecast-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
        self.assertIn(self.auth_login_url, response.url)

    def test_forecast_edit_unauth(self):
        url = reverse('weather:forecast-update', kwargs={'pk': self.forecast.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
        self.assertIn(self.auth_login_url, response.url)

    def test_forecast_list_auth(self):
        url = reverse('weather:forecast-list')
        self.client.force_login(user=self.user_regular)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_forecast_edit_auth_regular(self):
        self.client.force_login(user=self.user_regular)
        url = reverse('weather:forecast-update', kwargs={'pk': self.forecast.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 403)

    def test_forecast_edit_auth_super(self):
        self.client.force_login(user=self.user_superuser)
        url = reverse('weather:forecast-update', kwargs={'pk': self.forecast.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
