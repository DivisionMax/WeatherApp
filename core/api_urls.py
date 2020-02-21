from django.urls import path, include
from django.conf.urls import url

from rest_framework_swagger.views import get_swagger_view
from weather.api import views as weather_views

schema_view = get_swagger_view(title='Weather API')

app_name = 'api'

urlpatterns = [
    path('forecasts/', weather_views.ForecastListView.as_view(), name='forecast-list'),
    path('swagger-ui/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
