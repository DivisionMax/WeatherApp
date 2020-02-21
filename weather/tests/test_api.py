from datetime import date
import logging

from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, APIClient

from rest_framework.status import (
    HTTP_200_OK,
)

from ..models import Forecast
from users.models import WeatherAppUser

logger = logging.getLogger(__name__)


class APITests(APITestCase):
    """
    Weather API endpoints
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.forecast = Forecast.objects.create(
            forecast_date=date.today(),
            min_temp=1,
            max_temp=5,
            rainfall_mm=10,
            wind_km=10,
            city='Cape Town'
        )

        # Users
        self.email = "test@gmail.com"
        self.password = "random password"
        self.user_regular = WeatherAppUser.objects.create_user(
            "regular",
            email=self.email,
            password=self.password,
        )

    def test_fetch_forecast_list(self):
        url = reverse('api:forecast-list')
        success = self.client.login(email=self.email, password=self.password)
        request = self.client.get(url)
        data = request.json()
        self.assertEquals(request.status_code, HTTP_200_OK)
        self.assertEquals(len(data), 1)


