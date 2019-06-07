from datetime import datetime
import locale
import calendar


# True is pico y placa applies False if it doesn't
def pico_y_placa_predictor(plate_number, date, time=None, **kargs):
    if 'locale' in kargs:
        try:
            locale.setlocale(locale.LC_ALL, kargs['locale'])
        except Exception:
            return False
    else:
        locale.setlocale(locale.LC_ALL, 'es_EC')

    week_days = [x for x in calendar.day_name]

    plate_day = ""
    format_original = "%Y-%m-%d %H:%M:%S"

    if 'format' in kargs:
        format_ = kargs['format']
        format_original = format_[:8] + ' ' + format_original[-8:]
    else:
        format_ = format_original

    if len(plate_number) > 9:
        return False

    if plate_number[-1].isdigit():
        last_digit = int(plate_number[-1])
        if 1 <= last_digit <= 2:
            plate_day = week_days[0]
        elif 3 <= last_digit <= 4:
            plate_day = week_days[1]
        elif 5 <= last_digit <= 6:
            plate_day = week_days[2]
        elif 7 <= last_digit <= 8:
            plate_day = week_days[3]
        elif last_digit == 9 or last_digit == 0:
            plate_day = week_days[4]
    else:
        return False

    if type(date) is not str and type(time) is not str:
        return False
    else:
        if time is None:
            time = datetime.now().time().strftime("%H:%M:%S")
            time = datetime.strptime(" ".join([date, time]), format_)
        else:
            try:
                time = datetime.strptime(" ".join([date, time]), format_)
            except Exception:
                return False

        try:
            from_time_1 = datetime.strptime(" ".join([date, "07:00:00"]), format_original)
            to_time_1 = datetime.strptime(" ".join([date, "09:30:00"]), format_original)
            from_time_2 = datetime.strptime(" ".join([date, "16:00:00"]), format_original)
            to_time_2 = datetime.strptime(" ".join([date, "19:30:00"]), format_original)
        except Exception:
            return False

        if plate_day != time.strftime("%A"):
            return False
        if to_time_1 < time < from_time_2:
            return False
        if from_time_1 > time or time > to_time_2:
            return False

    return True
