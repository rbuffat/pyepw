import os
import tempfile
import unittest
from pyepw.epw import GroundTemperatures, GroundTemperature, EPW


class TestGroundTemperatures(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_ground_temperatures(self):

        obj = GroundTemperatures()
        ground_temperature_obj = GroundTemperature()
        var_ground_temperature_ground_temperature_depth = 1.1
        ground_temperature_obj.ground_temperature_depth = var_ground_temperature_ground_temperature_depth
        var_ground_temperature_depth_soil_conductivity = 2.2
        ground_temperature_obj.depth_soil_conductivity = var_ground_temperature_depth_soil_conductivity
        var_ground_temperature_depth_soil_density = 3.3
        ground_temperature_obj.depth_soil_density = var_ground_temperature_depth_soil_density
        var_ground_temperature_depth_soil_specific_heat = 4.4
        ground_temperature_obj.depth_soil_specific_heat = var_ground_temperature_depth_soil_specific_heat
        var_ground_temperature_depth_january_average_ground_temperature = 5.5
        ground_temperature_obj.depth_january_average_ground_temperature = var_ground_temperature_depth_january_average_ground_temperature
        var_ground_temperature_depth_february_average_ground_temperature = 6.6
        ground_temperature_obj.depth_february_average_ground_temperature = var_ground_temperature_depth_february_average_ground_temperature
        var_ground_temperature_depth_march_average_ground_temperature = 7.7
        ground_temperature_obj.depth_march_average_ground_temperature = var_ground_temperature_depth_march_average_ground_temperature
        var_ground_temperature_depth_april_average_ground_temperature = 8.8
        ground_temperature_obj.depth_april_average_ground_temperature = var_ground_temperature_depth_april_average_ground_temperature
        var_ground_temperature_depth_may_average_ground_temperature = 9.9
        ground_temperature_obj.depth_may_average_ground_temperature = var_ground_temperature_depth_may_average_ground_temperature
        var_ground_temperature_depth_june_average_ground_temperature = 10.10
        ground_temperature_obj.depth_june_average_ground_temperature = var_ground_temperature_depth_june_average_ground_temperature
        var_ground_temperature_depth_july_average_ground_temperature = 11.11
        ground_temperature_obj.depth_july_average_ground_temperature = var_ground_temperature_depth_july_average_ground_temperature
        var_ground_temperature_depth_august_average_ground_temperature = 12.12
        ground_temperature_obj.depth_august_average_ground_temperature = var_ground_temperature_depth_august_average_ground_temperature
        var_ground_temperature_depth_september_average_ground_temperature = 13.13
        ground_temperature_obj.depth_september_average_ground_temperature = var_ground_temperature_depth_september_average_ground_temperature
        var_ground_temperature_depth_october_average_ground_temperature = 14.14
        ground_temperature_obj.depth_october_average_ground_temperature = var_ground_temperature_depth_october_average_ground_temperature
        var_ground_temperature_depth_november_average_ground_temperature = 15.15
        ground_temperature_obj.depth_november_average_ground_temperature = var_ground_temperature_depth_november_average_ground_temperature
        var_ground_temperature_depth_december_average_ground_temperature = 16.16
        ground_temperature_obj.depth_december_average_ground_temperature = var_ground_temperature_depth_december_average_ground_temperature
        obj.add_ground_temperature(ground_temperature_obj)

        epw = EPW(ground_temperatures=obj)
        epw.save(self.path)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].ground_temperature_depth,
            var_ground_temperature_ground_temperature_depth)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_soil_conductivity,
            var_ground_temperature_depth_soil_conductivity)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_soil_density,
            var_ground_temperature_depth_soil_density)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_soil_specific_heat,
            var_ground_temperature_depth_soil_specific_heat)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_january_average_ground_temperature,
            var_ground_temperature_depth_january_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_february_average_ground_temperature,
            var_ground_temperature_depth_february_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_march_average_ground_temperature,
            var_ground_temperature_depth_march_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_april_average_ground_temperature,
            var_ground_temperature_depth_april_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_may_average_ground_temperature,
            var_ground_temperature_depth_may_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_june_average_ground_temperature,
            var_ground_temperature_depth_june_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_july_average_ground_temperature,
            var_ground_temperature_depth_july_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_august_average_ground_temperature,
            var_ground_temperature_depth_august_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_september_average_ground_temperature,
            var_ground_temperature_depth_september_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_october_average_ground_temperature,
            var_ground_temperature_depth_october_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_november_average_ground_temperature,
            var_ground_temperature_depth_november_average_ground_temperature)
        self.assertAlmostEqual(
            epw2.ground_temperatures.ground_temperatures[0].depth_december_average_ground_temperature,
            var_ground_temperature_depth_december_average_ground_temperature)
