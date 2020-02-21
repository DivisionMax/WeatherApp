from datetime import datetime

from django.test import Client, TestCase

from ..services import process_news24_forecasts


class ForecastViewsTests(TestCase):
    """
    Test that view by default require authentication
    """

    def setUp(self):
        self.valid_1 = {
            'wind_km': 12,
            'rainfall_mm': 2,
            'max_temp': 43,
            'min_temp': 0,
            'forecast_date': datetime.now(),
            'city': 'Cape Town'
        }

        self.valid_2 = {
            'wind_km': 12,
            'rainfall_mm': 2,
            'max_temp': 43,
            'min_temp': 0,
            'forecast_date': datetime.now(),
            'city': 'Joburg'
        }

        self.invalid_1 = {
            'wind_km': 'asd',
            'rainfall_mm': 2,
            'max_temp': 43,
            'min_temp': 0,
            'forecast_date': datetime.now(),
        }

    def test_importing_forecast_data(self):
        forecasts = [self.valid_1, self.valid_2, self.invalid_1]
        added, errors = process_news24_forecasts(forecasts=forecasts)

        self.assertEqual(added, 2)
        self.assertNotEqual(len(errors), 0)
