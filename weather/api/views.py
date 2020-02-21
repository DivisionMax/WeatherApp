from rest_framework.generics import ListAPIView

from .serializers import ForecastSerializer
from ..models import Forecast


class ForecastListView(ListAPIView):

    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

