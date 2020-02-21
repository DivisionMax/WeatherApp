from django.urls import reverse

from .models import Forecast

from core.views import AuthListView, AdminUpdateView


class ForecastListView(AuthListView):

    model = Forecast
    paginate_by = 3

    context_object_name = 'forecasts'


class ForecastUpdateView(AdminUpdateView):
    model = Forecast
    template_name_suffix = '_update'

    fields = ['min_temp', 'max_temp', 'rainfall_mm', 'wind_km', 'city']

    def get_success_url(self):
        return reverse('weather:forecast-list')
