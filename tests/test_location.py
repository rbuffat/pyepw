import os
import tempfile
import unittest
from pyepw.epw import Location, EPW


class TestLocation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_location(self):

        obj = Location()
        var_city = "city"
        obj.city = var_city
        var_state_province_region = "state_province_region"
        obj.state_province_region = var_state_province_region
        var_country = "country"
        obj.country = var_country
        var_source = "source"
        obj.source = var_source
        var_wmo = "wmo"
        obj.wmo = var_wmo
        var_latitude = (90.0 + -90.0) * 0.5
        obj.latitude = var_latitude
        var_longitude = (180.0 + -180.0) * 0.5
        obj.longitude = var_longitude
        var_timezone = (12.0 + -12.0) * 0.5
        obj.timezone = var_timezone
        var_elevation = ((9999.9 - 1.0) + -1000.0) * 0.5
        obj.elevation = var_elevation

        epw = EPW(location=obj)
        epw.save(self.path)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertEqual(epw2.location.city, var_city)
        self.assertEqual(
            epw2.location.state_province_region,
            var_state_province_region)
        self.assertEqual(epw2.location.country, var_country)
        self.assertEqual(epw2.location.source, var_source)
        self.assertEqual(epw2.location.wmo, var_wmo)
        self.assertAlmostEqual(epw2.location.latitude, var_latitude)
        self.assertAlmostEqual(epw2.location.longitude, var_longitude)
        self.assertAlmostEqual(epw2.location.timezone, var_timezone)
        self.assertAlmostEqual(epw2.location.elevation, var_elevation)
