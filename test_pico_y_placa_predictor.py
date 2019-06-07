from unittest import TestCase
from analyser import pico_y_placa_predictor
from datetime import datetime
from datetime import time

class TestPicoYPlacaPredictor(TestCase):
    def test_pico_y_placa_predictor_false(self):
        plate = "gnj-780"
        date = "2019-06-04"
        time = "09:00:00"

        self.assertFalse(pico_y_placa_predictor(plate, date, time))

    def test_pico_y_placa_predictor_true(self):
        plate = "gnj-780"
        date = "2019-06-07"
        time = "09:25:00"

        self.assertTrue(pico_y_placa_predictor(plate, date, time))

    def test_pico_y_placa_predictor_true_2(self):
        plate = "gnj-7810"
        date = "2019-06-07"
        time = "09:15:00"

        self.assertTrue(pico_y_placa_predictor(plate, date, time))

    def test_pico_y_placa_predictor_different_format(self):
        plate = "gnj-780"
        date = "07/06/2019"
        time = "09:05"

        self.assertTrue(pico_y_placa_predictor(plate, date, time, format="%d/%m/%Y %H:%M"))

    def test_pico_y_placa_predictor_different_locale(self):
        plate = "gnj-780"
        date = "2019-06-07"
        time = "09:50:00"

        self.assertFalse(pico_y_placa_predictor(plate, date, time, locale="en_US"))

    def test_pico_y_placa_predictor_wrong_license(self):
        plate = "gnj-780789"
        date = "2019-06-07"
        time = "09:05:00"

        self.assertFalse(pico_y_placa_predictor(plate, date, time))

    def test_pico_y_placa_predictor_current_time(self):
        plate = "gnj-780"
        date = "2019-06-07"

        init_time_1 = time(7, 0, 0)
        end_time_1 = time(9, 30, 0)
        init_time_2 = time(16, 0, 0)
        end_time_2 = time(19, 30, 0)

        current_time = datetime.now().time()

        if init_time_1 <= current_time <= end_time_1 or init_time_2 <= current_time <= end_time_2:
            self.assertTrue(pico_y_placa_predictor(plate, date))
        else:
            self.assertFalse(pico_y_placa_predictor(plate, date))
