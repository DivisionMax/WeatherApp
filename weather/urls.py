from django.urls import path

from .views import (
    ForecastListView,
    ForecastUpdateView,
)

app_name = 'weather'

urlpatterns = [
    path('', ForecastListView.as_view(), name='forecast-list'),
    path('<str:pk>/update', ForecastUpdateView.as_view(), name='forecast-update'),
]