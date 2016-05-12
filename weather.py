# coding: utf-8
import requests
import datetime
import wind

class CurrentWeather:
  def __init__(self, current_weather_json):
    self.json_weather = current_weather_json

  def parse(self):
    # parse response result
    current_weather.city = None
    current_weather.time = None
    current_weather.conditions = None
    current_weather.temp = None
    current_weather.feelslike = None
    current_weather.wind_dir = None
    current_weather.wind_kph = None
    if self.json_weather:
      current_observation = self.json_weather['current_observation']
    pass

  def to_text(self):
    # Преобразуем в текст для вывода
    self.parse()
    self.wind = wind.Wind(self.wind_kph, self.wind_dir)
    textPart = """%s
%s
%s
Температура: %d °C
Ощущается как: %d °C
Ветер: """ %(self.city, self.time, self.conditions, self.temp, self.feelslike)
    text = textPart + self.wind.to_text()
    return text

# if __name__ == "__main__":
query = 'http://api.wunderground.com/api/67baf1d645fb0443/conditions/lang:RU/q/Russia/St_Petersburg.json'
current_weather_response = requests.get(query)
current_weather_response.json()['current_observation']
# current_weather_response.text

current_weather = CurrentWeather(current_weather_response.json())
current_weather.json_weather
# current_observation = current_weather.json_weather['current_observation']
current_weather.to_text()



# current_weather = CurrentWeather(None)
# current_weather.city = "Санкт-Петербург"
# current_weather.time = "2016-05-12 14:30"
# current_weather.conditions = "Ясно"
# current_weather.temp = 14
# current_weather.feelslike = 14
# current_weather.wind_dir = 130
# current_weather.wind_kph = 11
# current_weather.to_text()

def get_current_weather():
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
  wind_mps = wind.get_mps_by_kph(wind_kph)
  wind_mps_formatted = wind.format_wind_mps(wind_mps)


  sTemp = str(temp) + " °C"
  sFeelslike = str(feelslike) + "  "
  city
  time
  weather
  sTemp
  sFeelslike
  wind_dir
  wind_rhumbs
  wind_kph
  wind_mps
  wind.format_wind_mps(wind_mps)

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
