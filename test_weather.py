import weather
import wind

def test_time_from_epoch():
    time_epoch = 1462644000
    assert weather.time_str_from_epoch(time_epoch) == "07.05.2016 21:00"
    time_epoch = 1462656600
    assert weather.time_str_from_epoch(time_epoch) == "08.05.2016 00:30"


def test_get_wind_rhumbs():
  assert wind.get_rhumbs_by_wind_dir(360) == None
  assert wind.get_rhumbs_by_wind_dir(0) == "С"
  assert wind.get_rhumbs_by_wind_dir(359) == "С"
  assert wind.get_rhumbs_by_wind_dir(1) == "С"
  assert wind.get_rhumbs_by_wind_dir(180) == "Ю"
  assert wind.get_rhumbs_by_wind_dir(90) == "В"
  assert wind.get_rhumbs_by_wind_dir(270) == "З"
  assert wind.get_rhumbs_by_wind_dir(25) == "СВ"
  assert wind.get_rhumbs_by_wind_dir(136) == "ЮВ"
  assert wind.get_rhumbs_by_wind_dir(216) == "ЮЗ"
  assert wind.get_rhumbs_by_wind_dir(301) == "СЗ"
