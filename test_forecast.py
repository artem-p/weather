import forecast

fcst = forecast.Forecast({'avewind': {'dir': 'SE', 'mph': 15, 'kph': 24, 'degrees': 146}, 'qpf_allday': {'in': 0.0, 'mm': 0}, 'skyicon': '', 'maxwind': {'dir': 'SE', 'mph': 20, 'kph': 32, 'degrees': 146}, 'date': {'tz_long': 'Europe/Moscow', 'weekday': 'Saturday', 'pretty': '7:00 PM MSK on May 14, 2016', 'month': 5, 'ampm': 'PM', 'epoch': '1463241600', 'min': '00', 'year': 2016, 'tz_short': 'MSK', 'sec': 0, 'day': 14, 'monthname': 'May', 'hour': 19, 'monthname_short': 'May', 'yday': 134, 'weekday_short': 'Sat', 'isdst': '0'}, 'qpf_day': {'in': 0.0, 'mm': 0}, 'low': {'celsius': '8', 'fahrenheit': '47'}, 'icon': 'clear', 'conditions': 'Clear', 'minhumidity': 0, 'icon_url': 'http://icons.wxug.com/i/c/k/clear.gif', 'snow_night': {'in': 0.0, 'cm': 0.0}, 'snow_day': {'in': 0.0, 'cm': 0.0}, 'qpf_night': {'in': 0.0, 'mm': 0}, 'snow_allday': {'in': 0.0, 'cm': 0.0}, 'pop': 0, 'avehumidity': 38, 'period': 2, 'high': {'celsius': '21', 'fahrenheit': '70'}, 'maxhumidity': 0})
fcst.to_text()

def test_forecast_to_text():
  fcst = forecast.Forecast({'avewind': {'dir': 'SE', 'mph': 15, 'kph': 24, 'degrees': 146}, 'qpf_allday': {'in': 0.0, 'mm': 0}, 'skyicon': '', 'maxwind': {'dir': 'SE', 'mph': 20, 'kph': 32, 'degrees': 146}, 'date': {'tz_long': 'Europe/Moscow', 'weekday': 'Saturday', 'pretty': '7:00 PM MSK on May 14, 2016', 'month': 5, 'ampm': 'PM', 'epoch': '1463241600', 'min': '00', 'year': 2016, 'tz_short': 'MSK', 'sec': 0, 'day': 14, 'monthname': 'May', 'hour': 19, 'monthname_short': 'May', 'yday': 134, 'weekday_short': 'Sat', 'isdst': '0'}, 'qpf_day': {'in': 0.0, 'mm': 0}, 'low': {'celsius': '8', 'fahrenheit': '47'}, 'icon': 'clear', 'conditions': 'Clear', 'minhumidity': 0, 'icon_url': 'http://icons.wxug.com/i/c/k/clear.gif', 'snow_night': {'in': 0.0, 'cm': 0.0}, 'snow_day': {'in': 0.0, 'cm': 0.0}, 'qpf_night': {'in': 0.0, 'mm': 0}, 'snow_allday': {'in': 0.0, 'cm': 0.0}, 'pop': 0, 'avehumidity': 38, 'period': 2, 'high': {'celsius': '21', 'fahrenheit': '70'}, 'maxhumidity': 0})
  assert fcst.to_text() == """Saturday, 14
Макс: 21 °C
Мин: 8 °C
Clear"""

  fcst = forecast.Forecast({u'avehumidity': 48, u'maxhumidity': 0, u'avewind': {u'kph': 19, u'degrees': 158, u'dir': u'\u042e\u042e\u0412', u'mph': 12}, u'icon_url': u'http://icons.wxug.com/i/c/k/chancerain.gif', u'snow_allday': {u'cm': 0.0, u'in': 0.0}, u'maxwind': {u'kph': 24, u'degrees': 158, u'dir': u'\u042e\u042e\u0412', u'mph': 15}, u'minhumidity': 0, u'period': 2, u'pop': 50, u'skyicon': u'', u'high': {u'fahrenheit': u'65', u'celsius': u'18'}, u'qpf_night': {u'mm': 0, u'in': 0.0}, u'qpf_allday': {u'mm': 2, u'in': 0.08}, u'low': {u'fahrenheit': u'43', u'celsius': u'6'}, u'snow_night': {u'cm': 0.0, u'in': 0.0}, u'date': {u'tz_short': u'MSK', u'weekday_short': u'\u041f\u043d', u'isdst': u'0', u'monthname': u'\u041c\u0430\u0439', u'hour': 19, u'min': u'00', u'ampm': u'PM', u'tz_long': u'Europe/Moscow', u'month': 5, u'epoch': u'1463414400', u'sec': 0, u'weekday': u'\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', u'pretty': u'16 05, 2016 19:00 MSK', u'year': 2016, u'yday': 136, u'day': 16, u'monthname_short': u'\u041c\u0430\u0439'}, u'snow_day': {u'cm': 0.0, u'in': 0.0}, u'qpf_day': {u'mm': 2, u'in': 0.08}, u'conditions': u'\u0432\u043e\u0437\u043c\u043e\u0436\u0435\u043d \u0434\u043e\u0436\u0434\u044c', u'icon': u'chancerain'})
  assert fcst.to_text() == """Понедельник, 16
Макс: 18 °C
Мин: 6 °C
возможен дождь"""
  pass
