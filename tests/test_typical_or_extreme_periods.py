import os
import tempfile
import unittest
from pyepw.epw import TypicalOrExtremePeriods, TypicalOrExtremePeriod, EPW


class TestTypicalOrExtremePeriods(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_typical_or_extreme_periods(self):

        obj = TypicalOrExtremePeriods()
        typical_or_extreme_period_obj = TypicalOrExtremePeriod()
        var_typical_or_extreme_period_typical_or_extreme_period_name = "typical_or_extreme_period_name"
        typical_or_extreme_period_obj.typical_or_extreme_period_name = var_typical_or_extreme_period_typical_or_extreme_period_name
        var_typical_or_extreme_period_typical_or_extreme_period_type = "typical_or_extreme_period_type"
        typical_or_extreme_period_obj.typical_or_extreme_period_type = var_typical_or_extreme_period_typical_or_extreme_period_type
        var_typical_or_extreme_period_period_start_day = "period_start_day"
        typical_or_extreme_period_obj.period_start_day = var_typical_or_extreme_period_period_start_day
        var_typical_or_extreme_period_period_end_day = "period_end_day"
        typical_or_extreme_period_obj.period_end_day = var_typical_or_extreme_period_period_end_day
        obj.add_typical_or_extreme_period(typical_or_extreme_period_obj)

        epw = EPW(typical_or_extreme_periods=obj)
        epw.save(self.path)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertEqual(
            epw2.typical_or_extreme_periods.typical_or_extreme_periods[0].typical_or_extreme_period_name,
            var_typical_or_extreme_period_typical_or_extreme_period_name)
        self.assertEqual(
            epw2.typical_or_extreme_periods.typical_or_extreme_periods[0].typical_or_extreme_period_type,
            var_typical_or_extreme_period_typical_or_extreme_period_type)
        self.assertEqual(
            epw2.typical_or_extreme_periods.typical_or_extreme_periods[0].period_start_day,
            var_typical_or_extreme_period_period_start_day)
        self.assertEqual(
            epw2.typical_or_extreme_periods.typical_or_extreme_periods[0].period_end_day,
            var_typical_or_extreme_period_period_end_day)
