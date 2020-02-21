from datetime import datetime
import logging
import re

import requests
import pytz

logger = logging.getLogger(__name__)

NEWS24_URL = "http://weather.news24.com/ajaxpro/Weather.Code.Ajax,Weather.ashx"

FORECAST_TYPE_15DAY = "GetForecast15DayExpanded"
FORECAST_TYPE_7DAY = "GetForecast7Day"

DURBAN = "77062"
CAPE_TOWN = "77107"

pytz_za = pytz.timezone("Africa/Johannesburg")


def _convert_str_to_float(input_value):
    """
    Converts a suspected string float to float
    Defaults to 0
    """
    try:
        value = float(input_value)
    except ValueError:
        logger.warning(f'Value, {input_value}, could not be cast to float')
        value = 0
    return value


def fetch_city_forecast_data(city_id=None, forecast_type=None):
    if not city_id:
        raise Exception('No city id provided')

    if not forecast_type:
        forecast_type = FORECAST_TYPE_15DAY

    headers = {"X-AjaxPro-Method": forecast_type}
    payload = {"cityId": city_id}
    response = requests.post(NEWS24_URL, json=payload, headers=headers)
    output = response.json()
    city = output["value"]["CityName"]
    forecasts = output["value"]["Forecasts"]

    processed_forecasts = []

    for cast in forecasts:
        wind_km = _convert_str_to_float(cast["WindSpeed"])
        rainfall_raw = cast["Rainfall"].lower().replace('mm', '')
        rainfall = _convert_str_to_float(rainfall_raw)
        max_temp_c = _convert_str_to_float(cast["HighTemp"])
        low_temp_c = _convert_str_to_float(cast["LowTemp"])

        forecast_date = re.findall("\d+", cast["Date"])[0]
        ts = int(forecast_date) / 1000
        ts = datetime.utcfromtimestamp(ts)
        za_ts = pytz.utc.localize(ts, is_dst=None).astimezone(pytz_za)

        data = {
            'wind_km': wind_km,
            'rainfall_mm': rainfall,
            'max_temp': max_temp_c,
            'min_temp': low_temp_c,
            'forecast_date': za_ts,
            'city': city
        }

        processed_forecasts.append(data)

    return processed_forecasts


