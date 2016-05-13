# coding: utf-8
import requests
import datetime

class Forecast:
  def __init__(self, forecast_response_days):
    self.timestamp = forecast_response_days['date']['epoch']
    self.weekday = forecast_response_days['date']['weekday']

  def to_text(self):
    time = datetime.datetime.fromtimestamp(int(self.timestamp))
    s_time = "%s, %s" % (self.weekday, time.strftime("%d"))
    text = """%s""" % (s_time)
    return text


forecast_response = requests.get('http://api.wunderground.com/api/67baf1d645fb0443/forecast/q/Russia/St_Petersburg.json')
forecast_response.text

result = forecast_response.json()
forecasts = result['forecast']
simple_forecast = forecasts['simpleforecast']
days_forecast = simple_forecast['forecastday']
days_forecast[1]
tomorrowForecast = Forecast(days_forecast[1])
tomorrowForecast.weekday
tomorrowForecast.to_text()
# if (days_forecast and len(days_forecast) > 1 ):
#   days_forecast[1]



