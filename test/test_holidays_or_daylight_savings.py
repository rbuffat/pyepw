import os
import tempfile
import unittest
from pyepw.epw import HolidaysOrDaylightSavings, Holiday, EPW


class TestHolidaysOrDaylightSavings(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_holidays_or_daylight_savings(self):

        obj = HolidaysOrDaylightSavings()
        var_leapyear_observed = "Yes"
        obj.leapyear_observed = var_leapyear_observed
        var_daylight_saving_start_day = "daylight_saving_start_day"
        obj.daylight_saving_start_day = var_daylight_saving_start_day
        var_daylight_saving_end_day = "daylight_saving_end_day"
        obj.daylight_saving_end_day = var_daylight_saving_end_day
        holiday_obj = Holiday()
        var_holiday_holiday_name = "holiday_name"
        holiday_obj.holiday_name = var_holiday_holiday_name
        var_holiday_holiday_day = "holiday_day"
        holiday_obj.holiday_day = var_holiday_holiday_day
        obj.add_holiday(holiday_obj)

        epw = EPW(holidays_or_daylight_savings=obj)
        epw.save(self.path, check=False)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertEqual(
            epw2.holidays_or_daylight_savings.leapyear_observed,
            var_leapyear_observed)
        self.assertEqual(
            epw2.holidays_or_daylight_savings.daylight_saving_start_day,
            var_daylight_saving_start_day)
        self.assertEqual(
            epw2.holidays_or_daylight_savings.daylight_saving_end_day,
            var_daylight_saving_end_day)
        self.assertEqual(
            epw2.holidays_or_daylight_savings.holidays[0].holiday_name,
            var_holiday_holiday_name)
        self.assertEqual(
            epw2.holidays_or_daylight_savings.holidays[0].holiday_day,
            var_holiday_holiday_day)
