import os
import tempfile
import unittest
from pyepw.epw import DesignConditions, DesignCondition, EPW


class TestDesignConditions(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_design_conditions(self):

        obj = DesignConditions()
        design_condition_obj = DesignCondition()
        var_design_condition_title_of_design_condition = "title_of_design_condition"
        design_condition_obj.title_of_design_condition = var_design_condition_title_of_design_condition
        var_design_condition_unkown_field = "unkown_field"
        design_condition_obj.unkown_field = var_design_condition_unkown_field
        var_design_condition_design_stat_heating = "Heating"
        design_condition_obj.design_stat_heating = var_design_condition_design_stat_heating
        var_design_condition_coldestmonth = int((12 + 1) * 0.5)
        design_condition_obj.coldestmonth = var_design_condition_coldestmonth
        var_design_condition_db996 = 5.5
        design_condition_obj.db996 = var_design_condition_db996
        var_design_condition_db990 = 6.6
        design_condition_obj.db990 = var_design_condition_db990
        var_design_condition_dp996 = 7.7
        design_condition_obj.dp996 = var_design_condition_dp996
        var_design_condition_hr_dp996 = 8.8
        design_condition_obj.hr_dp996 = var_design_condition_hr_dp996
        var_design_condition_db_dp996 = 9.9
        design_condition_obj.db_dp996 = var_design_condition_db_dp996
        var_design_condition_dp990 = 10.10
        design_condition_obj.dp990 = var_design_condition_dp990
        var_design_condition_hr_dp990 = 11.11
        design_condition_obj.hr_dp990 = var_design_condition_hr_dp990
        var_design_condition_db_dp990 = 12.12
        design_condition_obj.db_dp990 = var_design_condition_db_dp990
        var_design_condition_ws004c = 13.13
        design_condition_obj.ws004c = var_design_condition_ws004c
        var_design_condition_db_ws004c = 14.14
        design_condition_obj.db_ws004c = var_design_condition_db_ws004c
        var_design_condition_ws010c = 15.15
        design_condition_obj.ws010c = var_design_condition_ws010c
        var_design_condition_db_ws010c = 16.16
        design_condition_obj.db_ws010c = var_design_condition_db_ws010c
        var_design_condition_ws_db996 = 17.17
        design_condition_obj.ws_db996 = var_design_condition_ws_db996
        var_design_condition_wd_db996 = 18.18
        design_condition_obj.wd_db996 = var_design_condition_wd_db996
        var_design_condition_design_stat_cooling = "Cooling"
        design_condition_obj.design_stat_cooling = var_design_condition_design_stat_cooling
        var_design_condition_hottestmonth = int((12 + 1) * 0.5)
        design_condition_obj.hottestmonth = var_design_condition_hottestmonth
        var_design_condition_dbr = 21.21
        design_condition_obj.dbr = var_design_condition_dbr
        var_design_condition_db004 = 22.22
        design_condition_obj.db004 = var_design_condition_db004
        var_design_condition_wb_db004 = 23.23
        design_condition_obj.wb_db004 = var_design_condition_wb_db004
        var_design_condition_db010 = 24.24
        design_condition_obj.db010 = var_design_condition_db010
        var_design_condition_wb_db010 = 25.25
        design_condition_obj.wb_db010 = var_design_condition_wb_db010
        var_design_condition_db020 = 26.26
        design_condition_obj.db020 = var_design_condition_db020
        var_design_condition_wb_db020 = 27.27
        design_condition_obj.wb_db020 = var_design_condition_wb_db020
        var_design_condition_wb004 = 28.28
        design_condition_obj.wb004 = var_design_condition_wb004
        var_design_condition_db_wb004 = 29.29
        design_condition_obj.db_wb004 = var_design_condition_db_wb004
        var_design_condition_wb010 = 30.30
        design_condition_obj.wb010 = var_design_condition_wb010
        var_design_condition_db_wb010 = 31.31
        design_condition_obj.db_wb010 = var_design_condition_db_wb010
        var_design_condition_wb020 = 32.32
        design_condition_obj.wb020 = var_design_condition_wb020
        var_design_condition_db_wb020 = 33.33
        design_condition_obj.db_wb020 = var_design_condition_db_wb020
        var_design_condition_ws_db004 = 34.34
        design_condition_obj.ws_db004 = var_design_condition_ws_db004
        var_design_condition_wd_db004 = 35.35
        design_condition_obj.wd_db004 = var_design_condition_wd_db004
        var_design_condition_dp004 = 36.36
        design_condition_obj.dp004 = var_design_condition_dp004
        var_design_condition_hr_dp004 = 37.37
        design_condition_obj.hr_dp004 = var_design_condition_hr_dp004
        var_design_condition_db_dp004 = 38.38
        design_condition_obj.db_dp004 = var_design_condition_db_dp004
        var_design_condition_dp010 = 39.39
        design_condition_obj.dp010 = var_design_condition_dp010
        var_design_condition_hr_dp010 = 40.40
        design_condition_obj.hr_dp010 = var_design_condition_hr_dp010
        var_design_condition_db_dp010 = 41.41
        design_condition_obj.db_dp010 = var_design_condition_db_dp010
        var_design_condition_dp020 = 42.42
        design_condition_obj.dp020 = var_design_condition_dp020
        var_design_condition_hr_dp020 = 43.43
        design_condition_obj.hr_dp020 = var_design_condition_hr_dp020
        var_design_condition_db_dp020 = 44.44
        design_condition_obj.db_dp020 = var_design_condition_db_dp020
        var_design_condition_en004 = 45.45
        design_condition_obj.en004 = var_design_condition_en004
        var_design_condition_db_en004 = 46.46
        design_condition_obj.db_en004 = var_design_condition_db_en004
        var_design_condition_en010 = 47.47
        design_condition_obj.en010 = var_design_condition_en010
        var_design_condition_db_en010 = 48.48
        design_condition_obj.db_en010 = var_design_condition_db_en010
        var_design_condition_en020 = 49.49
        design_condition_obj.en020 = var_design_condition_en020
        var_design_condition_db_en020 = 50.50
        design_condition_obj.db_en020 = var_design_condition_db_en020
        var_design_condition_hrs_84_and_db12_8_or_20_6 = 51.51
        design_condition_obj.hrs_84_and_db12_8_or_20_6 = var_design_condition_hrs_84_and_db12_8_or_20_6
        var_design_condition_design_stat_extremes = "Extremes"
        design_condition_obj.design_stat_extremes = var_design_condition_design_stat_extremes
        var_design_condition_ws010 = 53.53
        design_condition_obj.ws010 = var_design_condition_ws010
        var_design_condition_ws025 = 54.54
        design_condition_obj.ws025 = var_design_condition_ws025
        var_design_condition_ws050 = 55.55
        design_condition_obj.ws050 = var_design_condition_ws050
        var_design_condition_wbmax = 56.56
        design_condition_obj.wbmax = var_design_condition_wbmax
        var_design_condition_dbmin_mean = 57.57
        design_condition_obj.dbmin_mean = var_design_condition_dbmin_mean
        var_design_condition_dbmax_mean = 58.58
        design_condition_obj.dbmax_mean = var_design_condition_dbmax_mean
        var_design_condition_dbmin_stddev = 59.59
        design_condition_obj.dbmin_stddev = var_design_condition_dbmin_stddev
        var_design_condition_dbmax_stddev = 60.60
        design_condition_obj.dbmax_stddev = var_design_condition_dbmax_stddev
        var_design_condition_dbmin05years = 61.61
        design_condition_obj.dbmin05years = var_design_condition_dbmin05years
        var_design_condition_dbmax05years = 62.62
        design_condition_obj.dbmax05years = var_design_condition_dbmax05years
        var_design_condition_dbmin10years = 63.63
        design_condition_obj.dbmin10years = var_design_condition_dbmin10years
        var_design_condition_dbmax10years = 64.64
        design_condition_obj.dbmax10years = var_design_condition_dbmax10years
        var_design_condition_dbmin20years = 65.65
        design_condition_obj.dbmin20years = var_design_condition_dbmin20years
        var_design_condition_dbmax20years = 66.66
        design_condition_obj.dbmax20years = var_design_condition_dbmax20years
        var_design_condition_dbmin50years = 67.67
        design_condition_obj.dbmin50years = var_design_condition_dbmin50years
        var_design_condition_dbmax50years = 68.68
        design_condition_obj.dbmax50years = var_design_condition_dbmax50years
        obj.add_design_condition(design_condition_obj)

        epw = EPW(design_conditions=obj)
        epw.save(self.path)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertEqual(
            epw2.design_conditions.design_conditions[0].title_of_design_condition,
            var_design_condition_title_of_design_condition)
        self.assertEqual(
            epw2.design_conditions.design_conditions[0].unkown_field,
            var_design_condition_unkown_field)
        self.assertEqual(
            epw2.design_conditions.design_conditions[0].design_stat_heating,
            var_design_condition_design_stat_heating)
        self.assertEqual(
            epw2.design_conditions.design_conditions[0].coldestmonth,
            var_design_condition_coldestmonth)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db996,
            var_design_condition_db996)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db990,
            var_design_condition_db990)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dp996,
            var_design_condition_dp996)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].hr_dp996,
            var_design_condition_hr_dp996)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_dp996,
            var_design_condition_db_dp996)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dp990,
            var_design_condition_dp990)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].hr_dp990,
            var_design_condition_hr_dp990)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_dp990,
            var_design_condition_db_dp990)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].ws004c,
            var_design_condition_ws004c)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_ws004c,
            var_design_condition_db_ws004c)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].ws010c,
            var_design_condition_ws010c)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_ws010c,
            var_design_condition_db_ws010c)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].ws_db996,
            var_design_condition_ws_db996)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wd_db996,
            var_design_condition_wd_db996)
        self.assertEqual(
            epw2.design_conditions.design_conditions[0].design_stat_cooling,
            var_design_condition_design_stat_cooling)
        self.assertEqual(
            epw2.design_conditions.design_conditions[0].hottestmonth,
            var_design_condition_hottestmonth)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbr,
            var_design_condition_dbr)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db004,
            var_design_condition_db004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wb_db004,
            var_design_condition_wb_db004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db010,
            var_design_condition_db010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wb_db010,
            var_design_condition_wb_db010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db020,
            var_design_condition_db020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wb_db020,
            var_design_condition_wb_db020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wb004,
            var_design_condition_wb004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_wb004,
            var_design_condition_db_wb004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wb010,
            var_design_condition_wb010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_wb010,
            var_design_condition_db_wb010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wb020,
            var_design_condition_wb020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_wb020,
            var_design_condition_db_wb020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].ws_db004,
            var_design_condition_ws_db004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wd_db004,
            var_design_condition_wd_db004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dp004,
            var_design_condition_dp004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].hr_dp004,
            var_design_condition_hr_dp004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_dp004,
            var_design_condition_db_dp004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dp010,
            var_design_condition_dp010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].hr_dp010,
            var_design_condition_hr_dp010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_dp010,
            var_design_condition_db_dp010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dp020,
            var_design_condition_dp020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].hr_dp020,
            var_design_condition_hr_dp020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_dp020,
            var_design_condition_db_dp020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].en004,
            var_design_condition_en004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_en004,
            var_design_condition_db_en004)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].en010,
            var_design_condition_en010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_en010,
            var_design_condition_db_en010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].en020,
            var_design_condition_en020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].db_en020,
            var_design_condition_db_en020)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].hrs_84_and_db12_8_or_20_6,
            var_design_condition_hrs_84_and_db12_8_or_20_6)
        self.assertEqual(
            epw2.design_conditions.design_conditions[0].design_stat_extremes,
            var_design_condition_design_stat_extremes)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].ws010,
            var_design_condition_ws010)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].ws025,
            var_design_condition_ws025)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].ws050,
            var_design_condition_ws050)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].wbmax,
            var_design_condition_wbmax)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmin_mean,
            var_design_condition_dbmin_mean)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmax_mean,
            var_design_condition_dbmax_mean)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmin_stddev,
            var_design_condition_dbmin_stddev)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmax_stddev,
            var_design_condition_dbmax_stddev)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmin05years,
            var_design_condition_dbmin05years)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmax05years,
            var_design_condition_dbmax05years)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmin10years,
            var_design_condition_dbmin10years)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmax10years,
            var_design_condition_dbmax10years)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmin20years,
            var_design_condition_dbmin20years)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmax20years,
            var_design_condition_dbmax20years)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmin50years,
            var_design_condition_dbmin50years)
        self.assertAlmostEqual(
            epw2.design_conditions.design_conditions[0].dbmax50years,
            var_design_condition_dbmax50years)
