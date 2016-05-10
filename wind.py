def get_rhumbs_by_wind_dir(wd):
    #   Получаем направление ветра в румбах по градусам
    WD_MIN = 0
    WD_MAX = 359

    NORTH_MIN = 338
    NORTH_MAX = 23
    NORTH_TEXT = "С"

    NORTH_OST_MIN = 24
    NORTH_OST_MAX = 67
    NORTH_OST_TEXT = "СВ"

    OST_MIN = 68
    OST_MAX = 112
    OST_TEXT = "В"

    SOUTH_OST_MIN = 113
    SOUTH_OST_MAX = 157
    SOUTH_OST_TEXT = "ЮВ"

    SOUTH_MIN = 158
    SOUTH_MAX = 202
    SOUTH_TEXT = "Ю"

    SOUTH_WEST_MIN = 203
    SOUTH_WEST_MAX = 247
    SOUTH_WEST_TEXT = "ЮЗ"

    WEST_MIN = 248
    WEST_MAX = 292
    WEST_TEXT = "З"

    NORTH_WEST_MIN = 293
    NORTH_WEST_MAX = 337
    NORTH_WEST_TEXT = "СЗ"

    rhumbWind = None
    if wd is not None:
        if WD_MIN <= wd and wd <= WD_MAX:

            if NORTH_MIN <= wd <= WD_MAX or 0 <= wd <= NORTH_MAX:
                rhumbWind = NORTH_TEXT
            elif NORTH_OST_MIN <= wd <= NORTH_OST_MAX:
                rhumbWind = NORTH_OST_TEXT
            elif OST_MIN <= wd <= OST_MAX:
                rhumbWind = OST_TEXT
            elif SOUTH_OST_MIN <= wd <= SOUTH_OST_MAX:
                rhumbWind = SOUTH_OST_TEXT
            elif SOUTH_MIN <= wd <= SOUTH_MAX:
                rhumbWind = SOUTH_TEXT
            elif SOUTH_WEST_MIN <= wd <= SOUTH_WEST_MAX:
                rhumbWind = SOUTH_WEST_TEXT
            elif WEST_MIN <= wd <= WEST_MAX:
                rhumbWind = WEST_TEXT
            elif NORTH_WEST_MIN <= wd <= NORTH_WEST_MAX:
                rhumbWind = NORTH_WEST_TEXT
    return rhumbWind

