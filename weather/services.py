import logging

from .forms import ForecastForm

logger = logging.getLogger(__name__)


def process_news24_forecasts(forecasts=None):
    """
    Persists valid forecast data from News24 to Forecast instances
    :param forecasts:
    :return:
    """
    if not forecasts:
        forecasts = []

    records_added = 0
    errors = []

    for forecast_data in forecasts:
        form = ForecastForm(forecast_data)
        # Check to see if the row data is valid.
        if form.is_valid():
            # Row data is valid so save the record.
            form.save()
            records_added += 1
            logger.info('Created')
            logger.info(form)
        else:
            logger.warning('Form is not valid')
            errors.append(form.errors)

    return records_added, errors
