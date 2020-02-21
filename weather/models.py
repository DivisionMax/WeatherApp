from django.db import models
from django.core.validators import MinValueValidator

from django_extensions.db.models import TimeStampedModel


class Forecast(TimeStampedModel):

    forecast_date = models.DateField(help_text='Date of forecast')
    min_temp = models.FloatField(help_text='Minimum temperature in Celsius')
    max_temp = models.FloatField(help_text='Maximum temperature in Celsius')
    rainfall_mm = models.FloatField(help_text='Rainfall in MM', validators=[MinValueValidator(0)])
    wind_km = models.FloatField(help_text='Wind speed in km/h', validators=[MinValueValidator(0)])

    city = models.TextField(help_text='City for the forecast')

    def __str__(self):
        return f'{self.city} - {self.forecast_date}'