# coding: utf-8
import requests
import datetime

query = 'http://api.wunderground.com/api/67baf1d645fb0443/conditions/lang:ru/q/Russia/St_Petersburg.json'
current_weather_response = requests.get(query)
current_weather_response.text
current_observation = current_weather_response.json()['current_observation']
city = current_observation['display_location']['city']

time = datetime.datetime.fromtimestamp(1462644000)
time.strftime("%d.%m.%Y %H:%M")


def time_str_from_epoch(time_epoch):
    time_from_epoch = datetime.datetime.fromtimestamp(time_epoch)
    return time_from_epoch.strftime("%d.%m.%Y %H:%M")


def test_time_from_epoch():
    time_epoch = 1462644000
    assert time_str_from_epoch(time_epoch) == "07.05.2016 21:00"
    time_epoch = 1462656600
    assert time_str_from_epoch(time_epoch) == "08.05.2016 00:30"

# Сделать из метки нормальное время с юнит-тестом
# "observation_epoch":"1462644000",
# "observation_time_rfc822":"Sat, 07 May 2016 21:00:00 +0300",

# Прогноз
# forecast_response = requests.get('http://api.wunderground.com/api/67baf1d645fb0443/forecast/q/Russia/St_Petersburg.json')
# forecast_response.text

# result = forecast_response.json()
# forecasts = result['forecast']
# simple_forecast = forecasts['simpleforecast']
# days_forecast = simple_forecast['forecastday']

# for day_forecast in days_forecast:
#   year = day_forecast['date']['year']
#   month = day_forecast['date']['month']

# year
