from rest_framework import serializers
from ..models import Forecast


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['forecast_date',
                  'min_temp',
                  'max_temp',
                  'rainfall_mm',
                  'wind_km',
                  'city']
