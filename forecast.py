# coding: utf-8
import requests
import datetime

class Forecast:
  def __init__(self, forecast_response_days):
    self.timestamp = forecast_response_days['date']['epoch']
    self.weekday = forecast_response_days['date']['weekday']
    self.max_temp = forecast_response_days['high']['celsius']
    self.min_temp = forecast_response_days['low']['celsius']
    self.conditions = forecast_response_days['conditions']

  def to_text(self):
    time = datetime.datetime.fromtimestamp(int(self.timestamp))
    s_time = "%s, %s" % (self.weekday, time.strftime("%d"))
    s_max_temp = "Макс: %s °C" % self.max_temp
    s_min_temp = "Мин: %s °C" % self.min_temp
    text = """%s
%s
%s
%s
""" % (s_time, s_max_temp, s_min_temp, self.conditions )
    return text


forecast_response = requests.get('http://api.wunderground.com/api/67baf1d645fb0443/forecast/lang:RU/q/Russia/St_Petersburg.json')
forecast_response.text

result = forecast_response.json()
forecasts = result['forecast']
simple_forecast = forecasts['simpleforecast']
days_forecast = simple_forecast['forecastday']
days_forecast[1]
tomorrowForecast = Forecast(days_forecast[1])


tomorrowForecast.to_text()
# if (days_forecast and len(days_forecast) > 1 ):
#   days_forecast[1]



