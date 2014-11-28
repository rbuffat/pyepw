import os
import tempfile
import unittest
from pyepw.epw import DataPeriods, DataPeriod, EPW


class TestDataPeriods(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_data_periods(self):

        obj = DataPeriods()
        data_period_obj = DataPeriod()
        var_data_period_number_of_records_per_hour = 1
        data_period_obj.number_of_records_per_hour = var_data_period_number_of_records_per_hour
        var_data_period_data_period_name_or_description = "data_period_name_or_description"
        data_period_obj.data_period_name_or_description = var_data_period_data_period_name_or_description
        var_data_period_data_period_start_day_of_week = "Sunday"
        data_period_obj.data_period_start_day_of_week = var_data_period_data_period_start_day_of_week
        var_data_period_data_period_start_day = "data_period_start_day"
        data_period_obj.data_period_start_day = var_data_period_data_period_start_day
        var_data_period_data_period_end_day = "data_period_end_day"
        data_period_obj.data_period_end_day = var_data_period_data_period_end_day
        obj.add_data_period(data_period_obj)

        epw = EPW(data_periods=obj)
        epw.save(self.path)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertEqual(
            epw2.data_periods.data_periods[0].number_of_records_per_hour,
            var_data_period_number_of_records_per_hour)
        self.assertEqual(
            epw2.data_periods.data_periods[0].data_period_name_or_description,
            var_data_period_data_period_name_or_description)
        self.assertEqual(
            epw2.data_periods.data_periods[0].data_period_start_day_of_week,
            var_data_period_data_period_start_day_of_week)
        self.assertEqual(
            epw2.data_periods.data_periods[0].data_period_start_day,
            var_data_period_data_period_start_day)
        self.assertEqual(
            epw2.data_periods.data_periods[0].data_period_end_day,
            var_data_period_data_period_end_day)
