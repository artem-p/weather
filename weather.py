# coding: utf-8
import requests
import datetime
import wind

query = 'http://api.wunderground.com/api/67baf1d645fb0443/conditions/lang:RU/q/Russia/St_Petersburg.json'
current_weather_response = requests.get(query)
current_weather_response.text
current_observation = current_weather_response.json()['current_observation']
city = current_observation['display_location']['city']

time = datetime.datetime.fromtimestamp(int(current_observation['observation_epoch']))
time.strftime("%d.%m.%Y %H:%M")
weather = current_observation['weather']
temp = current_observation['temp_c']
feelslike = current_observation['feelslike_c']
wind_dir = current_observation['wind_degrees']
wind_rhumbs = wind.get_rhumbs_by_wind_dir(wind_dir)
wind_kph = current_observation['wind_kph']


sTemp = str(temp) + " °C"
sFeelslike = str(feelslike) + " °C"
city
time
weather
sTemp
sFeelslike
wind_dir
wind_rhumbs
wind_kph


def time_str_from_epoch(time_epoch):
    time_from_epoch = datetime.datetime.fromtimestamp(time_epoch)
    return time_from_epoch.strftime("%d.%m.%Y %H:%M")


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
