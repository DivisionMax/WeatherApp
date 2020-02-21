from .models import Forecast
from django.forms import ModelForm


class ForecastForm(ModelForm):

    class Meta:
        model = Forecast
        fields = ['forecast_date',
                  'min_temp',
                  'max_temp',
                  'rainfall_mm',
                  'wind_km',
                  'city'
                  ]
