from django.contrib import admin

from .models import Forecast


class ForecastAdmin(admin.ModelAdmin):

    list_display = ['city', 'forecast_date', 'min_temp', 'max_temp', 'rainfall_mm', 'wind_km']
    list_filter = ['city']


admin.site.register(Forecast, ForecastAdmin)


