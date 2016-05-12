import weather
import wind

def test_time_from_epoch():
    time_epoch = 1462644000
    assert weather.time_str_from_epoch(time_epoch) == "07.05.2016 21:00"
    time_epoch = 1462656600
    assert weather.time_str_from_epoch(time_epoch) == "08.05.2016 00:30"


def test_get_wind_rhumbs():
  check_wind_rhumbs(360, None)
  check_wind_rhumbs(0, "С")
  check_wind_rhumbs(359, "С")
  check_wind_rhumbs(1, "С")
  check_wind_rhumbs(180, "Ю")
  check_wind_rhumbs(90, "В")
  check_wind_rhumbs(270, "З")
  check_wind_rhumbs(25, "СВ")
  check_wind_rhumbs(136, "ЮВ")
  check_wind_rhumbs(216, "ЮЗ")
  check_wind_rhumbs(301, "СЗ")


def check_wind_rhumbs(wd, rhumbs_expected):
  cur_wind = wind.Wind(1, wd)
  assert cur_wind.to_rhumbs() == rhumbs_expected


def test_mps_by_kph():
  cur_wind = wind.Wind(0, 0)
  assert cur_wind.get_mps_by_kph(7) == 1.9444460000000001
  assert cur_wind.get_mps_by_kph(10) == 2.7777800000000004
  assert cur_wind.get_mps_by_kph(60) == 16.666680000000003


def test_format_wind_mps():
  cur_wind = wind.Wind(0, 0)
  assert cur_wind.format_wind_mps(3.8888920000000002) == "3.9"
  assert cur_wind.format_wind_mps(1.9444460000000001) == "1.9"
  assert cur_wind.format_wind_mps(2.7777800000000004) == "2.8"
  assert cur_wind.format_wind_mps(16.666680000000003) == "16.7"


def test_wind_output():
  cur_wind = wind.Wind(0, 0)
  assert cur_wind.to_text () == """С
0.0 м/с"""

  cur_wind = wind.Wind(10, 90)
  assert cur_wind.to_text () == """В
2.8 м/с"""

  cur_wind = wind.Wind(7, 216)
  assert cur_wind.to_text () == """ЮЗ
1.9 м/с"""

  cur_wind = wind.Wind(60, 301)
  assert cur_wind.to_text () == """СЗ
16.7 м/с"""
