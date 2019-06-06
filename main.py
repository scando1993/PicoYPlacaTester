from datetime import datetime
from datetime import timedelta
import locale
import calendar

locale.setlocale(locale.LC_ALL, 'es_EC')


def pico_y_placa_predictor(plate_number, date, time=None, **kargs):
    # time_frame_1 = ['07:00', '09:30']
    # time_frame_2 = ['16:00', '19:30']
    time_frame = timedelta(hours=2, minutes=30)
    time_frame_2 = timedelta(hours=3, minutes=30)
    week_days = [x for x in calendar.day_name]
    plate_day = ""

    if len(plate_number) > 9:
        return False

    if plate_number[-1].isdigit():
        last_digit = plate_number[-1]
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

    current_day = time.strftime("%A")
    if current_day != plate_day:
        return False

    if type(date) is not str and type(time) is not str:
        return False
    else:
        if time is None:
            time = datetime.now().time()
        else:
            try:
                time = datetime.strptime(" ".join([date, time]), "%Y-%m-%d %H:%M:%S")
                from_time_1 = datetime.strptime(" ".join([date, "07:00:00"]), "%Y-%m-%d %H:%M:%S")
                to_time_1 = datetime.strptime(" ".join([date, "09:30:00"]), "%Y-%m-%d %H:%M:%S")
                from_time_2 = datetime.strptime(" ".join([date, "16:00:00"]), "%Y-%m-%d %H:%M:%S")
                to_time_2 = datetime.strptime(" ".join([date, "19:30:00"]), "%Y-%m-%d %H:%M:%S")
            except Exception:
                return False

            if from_time_1 > time > to_time_1 or from_time_2 > time > to_time_2:
                return False


    return True


if __name__ == '__main__':
    pass