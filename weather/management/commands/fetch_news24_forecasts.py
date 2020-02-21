from django.core.management.base import BaseCommand

from weather.services import process_news24_forecasts
from weather.utils import api_news24


class Command(BaseCommand):
    help = 'Fetches forecast data from News24 API'

    def add_arguments(self, parser):
        parser.add_argument('city_id', type=str, help='ID for the News24 city', )

    def handle(self, *args, **options):
        city_id = options['city_id']
        self.stdout.write(self.style.SUCCESS(f'Fetching city {city_id}'))
        results = api_news24.fetch_city_forecast_data(city_id=city_id,
                                                      forecast_type=api_news24.FORECAST_TYPE_15DAY)
        num_created, errors = process_news24_forecasts(forecasts=results)
        self.stdout.write(self.style.SUCCESS(f'Created {num_created} entries'))
        self.stdout.write(self.style.WARNING(f'Errors'))
        self.stdout.write(self.style.WARNING(errors))


