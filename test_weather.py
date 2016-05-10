import weather
def test_time_from_epoch():
    time_epoch = 1462644000
    assert weather.time_str_from_epoch(time_epoch) == "07.05.2016 21:00"
    time_epoch = 1462656600
    assert weather.time_str_from_epoch(time_epoch) == "08.05.2016 00:30"
