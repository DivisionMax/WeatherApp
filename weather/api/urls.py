from django.conf.urls import url

from .views import AthleteView

urlpatterns = [
    url('forecasts', view=AthleteView.as_view(), name='api-athlete'),
]
