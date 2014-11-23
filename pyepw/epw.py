"""
WARNING: This is an automatically generated file.
It is based on the EPW IDD specification given in the document
Auxiliary EnergyPlus Programs - Extra programs for EnergyPlus, Date: November 22 2013

Do not expect that it actually works!

Generation date: 2014-11-23

"""
from collections import OrderedDict
import re


class Location(object):

    """Corresponds to EPW IDD object `LOCATION`"""
    _internal_name = "LOCATION"
    _field_count = 9

    def __init__(self):
        self._city = None
        self._state_province_region = None
        self._country = None
        self._source = None
        self._wmo = None
        self._latitude = None
        self._longitude = None
        self._timezone = None
        self._elevation = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.city = None
        else:
            self.city = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.state_province_region = None
        else:
            self.state_province_region = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.country = None
        else:
            self.country = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.source = None
        else:
            self.source = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.wmo = None
        else:
            self.wmo = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.latitude = None
        else:
            self.latitude = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.longitude = None
        else:
            self.longitude = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.timezone = None
        else:
            self.timezone = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.elevation = None
        else:
            self.elevation = str(vals[i])
        i += 1

    @property
    def city(self):
        """Get city."""
        return self._city

    @city.setter
    def city(self, value=None):
        """Corresponds to IDD Field `city`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field city'.format(value))

        self._city = value

    @property
    def state_province_region(self):
        """Get state_province_region."""
        return self._state_province_region

    @state_province_region.setter
    def state_province_region(self, value=None):
        """Corresponds to IDD Field `state_province_region`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field state_province_region'.format(value))

        self._state_province_region = value

    @property
    def country(self):
        """Get country."""
        return self._country

    @country.setter
    def country(self, value=None):
        """Corresponds to IDD Field `country`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field country'.format(value))

        self._country = value

    @property
    def source(self):
        """Get source."""
        return self._source

    @source.setter
    def source(self, value=None):
        """Corresponds to IDD Field `source`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field source'.format(value))

        self._source = value

    @property
    def wmo(self):
        """Get wmo."""
        return self._wmo

    @wmo.setter
    def wmo(self, value=None):
        """Corresponds to IDD Field `wmo` usually a 6 digit field.

        Used as alpha in EnergyPlus

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field wmo'.format(value))

        self._wmo = value

    @property
    def latitude(self):
        """Get latitude."""
        return self._latitude

    @latitude.setter
    def latitude(self, value=0.0):
        """Corresponds to IDD Field `latitude`

        + is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)
        Unit: deg
        Default value: 0.0
        value >= -90.0
        value <= 90.0

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field latitude'.format(value))
            if value < -90.0:
                raise ValueError(
                    'value need to be greater or equal -90.0 for field latitude')
            if value > 90.0:
                raise ValueError(
                    'value need to be smaller 90.0 for field latitude')

        self._latitude = value

    @property
    def longitude(self):
        """Get longitude."""
        return self._longitude

    @longitude.setter
    def longitude(self, value=0.0):
        """Corresponds to IDD Field `longitude`

        - is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)
        Unit: deg
        Default value: 0.0
        value >= -180.0
        value <= 180.0

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field longitude'.format(value))
            if value < -180.0:
                raise ValueError(
                    'value need to be greater or equal -180.0 for field longitude')
            if value > 180.0:
                raise ValueError(
                    'value need to be smaller 180.0 for field longitude')

        self._longitude = value

    @property
    def timezone(self):
        """Get timezone."""
        return self._timezone

    @timezone.setter
    def timezone(self, value=0.0):
        """Corresponds to IDD Field `timezone` Time relative to GMT.

        Unit: hr - not on standard units list???
        Default value: 0.0
        value >= -12.0
        value <= 12.0

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field timezone'.format(value))
            if value < -12.0:
                raise ValueError(
                    'value need to be greater or equal -12.0 for field timezone')
            if value > 12.0:
                raise ValueError(
                    'value need to be smaller 12.0 for field timezone')

        self._timezone = value

    @property
    def elevation(self):
        """Get elevation."""
        return self._elevation

    @elevation.setter
    def elevation(self, value=0.0):
        """  Corresponds to IDD Field `elevation`
        Unit: m
        Default value: 0.0
        value >= -1000.0
        value < 9999.9
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field elevation'.format(value))
            if value < -1000.0:
                raise ValueError(
                    'value need to be greater or equal -1000.0 for field elevation')
            if value >= 9999.9:
                raise ValueError(
                    'value need to be smaller or equal 9999.9 for field elevation')

        self._elevation = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.city))
        out.append(self._to_str(self.state_province_region))
        out.append(self._to_str(self.country))
        out.append(self._to_str(self.source))
        out.append(self._to_str(self.wmo))
        out.append(self._to_str(self.latitude))
        out.append(self._to_str(self.longitude))
        out.append(self._to_str(self.timezone))
        out.append(self._to_str(self.elevation))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class TypicalOrExtremePeriod(object):

    """Corresponds to EPW IDD object `TYPICAL/EXTREME PERIOD`"""
    _internal_name = "TYPICAL/EXTREME PERIOD"
    _field_count = 4

    def __init__(self):
        self._typical_or_extreme_period_name = None
        self._typical_or_extreme_period__type = None
        self._period_start_day = None
        self._period__end_day = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.typical_or_extreme_period_name = None
        else:
            self.typical_or_extreme_period_name = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.typical_or_extreme_period__type = None
        else:
            self.typical_or_extreme_period__type = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.period_start_day = None
        else:
            self.period_start_day = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.period__end_day = None
        else:
            self.period__end_day = str(vals[i])
        i += 1

    @property
    def typical_or_extreme_period_name(self):
        """Get typical_or_extreme_period_name."""
        return self._typical_or_extreme_period_name

    @typical_or_extreme_period_name.setter
    def typical_or_extreme_period_name(self, value=None):
        """Corresponds to IDD Field `typical_or_extreme_period_name`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field typical_or_extreme_period_name'.format(value))

        self._typical_or_extreme_period_name = value

    @property
    def typical_or_extreme_period__type(self):
        """Get typical_or_extreme_period__type."""
        return self._typical_or_extreme_period__type

    @typical_or_extreme_period__type.setter
    def typical_or_extreme_period__type(self, value=None):
        """Corresponds to IDD Field `typical_or_extreme_period__type`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field typical_or_extreme_period__type'.format(value))

        self._typical_or_extreme_period__type = value

    @property
    def period_start_day(self):
        """Get period_start_day."""
        return self._period_start_day

    @period_start_day.setter
    def period_start_day(self, value=None):
        """Corresponds to IDD Field `period_start_day`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field period_start_day'.format(value))

        self._period_start_day = value

    @property
    def period__end_day(self):
        """Get period__end_day."""
        return self._period__end_day

    @period__end_day.setter
    def period__end_day(self, value=None):
        """Corresponds to IDD Field `period__end_day`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field period__end_day'.format(value))

        self._period__end_day = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.typical_or_extreme_period_name))
        out.append(self._to_str(self.typical_or_extreme_period__type))
        out.append(self._to_str(self.period_start_day))
        out.append(self._to_str(self.period__end_day))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class TypicalOrExtremePeriods(object):

    """Corresponds to EPW IDD object `TYPICAL/EXTREME PERIODS`"""
    _internal_name = "TYPICAL/EXTREME PERIODS"
    _field_count = 1

    def __init__(self):
        self._typical_or_extreme_periods = []

    def read(self, vals):
        i = 0
        count = int(vals[i])
        i += 1
        for _ in range(count):
            obj = TypicalOrExtremePeriod()
            obj.read(vals[i:i + obj._field_count])
            self.add_typical_or_extreme_period(obj)
            i += obj._field_count

    @property
    def typical_or_extreme_periods(self):
        """Get typical_or_extreme_periods."""
        return self._typical_or_extreme_periods

    def add_typical_or_extreme_period(self, value):
        """Add TypicalOrExtremePeriod."""
        self._typical_or_extreme_periods.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(str(len(self.typical_or_extreme_periods)))
        for obj in self.typical_or_extreme_periods:
            out.append(obj.export(top=False))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class GroundTemperature(object):

    """Corresponds to EPW IDD object `GROUND TEMPERATURE`"""
    _internal_name = "GROUND TEMPERATURE"
    _field_count = 16

    def __init__(self):
        self._ground_temperature_depth = None
        self._depth_soil_conductivity = None
        self._depth_soil_density = None
        self._depth_soil_specific_heat = None
        self._depth_january_average_ground_temperature = None
        self._depth_february_average_ground_temperature = None
        self._depth_march_average_ground_temperature = None
        self._depth_april_average_ground_temperature = None
        self._depth_may_average_ground_temperature = None
        self._depth_june_average_ground_temperature = None
        self._depth_july_average_ground_temperature = None
        self._depth_august_average_ground_temperature = None
        self._depth_september_average_ground_temperature = None
        self._depth_october_average_ground_temperature = None
        self._depth_november_average_ground_temperature = None
        self._depth_december_average_ground_temperature = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.ground_temperature_depth = None
        else:
            self.ground_temperature_depth = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_soil_conductivity = None
        else:
            self.depth_soil_conductivity = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_soil_density = None
        else:
            self.depth_soil_density = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_soil_specific_heat = None
        else:
            self.depth_soil_specific_heat = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_january_average_ground_temperature = None
        else:
            self.depth_january_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_february_average_ground_temperature = None
        else:
            self.depth_february_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_march_average_ground_temperature = None
        else:
            self.depth_march_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_april_average_ground_temperature = None
        else:
            self.depth_april_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_may_average_ground_temperature = None
        else:
            self.depth_may_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_june_average_ground_temperature = None
        else:
            self.depth_june_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_july_average_ground_temperature = None
        else:
            self.depth_july_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_august_average_ground_temperature = None
        else:
            self.depth_august_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_september_average_ground_temperature = None
        else:
            self.depth_september_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_october_average_ground_temperature = None
        else:
            self.depth_october_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_november_average_ground_temperature = None
        else:
            self.depth_november_average_ground_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.depth_december_average_ground_temperature = None
        else:
            self.depth_december_average_ground_temperature = str(vals[i])
        i += 1

    @property
    def ground_temperature_depth(self):
        """Get ground_temperature_depth."""
        return self._ground_temperature_depth

    @ground_temperature_depth.setter
    def ground_temperature_depth(self, value=None):
        """  Corresponds to IDD Field `ground_temperature_depth`
        Unit: m
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field ground_temperature_depth'.format(value))

        self._ground_temperature_depth = value

    @property
    def depth_soil_conductivity(self):
        """Get depth_soil_conductivity."""
        return self._depth_soil_conductivity

    @depth_soil_conductivity.setter
    def depth_soil_conductivity(self, value=None):
        """  Corresponds to IDD Field `depth_soil_conductivity`
        Unit: W/m-K,
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_soil_conductivity'.format(value))

        self._depth_soil_conductivity = value

    @property
    def depth_soil_density(self):
        """Get depth_soil_density."""
        return self._depth_soil_density

    @depth_soil_density.setter
    def depth_soil_density(self, value=None):
        """  Corresponds to IDD Field `depth_soil_density`
        Unit: kg/m3
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_soil_density'.format(value))

        self._depth_soil_density = value

    @property
    def depth_soil_specific_heat(self):
        """Get depth_soil_specific_heat."""
        return self._depth_soil_specific_heat

    @depth_soil_specific_heat.setter
    def depth_soil_specific_heat(self, value=None):
        """  Corresponds to IDD Field `depth_soil_specific_heat`
        Unit: J/kg-K,
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_soil_specific_heat'.format(value))

        self._depth_soil_specific_heat = value

    @property
    def depth_january_average_ground_temperature(self):
        """Get depth_january_average_ground_temperature."""
        return self._depth_january_average_ground_temperature

    @depth_january_average_ground_temperature.setter
    def depth_january_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_january_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_january_average_ground_temperature'.format(value))

        self._depth_january_average_ground_temperature = value

    @property
    def depth_february_average_ground_temperature(self):
        """Get depth_february_average_ground_temperature."""
        return self._depth_february_average_ground_temperature

    @depth_february_average_ground_temperature.setter
    def depth_february_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_february_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_february_average_ground_temperature'.format(value))

        self._depth_february_average_ground_temperature = value

    @property
    def depth_march_average_ground_temperature(self):
        """Get depth_march_average_ground_temperature."""
        return self._depth_march_average_ground_temperature

    @depth_march_average_ground_temperature.setter
    def depth_march_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_march_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_march_average_ground_temperature'.format(value))

        self._depth_march_average_ground_temperature = value

    @property
    def depth_april_average_ground_temperature(self):
        """Get depth_april_average_ground_temperature."""
        return self._depth_april_average_ground_temperature

    @depth_april_average_ground_temperature.setter
    def depth_april_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_april_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_april_average_ground_temperature'.format(value))

        self._depth_april_average_ground_temperature = value

    @property
    def depth_may_average_ground_temperature(self):
        """Get depth_may_average_ground_temperature."""
        return self._depth_may_average_ground_temperature

    @depth_may_average_ground_temperature.setter
    def depth_may_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_may_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_may_average_ground_temperature'.format(value))

        self._depth_may_average_ground_temperature = value

    @property
    def depth_june_average_ground_temperature(self):
        """Get depth_june_average_ground_temperature."""
        return self._depth_june_average_ground_temperature

    @depth_june_average_ground_temperature.setter
    def depth_june_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_june_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_june_average_ground_temperature'.format(value))

        self._depth_june_average_ground_temperature = value

    @property
    def depth_july_average_ground_temperature(self):
        """Get depth_july_average_ground_temperature."""
        return self._depth_july_average_ground_temperature

    @depth_july_average_ground_temperature.setter
    def depth_july_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_july_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_july_average_ground_temperature'.format(value))

        self._depth_july_average_ground_temperature = value

    @property
    def depth_august_average_ground_temperature(self):
        """Get depth_august_average_ground_temperature."""
        return self._depth_august_average_ground_temperature

    @depth_august_average_ground_temperature.setter
    def depth_august_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_august_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_august_average_ground_temperature'.format(value))

        self._depth_august_average_ground_temperature = value

    @property
    def depth_september_average_ground_temperature(self):
        """Get depth_september_average_ground_temperature."""
        return self._depth_september_average_ground_temperature

    @depth_september_average_ground_temperature.setter
    def depth_september_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_september_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_september_average_ground_temperature'.format(value))

        self._depth_september_average_ground_temperature = value

    @property
    def depth_october_average_ground_temperature(self):
        """Get depth_october_average_ground_temperature."""
        return self._depth_october_average_ground_temperature

    @depth_october_average_ground_temperature.setter
    def depth_october_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_october_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_october_average_ground_temperature'.format(value))

        self._depth_october_average_ground_temperature = value

    @property
    def depth_november_average_ground_temperature(self):
        """Get depth_november_average_ground_temperature."""
        return self._depth_november_average_ground_temperature

    @depth_november_average_ground_temperature.setter
    def depth_november_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_november_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_november_average_ground_temperature'.format(value))

        self._depth_november_average_ground_temperature = value

    @property
    def depth_december_average_ground_temperature(self):
        """Get depth_december_average_ground_temperature."""
        return self._depth_december_average_ground_temperature

    @depth_december_average_ground_temperature.setter
    def depth_december_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `depth_december_average_ground_temperature`
        Unit: C
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field depth_december_average_ground_temperature'.format(value))

        self._depth_december_average_ground_temperature = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.ground_temperature_depth))
        out.append(self._to_str(self.depth_soil_conductivity))
        out.append(self._to_str(self.depth_soil_density))
        out.append(self._to_str(self.depth_soil_specific_heat))
        out.append(self._to_str(self.depth_january_average_ground_temperature))
        out.append(
            self._to_str(
                self.depth_february_average_ground_temperature))
        out.append(self._to_str(self.depth_march_average_ground_temperature))
        out.append(self._to_str(self.depth_april_average_ground_temperature))
        out.append(self._to_str(self.depth_may_average_ground_temperature))
        out.append(self._to_str(self.depth_june_average_ground_temperature))
        out.append(self._to_str(self.depth_july_average_ground_temperature))
        out.append(self._to_str(self.depth_august_average_ground_temperature))
        out.append(
            self._to_str(
                self.depth_september_average_ground_temperature))
        out.append(self._to_str(self.depth_october_average_ground_temperature))
        out.append(
            self._to_str(
                self.depth_november_average_ground_temperature))
        out.append(
            self._to_str(
                self.depth_december_average_ground_temperature))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class GroundTemperatures(object):

    """Corresponds to EPW IDD object `GROUND TEMPERATURES`"""
    _internal_name = "GROUND TEMPERATURES"
    _field_count = 1

    def __init__(self):
        self._ground_temperatures = []

    def read(self, vals):
        i = 0
        count = int(vals[i])
        i += 1
        for _ in range(count):
            obj = GroundTemperature()
            obj.read(vals[i:i + obj._field_count])
            self.add_ground_temperature(obj)
            i += obj._field_count

    @property
    def ground_temperatures(self):
        """Get ground_temperatures."""
        return self._ground_temperatures

    def add_ground_temperature(self, value):
        """Add TypicalOrExtremePeriod."""
        self._ground_temperatures.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(str(len(self.ground_temperatures)))
        for obj in self.ground_temperatures:
            out.append(obj.export(top=False))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class Holiday(object):

    """Corresponds to EPW IDD object `HOLIDAY`"""
    _internal_name = "HOLIDAY"
    _field_count = 2

    def __init__(self):
        self._holiday_name = None
        self._holiday_day = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.holiday_name = None
        else:
            self.holiday_name = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.holiday_day = None
        else:
            self.holiday_day = str(vals[i])
        i += 1

    @property
    def holiday_name(self):
        """Get holiday_name."""
        return self._holiday_name

    @holiday_name.setter
    def holiday_name(self, value=None):
        """Corresponds to IDD Field `holiday_name`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field holiday_name'.format(value))

        self._holiday_name = value

    @property
    def holiday_day(self):
        """Get holiday_day."""
        return self._holiday_day

    @holiday_day.setter
    def holiday_day(self, value=None):
        """Corresponds to IDD Field `holiday_day`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field holiday_day'.format(value))

        self._holiday_day = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.holiday_name))
        out.append(self._to_str(self.holiday_day))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class HolidaysOrDaylightSavings(object):

    """Corresponds to EPW IDD object `HOLIDAYS/DAYLIGHT SAVINGS`"""
    _internal_name = "HOLIDAYS/DAYLIGHT SAVINGS"
    _field_count = 4

    def __init__(self):
        self._leapyear_observed = None
        self._daylight_saving_start_day = None
        self._daylight_saving_end_day = None
        self._holidays = []

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.leapyear_observed = None
        else:
            self.leapyear_observed = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.daylight_saving_start_day = None
        else:
            self.daylight_saving_start_day = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.daylight_saving_end_day = None
        else:
            self.daylight_saving_end_day = str(vals[i])
        i += 1
        count = int(vals[i])
        i += 1
        for _ in range(count):
            obj = Holiday()
            obj.read(vals[i:i + obj._field_count])
            self.add_holiday(obj)
            i += obj._field_count

    @property
    def leapyear_observed(self):
        """Get leapyear_observed."""
        return self._leapyear_observed

    @leapyear_observed.setter
    def leapyear_observed(self, value=None):
        """Corresponds to IDD Field `leapyear_observed` Yes if Leap Year will
        be observed for this file No if Leap Year days (29 Feb) should be
        ignored in this file.

        Accepted values:
          - Yes
          - No

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field leapyear_observed'.format(value))
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError(
                    'value {} is not an accepted value for field leapyear_observed'.format(value))

        self._leapyear_observed = value

    @property
    def daylight_saving_start_day(self):
        """Get daylight_saving_start_day."""
        return self._daylight_saving_start_day

    @daylight_saving_start_day.setter
    def daylight_saving_start_day(self, value=None):
        """Corresponds to IDD Field `daylight_saving_start_day`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field daylight_saving_start_day'.format(value))

        self._daylight_saving_start_day = value

    @property
    def daylight_saving_end_day(self):
        """Get daylight_saving_end_day."""
        return self._daylight_saving_end_day

    @daylight_saving_end_day.setter
    def daylight_saving_end_day(self, value=None):
        """Corresponds to IDD Field `daylight_saving_end_day`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field daylight_saving_end_day'.format(value))

        self._daylight_saving_end_day = value

    @property
    def holidays(self):
        """Get holidays."""
        return self._holidays

    def add_holiday(self, value):
        """Add TypicalOrExtremePeriod."""
        self._holidays.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.leapyear_observed))
        out.append(self._to_str(self.daylight_saving_start_day))
        out.append(self._to_str(self.daylight_saving_end_day))
        out.append(str(len(self.holidays)))
        for obj in self.holidays:
            out.append(obj.export(top=False))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class Comments1(object):

    """Corresponds to EPW IDD object `COMMENTS 1`"""
    _internal_name = "COMMENTS 1"
    _field_count = 1

    def __init__(self):
        self._comments_1 = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.comments_1 = None
        else:
            self.comments_1 = str(vals[i])
        i += 1

    @property
    def comments_1(self):
        """Get comments_1."""
        return self._comments_1

    @comments_1.setter
    def comments_1(self, value=None):
        """Corresponds to IDD Field `comments_1`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field comments_1'.format(value))

        self._comments_1 = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.comments_1))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class Comments2(object):

    """Corresponds to EPW IDD object `COMMENTS 2`"""
    _internal_name = "COMMENTS 2"
    _field_count = 1

    def __init__(self):
        self._comments_2 = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.comments_2 = None
        else:
            self.comments_2 = str(vals[i])
        i += 1

    @property
    def comments_2(self):
        """Get comments_2."""
        return self._comments_2

    @comments_2.setter
    def comments_2(self, value=None):
        """Corresponds to IDD Field `comments_2`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field comments_2'.format(value))

        self._comments_2 = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.comments_2))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class DataPeriod(object):

    """Corresponds to EPW IDD object `DATA PERIOD`"""
    _internal_name = "DATA PERIOD"
    _field_count = 5

    def __init__(self):
        self._number_of_records_per_hour = None
        self._data_period_name_or_description = None
        self._data_period_start_day_of_week = None
        self._data_period_start_day = None
        self._data_period_end_day = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.number_of_records_per_hour = None
        else:
            self.number_of_records_per_hour = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.data_period_name_or_description = None
        else:
            self.data_period_name_or_description = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.data_period_start_day_of_week = None
        else:
            self.data_period_start_day_of_week = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.data_period_start_day = None
        else:
            self.data_period_start_day = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.data_period_end_day = None
        else:
            self.data_period_end_day = str(vals[i])
        i += 1

    @property
    def number_of_records_per_hour(self):
        """Get number_of_records_per_hour."""
        return self._number_of_records_per_hour

    @number_of_records_per_hour.setter
    def number_of_records_per_hour(self, value=None):
        """Corresponds to IDD Field `number_of_records_per_hour`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field number_of_records_per_hour'.format(value))

        self._number_of_records_per_hour = value

    @property
    def data_period_name_or_description(self):
        """Get data_period_name_or_description."""
        return self._data_period_name_or_description

    @data_period_name_or_description.setter
    def data_period_name_or_description(self, value=None):
        """Corresponds to IDD Field `data_period_name_or_description`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field data_period_name_or_description'.format(value))

        self._data_period_name_or_description = value

    @property
    def data_period_start_day_of_week(self):
        """Get data_period_start_day_of_week."""
        return self._data_period_start_day_of_week

    @data_period_start_day_of_week.setter
    def data_period_start_day_of_week(self, value=None):
        """Corresponds to IDD Field `data_period_start_day_of_week`

        Accepted values:
          - Sunday
          - Monday
          - Tuesday
          - Wednesday
          - Thursday
          - Friday
          - Saturday

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field data_period_start_day_of_week'.format(value))
            vals = set()
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            if value not in vals:
                raise ValueError(
                    'value {} is not an accepted value for field data_period_start_day_of_week'.format(value))

        self._data_period_start_day_of_week = value

    @property
    def data_period_start_day(self):
        """Get data_period_start_day."""
        return self._data_period_start_day

    @data_period_start_day.setter
    def data_period_start_day(self, value=None):
        """Corresponds to IDD Field `data_period_start_day`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field data_period_start_day'.format(value))

        self._data_period_start_day = value

    @property
    def data_period_end_day(self):
        """Get data_period_end_day."""
        return self._data_period_end_day

    @data_period_end_day.setter
    def data_period_end_day(self, value=None):
        """Corresponds to IDD Field `data_period_end_day`"""
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field data_period_end_day'.format(value))

        self._data_period_end_day = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.number_of_records_per_hour))
        out.append(self._to_str(self.data_period_name_or_description))
        out.append(self._to_str(self.data_period_start_day_of_week))
        out.append(self._to_str(self.data_period_start_day))
        out.append(self._to_str(self.data_period_end_day))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class DataPeriods(object):

    """Corresponds to EPW IDD object `DATA PERIODS`"""
    _internal_name = "DATA PERIODS"
    _field_count = 1

    def __init__(self):
        self._data_periods = []

    def read(self, vals):
        i = 0
        count = int(vals[i])
        i += 1
        for _ in range(count):
            obj = DataPeriod()
            obj.read(vals[i:i + obj._field_count])
            self.add_data_period(obj)
            i += obj._field_count

    @property
    def data_periods(self):
        """Get data_periods."""
        return self._data_periods

    def add_data_period(self, value):
        """Add TypicalOrExtremePeriod."""
        self._data_periods.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(str(len(self.data_periods)))
        for obj in self.data_periods:
            out.append(obj.export(top=False))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class WeatherData(object):

    """Corresponds to EPW IDD object `WEATHER DATA`"""
    _internal_name = "WEATHER DATA"
    _field_count = 35

    def __init__(self):
        self._year = None
        self._month = None
        self._day = None
        self._hour = None
        self._minute = None
        self._data_source_and_uncertainty_flags = None
        self._dry_bulb_temperature = None
        self._dew_point_temperature = None
        self._relative_humidity = None
        self._atmospheric_station_pressure = None
        self._extraterrestrial_horizontal_radiation = None
        self._extraterrestrial_direct_normal_radiation = None
        self._horizontal_infrared_radiation_intensity = None
        self._global_horizontal_radiation = None
        self._direct_normal_radiation = None
        self._diffuse_horizontal_radiation = None
        self._global_horizontal_illuminance = None
        self._direct_normal_illuminance = None
        self._diffuse_horizontal_illuminance = None
        self._zenith_luminance = None
        self._wind_direction = None
        self._wind_speed = None
        self._total_sky_cover = None
        self._opaque_sky_cover_used_if_horizontal_ir_intensity_missing = None
        self._visibility = None
        self._ceiling_height = None
        self._present_weather_observation = None
        self._present_weather_codes = None
        self._precipitable_water = None
        self._aerosol_optical_depth = None
        self._snow_depth = None
        self._days_since_last_snowfall = None
        self._albedo = None
        self._liquid_precipitation_depth = None
        self._liquid_precipitation_quantity = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.year = None
        else:
            self.year = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.month = None
        else:
            self.month = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.day = None
        else:
            self.day = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.hour = None
        else:
            self.hour = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.minute = None
        else:
            self.minute = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.data_source_and_uncertainty_flags = None
        else:
            self.data_source_and_uncertainty_flags = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.dry_bulb_temperature = None
        else:
            self.dry_bulb_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.dew_point_temperature = None
        else:
            self.dew_point_temperature = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity = None
        else:
            self.relative_humidity = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.atmospheric_station_pressure = None
        else:
            self.atmospheric_station_pressure = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.extraterrestrial_horizontal_radiation = None
        else:
            self.extraterrestrial_horizontal_radiation = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.extraterrestrial_direct_normal_radiation = None
        else:
            self.extraterrestrial_direct_normal_radiation = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.horizontal_infrared_radiation_intensity = None
        else:
            self.horizontal_infrared_radiation_intensity = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.global_horizontal_radiation = None
        else:
            self.global_horizontal_radiation = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.direct_normal_radiation = None
        else:
            self.direct_normal_radiation = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_horizontal_radiation = None
        else:
            self.diffuse_horizontal_radiation = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.global_horizontal_illuminance = None
        else:
            self.global_horizontal_illuminance = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.direct_normal_illuminance = None
        else:
            self.direct_normal_illuminance = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_horizontal_illuminance = None
        else:
            self.diffuse_horizontal_illuminance = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.zenith_luminance = None
        else:
            self.zenith_luminance = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction = None
        else:
            self.wind_direction = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed = None
        else:
            self.wind_speed = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.total_sky_cover = None
        else:
            self.total_sky_cover = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.opaque_sky_cover_used_if_horizontal_ir_intensity_missing = None
        else:
            self.opaque_sky_cover_used_if_horizontal_ir_intensity_missing = str(
                vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.visibility = None
        else:
            self.visibility = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.ceiling_height = None
        else:
            self.ceiling_height = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.present_weather_observation = None
        else:
            self.present_weather_observation = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.present_weather_codes = None
        else:
            self.present_weather_codes = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.precipitable_water = None
        else:
            self.precipitable_water = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.aerosol_optical_depth = None
        else:
            self.aerosol_optical_depth = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.snow_depth = None
        else:
            self.snow_depth = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.days_since_last_snowfall = None
        else:
            self.days_since_last_snowfall = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.albedo = None
        else:
            self.albedo = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.liquid_precipitation_depth = None
        else:
            self.liquid_precipitation_depth = str(vals[i])
        i += 1
        if len(vals[i]) == 0:
            self.liquid_precipitation_quantity = None
        else:
            self.liquid_precipitation_quantity = str(vals[i])
        i += 1

    @property
    def year(self):
        """Get year."""
        return self._year

    @year.setter
    def year(self, value=None):
        """Corresponds to IDD Field `year`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field year'.format(value))

        self._year = value

    @property
    def month(self):
        """Get month."""
        return self._month

    @month.setter
    def month(self, value=None):
        """Corresponds to IDD Field `month`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field month'.format(value))

        self._month = value

    @property
    def day(self):
        """Get day."""
        return self._day

    @day.setter
    def day(self, value=None):
        """Corresponds to IDD Field `day`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field day'.format(value))

        self._day = value

    @property
    def hour(self):
        """Get hour."""
        return self._hour

    @hour.setter
    def hour(self, value=None):
        """Corresponds to IDD Field `hour`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field hour'.format(value))

        self._hour = value

    @property
    def minute(self):
        """Get minute."""
        return self._minute

    @minute.setter
    def minute(self, value=None):
        """Corresponds to IDD Field `minute`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field minute'.format(value))

        self._minute = value

    @property
    def data_source_and_uncertainty_flags(self):
        """Get data_source_and_uncertainty_flags."""
        return self._data_source_and_uncertainty_flags

    @data_source_and_uncertainty_flags.setter
    def data_source_and_uncertainty_flags(self, value=None):
        """Corresponds to IDD Field `data_source_and_uncertainty_flags` Initial
        day of weather file is checked by EnergyPlus for validity (as shown
        below) Each field is checked for "missing" as shown below.

        Reasonable values, calculated values or the last "good" value is
        substituted.

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type string for field data_source_and_uncertainty_flags'.format(value))

        self._data_source_and_uncertainty_flags = value

    @property
    def dry_bulb_temperature(self):
        """Get dry_bulb_temperature."""
        return self._dry_bulb_temperature

    @dry_bulb_temperature.setter
    def dry_bulb_temperature(self, value=99.9):
        """  Corresponds to IDD Field `dry_bulb_temperature`
        Unit: C
        value > -70.0
        value < 70.0
        Missing value: 99.9
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field dry_bulb_temperature'.format(value))
            if value <= -70.0:
                raise ValueError(
                    'value need to be greater -70.0 for field dry_bulb_temperature')
            if value >= 70.0:
                raise ValueError(
                    'value need to be smaller or equal 70.0 for field dry_bulb_temperature')

        self._dry_bulb_temperature = value

    @property
    def dew_point_temperature(self):
        """Get dew_point_temperature."""
        return self._dew_point_temperature

    @dew_point_temperature.setter
    def dew_point_temperature(self, value=99.9):
        """  Corresponds to IDD Field `dew_point_temperature`
        Unit: C
        value > -70.0
        value < 70.0
        Missing value: 99.9
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field dew_point_temperature'.format(value))
            if value <= -70.0:
                raise ValueError(
                    'value need to be greater -70.0 for field dew_point_temperature')
            if value >= 70.0:
                raise ValueError(
                    'value need to be smaller or equal 70.0 for field dew_point_temperature')

        self._dew_point_temperature = value

    @property
    def relative_humidity(self):
        """Get relative_humidity."""
        return self._relative_humidity

    @relative_humidity.setter
    def relative_humidity(self, value=999.0):
        """  Corresponds to IDD Field `relative_humidity`
        value >= 0.0
        value <= 110.0
        Missing value: 999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field relative_humidity'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field relative_humidity')
            if value > 110.0:
                raise ValueError(
                    'value need to be smaller 110.0 for field relative_humidity')

        self._relative_humidity = value

    @property
    def atmospheric_station_pressure(self):
        """Get atmospheric_station_pressure."""
        return self._atmospheric_station_pressure

    @atmospheric_station_pressure.setter
    def atmospheric_station_pressure(self, value=999999.0):
        """  Corresponds to IDD Field `atmospheric_station_pressure`
        Unit: Pa
        value > 31000.0
        value < 120000.0
        Missing value: 999999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field atmospheric_station_pressure'.format(value))
            if value <= 31000.0:
                raise ValueError(
                    'value need to be greater 31000.0 for field atmospheric_station_pressure')
            if value >= 120000.0:
                raise ValueError(
                    'value need to be smaller or equal 120000.0 for field atmospheric_station_pressure')

        self._atmospheric_station_pressure = value

    @property
    def extraterrestrial_horizontal_radiation(self):
        """Get extraterrestrial_horizontal_radiation."""
        return self._extraterrestrial_horizontal_radiation

    @extraterrestrial_horizontal_radiation.setter
    def extraterrestrial_horizontal_radiation(self, value=9999.0):
        """  Corresponds to IDD Field `extraterrestrial_horizontal_radiation`
        Unit: Wh/m2
        value >= 0.0
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field extraterrestrial_horizontal_radiation'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field extraterrestrial_horizontal_radiation')

        self._extraterrestrial_horizontal_radiation = value

    @property
    def extraterrestrial_direct_normal_radiation(self):
        """Get extraterrestrial_direct_normal_radiation."""
        return self._extraterrestrial_direct_normal_radiation

    @extraterrestrial_direct_normal_radiation.setter
    def extraterrestrial_direct_normal_radiation(self, value=9999.0):
        """  Corresponds to IDD Field `extraterrestrial_direct_normal_radiation`
        Unit: Wh/m2
        value >= 0.0
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field extraterrestrial_direct_normal_radiation'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field extraterrestrial_direct_normal_radiation')

        self._extraterrestrial_direct_normal_radiation = value

    @property
    def horizontal_infrared_radiation_intensity(self):
        """Get horizontal_infrared_radiation_intensity."""
        return self._horizontal_infrared_radiation_intensity

    @horizontal_infrared_radiation_intensity.setter
    def horizontal_infrared_radiation_intensity(self, value=9999.0):
        """  Corresponds to IDD Field `horizontal_infrared_radiation_intensity`
        Unit: Wh/m2
        value >= 0.0
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field horizontal_infrared_radiation_intensity'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field horizontal_infrared_radiation_intensity')

        self._horizontal_infrared_radiation_intensity = value

    @property
    def global_horizontal_radiation(self):
        """Get global_horizontal_radiation."""
        return self._global_horizontal_radiation

    @global_horizontal_radiation.setter
    def global_horizontal_radiation(self, value=9999.0):
        """  Corresponds to IDD Field `global_horizontal_radiation`
        Unit: Wh/m2
        value >= 0.0
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field global_horizontal_radiation'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field global_horizontal_radiation')

        self._global_horizontal_radiation = value

    @property
    def direct_normal_radiation(self):
        """Get direct_normal_radiation."""
        return self._direct_normal_radiation

    @direct_normal_radiation.setter
    def direct_normal_radiation(self, value=9999.0):
        """  Corresponds to IDD Field `direct_normal_radiation`
        Unit: Wh/m2
        value >= 0.0
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field direct_normal_radiation'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field direct_normal_radiation')

        self._direct_normal_radiation = value

    @property
    def diffuse_horizontal_radiation(self):
        """Get diffuse_horizontal_radiation."""
        return self._diffuse_horizontal_radiation

    @diffuse_horizontal_radiation.setter
    def diffuse_horizontal_radiation(self, value=9999.0):
        """  Corresponds to IDD Field `diffuse_horizontal_radiation`
        Unit: Wh/m2
        value >= 0.0
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field diffuse_horizontal_radiation'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field diffuse_horizontal_radiation')

        self._diffuse_horizontal_radiation = value

    @property
    def global_horizontal_illuminance(self):
        """Get global_horizontal_illuminance."""
        return self._global_horizontal_illuminance

    @global_horizontal_illuminance.setter
    def global_horizontal_illuminance(self, value=999999.0):
        """  Corresponds to IDD Field `global_horizontal_illuminance`
        will be missing if >= 999900
        Unit: lux
        value >= 0.0
        Missing value: 999999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field global_horizontal_illuminance'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field global_horizontal_illuminance')

        self._global_horizontal_illuminance = value

    @property
    def direct_normal_illuminance(self):
        """Get direct_normal_illuminance."""
        return self._direct_normal_illuminance

    @direct_normal_illuminance.setter
    def direct_normal_illuminance(self, value=999999.0):
        """  Corresponds to IDD Field `direct_normal_illuminance`
        will be missing if >= 999900
        Unit: lux
        value >= 0.0
        Missing value: 999999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field direct_normal_illuminance'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field direct_normal_illuminance')

        self._direct_normal_illuminance = value

    @property
    def diffuse_horizontal_illuminance(self):
        """Get diffuse_horizontal_illuminance."""
        return self._diffuse_horizontal_illuminance

    @diffuse_horizontal_illuminance.setter
    def diffuse_horizontal_illuminance(self, value=999999.0):
        """  Corresponds to IDD Field `diffuse_horizontal_illuminance`
        will be missing if >= 999900
        Unit: lux
        value >= 0.0
        Missing value: 999999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field diffuse_horizontal_illuminance'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field diffuse_horizontal_illuminance')

        self._diffuse_horizontal_illuminance = value

    @property
    def zenith_luminance(self):
        """Get zenith_luminance."""
        return self._zenith_luminance

    @zenith_luminance.setter
    def zenith_luminance(self, value=9999.0):
        """  Corresponds to IDD Field `zenith_luminance`
        will be missing if >= 9999
        Unit: Cd/m2
        value >= 0.0
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field zenith_luminance'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field zenith_luminance')

        self._zenith_luminance = value

    @property
    def wind_direction(self):
        """Get wind_direction."""
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value=999.0):
        """  Corresponds to IDD Field `wind_direction`
        Unit: degrees
        value >= 0.0
        value <= 360.0
        Missing value: 999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field wind_direction'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field wind_direction')
            if value > 360.0:
                raise ValueError(
                    'value need to be smaller 360.0 for field wind_direction')

        self._wind_direction = value

    @property
    def wind_speed(self):
        """Get wind_speed."""
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value=999.0):
        """  Corresponds to IDD Field `wind_speed`
        Unit: m/s
        value >= 0.0
        value <= 40.0
        Missing value: 999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field wind_speed'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field wind_speed')
            if value > 40.0:
                raise ValueError(
                    'value need to be smaller 40.0 for field wind_speed')

        self._wind_speed = value

    @property
    def total_sky_cover(self):
        """Get total_sky_cover."""
        return self._total_sky_cover

    @total_sky_cover.setter
    def total_sky_cover(self, value=99.0):
        """  Corresponds to IDD Field `total_sky_cover`
        value >= 0.0
        value <= 10.0
        Missing value: 99.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field total_sky_cover'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field total_sky_cover')
            if value > 10.0:
                raise ValueError(
                    'value need to be smaller 10.0 for field total_sky_cover')

        self._total_sky_cover = value

    @property
    def opaque_sky_cover_used_if_horizontal_ir_intensity_missing(self):
        """Get opaque_sky_cover_used_if_horizontal_ir_intensity_missing."""
        return self._opaque_sky_cover_used_if_horizontal_ir_intensity_missing

    @opaque_sky_cover_used_if_horizontal_ir_intensity_missing.setter
    def opaque_sky_cover_used_if_horizontal_ir_intensity_missing(
            self,
            value=99.0):
        """  Corresponds to IDD Field `opaque_sky_cover_used_if_horizontal_ir_intensity_missing`
        value >= 0.0
        value <= 10.0
        Missing value: 99.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field opaque_sky_cover_used_if_horizontal_ir_intensity_missing'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 for field opaque_sky_cover_used_if_horizontal_ir_intensity_missing')
            if value > 10.0:
                raise ValueError(
                    'value need to be smaller 10.0 for field opaque_sky_cover_used_if_horizontal_ir_intensity_missing')

        self._opaque_sky_cover_used_if_horizontal_ir_intensity_missing = value

    @property
    def visibility(self):
        """Get visibility."""
        return self._visibility

    @visibility.setter
    def visibility(self, value=9999.0):
        """  Corresponds to IDD Field `visibility`
        Unit: km
        Missing value: 9999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field visibility'.format(value))

        self._visibility = value

    @property
    def ceiling_height(self):
        """Get ceiling_height."""
        return self._ceiling_height

    @ceiling_height.setter
    def ceiling_height(self, value=99999.0):
        """  Corresponds to IDD Field `ceiling_height`
        Unit: m
        Missing value: 99999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field ceiling_height'.format(value))

        self._ceiling_height = value

    @property
    def present_weather_observation(self):
        """Get present_weather_observation."""
        return self._present_weather_observation

    @present_weather_observation.setter
    def present_weather_observation(self, value=None):
        """Corresponds to IDD Field `present_weather_observation`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field present_weather_observation'.format(value))

        self._present_weather_observation = value

    @property
    def present_weather_codes(self):
        """Get present_weather_codes."""
        return self._present_weather_codes

    @present_weather_codes.setter
    def present_weather_codes(self, value=None):
        """Corresponds to IDD Field `present_weather_codes`"""
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field present_weather_codes'.format(value))

        self._present_weather_codes = value

    @property
    def precipitable_water(self):
        """Get precipitable_water."""
        return self._precipitable_water

    @precipitable_water.setter
    def precipitable_water(self, value=999.0):
        """  Corresponds to IDD Field `precipitable_water`
        Unit: mm
        Missing value: 999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field precipitable_water'.format(value))

        self._precipitable_water = value

    @property
    def aerosol_optical_depth(self):
        """Get aerosol_optical_depth."""
        return self._aerosol_optical_depth

    @aerosol_optical_depth.setter
    def aerosol_optical_depth(self, value=0.999):
        """  Corresponds to IDD Field `aerosol_optical_depth`
        Unit: thousandths
        Missing value: 0.999
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field aerosol_optical_depth'.format(value))

        self._aerosol_optical_depth = value

    @property
    def snow_depth(self):
        """Get snow_depth."""
        return self._snow_depth

    @snow_depth.setter
    def snow_depth(self, value=999.0):
        """  Corresponds to IDD Field `snow_depth`
        Unit: cm
        Missing value: 999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field snow_depth'.format(value))

        self._snow_depth = value

    @property
    def days_since_last_snowfall(self):
        """Get days_since_last_snowfall."""
        return self._days_since_last_snowfall

    @days_since_last_snowfall.setter
    def days_since_last_snowfall(self, value=99.0):
        """  Corresponds to IDD Field `days_since_last_snowfall`
        Missing value: 99.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field days_since_last_snowfall'.format(value))

        self._days_since_last_snowfall = value

    @property
    def albedo(self):
        """Get albedo."""
        return self._albedo

    @albedo.setter
    def albedo(self, value=999.0):
        """  Corresponds to IDD Field `albedo`
        Missing value: 999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field albedo'.format(value))

        self._albedo = value

    @property
    def liquid_precipitation_depth(self):
        """Get liquid_precipitation_depth."""
        return self._liquid_precipitation_depth

    @liquid_precipitation_depth.setter
    def liquid_precipitation_depth(self, value=999.0):
        """  Corresponds to IDD Field `liquid_precipitation_depth`
        Unit: mm
        Missing value: 999.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field liquid_precipitation_depth'.format(value))

        self._liquid_precipitation_depth = value

    @property
    def liquid_precipitation_quantity(self):
        """Get liquid_precipitation_quantity."""
        return self._liquid_precipitation_quantity

    @liquid_precipitation_quantity.setter
    def liquid_precipitation_quantity(self, value=99.0):
        """  Corresponds to IDD Field `liquid_precipitation_quantity`
        Unit: hr
        Missing value: 99.0
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float for field liquid_precipitation_quantity'.format(value))

        self._liquid_precipitation_quantity = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.year))
        out.append(self._to_str(self.month))
        out.append(self._to_str(self.day))
        out.append(self._to_str(self.hour))
        out.append(self._to_str(self.minute))
        out.append(self._to_str(self.data_source_and_uncertainty_flags))
        out.append(self._to_str(self.dry_bulb_temperature))
        out.append(self._to_str(self.dew_point_temperature))
        out.append(self._to_str(self.relative_humidity))
        out.append(self._to_str(self.atmospheric_station_pressure))
        out.append(self._to_str(self.extraterrestrial_horizontal_radiation))
        out.append(self._to_str(self.extraterrestrial_direct_normal_radiation))
        out.append(self._to_str(self.horizontal_infrared_radiation_intensity))
        out.append(self._to_str(self.global_horizontal_radiation))
        out.append(self._to_str(self.direct_normal_radiation))
        out.append(self._to_str(self.diffuse_horizontal_radiation))
        out.append(self._to_str(self.global_horizontal_illuminance))
        out.append(self._to_str(self.direct_normal_illuminance))
        out.append(self._to_str(self.diffuse_horizontal_illuminance))
        out.append(self._to_str(self.zenith_luminance))
        out.append(self._to_str(self.wind_direction))
        out.append(self._to_str(self.wind_speed))
        out.append(self._to_str(self.total_sky_cover))
        out.append(
            self._to_str(
                self.opaque_sky_cover_used_if_horizontal_ir_intensity_missing))
        out.append(self._to_str(self.visibility))
        out.append(self._to_str(self.ceiling_height))
        out.append(self._to_str(self.present_weather_observation))
        out.append(self._to_str(self.present_weather_codes))
        out.append(self._to_str(self.precipitable_water))
        out.append(self._to_str(self.aerosol_optical_depth))
        out.append(self._to_str(self.snow_depth))
        out.append(self._to_str(self.days_since_last_snowfall))
        out.append(self._to_str(self.albedo))
        out.append(self._to_str(self.liquid_precipitation_depth))
        out.append(self._to_str(self.liquid_precipitation_quantity))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class EPW(object):

    def __init__(
            self,
            location=None,
            typical_or_extreme_periods=None,
            ground_temperatures=None,
            holidays_or_daylight_savings=None,
            comments_1=None,
            comments_2=None,
            data_periods=None,
            weatherdata=[]):
        self._data = OrderedDict()
        self._data["LOCATION"] = location
        self._data["TYPICAL/EXTREME PERIODS"] = typical_or_extreme_periods
        self._data["GROUND TEMPERATURES"] = ground_temperatures
        self._data["HOLIDAYS/DAYLIGHT SAVINGS"] = holidays_or_daylight_savings
        self._data["COMMENTS 1"] = comments_1
        self._data["COMMENTS 2"] = comments_2
        self._data["DATA PERIODS"] = data_periods
        self._data["WEATHER DATA"] = weatherdata

    @property
    def location(self):
        """Get location data dictionary object."""
        return self._data["LOCATION"]

    @location.setter
    def location(self, data_dictionary):
        """Set location data dictionary object."""
        self._data["LOCATION"] = data_dictionary

    @property
    def typical_or_extreme_periods(self):
        """Get typical_or_extreme_periods data dictionary object."""
        return self._data["TYPICAL/EXTREME PERIODS"]

    @typical_or_extreme_periods.setter
    def typical_or_extreme_periods(self, data_dictionary):
        """Set typical_or_extreme_periods data dictionary object."""
        self._data["TYPICAL/EXTREME PERIODS"] = data_dictionary

    @property
    def ground_temperatures(self):
        """Get ground_temperatures data dictionary object."""
        return self._data["GROUND TEMPERATURES"]

    @ground_temperatures.setter
    def ground_temperatures(self, data_dictionary):
        """Set ground_temperatures data dictionary object."""
        self._data["GROUND TEMPERATURES"] = data_dictionary

    @property
    def holidays_or_daylight_savings(self):
        """Get holidays_or_daylight_savings data dictionary object."""
        return self._data["HOLIDAYS/DAYLIGHT SAVINGS"]

    @holidays_or_daylight_savings.setter
    def holidays_or_daylight_savings(self, data_dictionary):
        """Set holidays_or_daylight_savings data dictionary object."""
        self._data["HOLIDAYS/DAYLIGHT SAVINGS"] = data_dictionary

    @property
    def comments_1(self):
        """Get comments_1 data dictionary object."""
        return self._data["COMMENTS 1"]

    @comments_1.setter
    def comments_1(self, data_dictionary):
        """Set comments_1 data dictionary object."""
        self._data["COMMENTS 1"] = data_dictionary

    @property
    def comments_2(self):
        """Get comments_2 data dictionary object."""
        return self._data["COMMENTS 2"]

    @comments_2.setter
    def comments_2(self, data_dictionary):
        """Set comments_2 data dictionary object."""
        self._data["COMMENTS 2"] = data_dictionary

    @property
    def data_periods(self):
        """Get data_periods data dictionary object."""
        return self._data["DATA PERIODS"]

    @data_periods.setter
    def data_periods(self, data_dictionary):
        """Set data_periods data dictionary object."""
        self._data["DATA PERIODS"] = data_dictionary

    @property
    def weatherdata(self):
        """Get list of WeatherData data dictionary objects."""
        return self._data["WEATHER DATA"]

    @weatherdata.setter
    def weatherdata(self, weatherdata):
        """Set list of WeatherData data dictionary objects."""
        self._data["WEATHER DATA"] = weatherdata

    def add_weatherdata(self, data):
        """Add weather data, data need to be of type WeatherData."""
        if not isinstance(data, WeatherData):
            raise ValueError('Weather data need to be of type WeatherData')
        self._data["WEATHER DATA"].append(data)

    def save(self, path):
        """Save WeatherData in EPW format to path."""
        with open(path, 'w') as f:
            f.write(self._data["LOCATION"].export() + "\n")
            f.write(self._data["TYPICAL/EXTREME PERIODS"].export() + "\n")
            f.write(self._data["GROUND TEMPERATURES"].export() + "\n")
            f.write(self._data["HOLIDAYS/DAYLIGHT SAVINGS"].export() + "\n")
            f.write(self._data["COMMENTS 1"].export() + "\n")
            f.write(self._data["COMMENTS 2"].export() + "\n")
            f.write(self._data["DATA PERIODS"].export() + "\n")
            for item in self._data["WEATHER DATA"]:
                f.write(item.export(False) + "\n")

    def _create_datadict(self, internal_name):
        if internal_name == "LOCATION":
            return Location()
        if internal_name == "TYPICAL/EXTREME PERIODS":
            return TypicalOrExtremePeriods()
        if internal_name == "GROUND TEMPERATURES":
            return GroundTemperatures()
        if internal_name == "HOLIDAYS/DAYLIGHT SAVINGS":
            return HolidaysOrDaylightSavings()
        if internal_name == "COMMENTS 1":
            return Comments1()
        if internal_name == "COMMENTS 2":
            return Comments2()
        if internal_name == "DATA PERIODS":
            return DataPeriods()
        raise ValueError(
            "No DataDictionary known for {}".format(internal_name))

    def read(self, path):
        """Read EPW weather data from path."""
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                match_obj_name = re.search(r"^([A-Z][A-Z/ \d]+),", line)
                if match_obj_name is not None:
                    internal_name = match_obj_name.group(1)
                    if internal_name in self._data:
                        self._data[internal_name] = self._create_datadict(
                            internal_name)
                        data_line = line[len(internal_name) + 1:]
                        vals = data_line.strip().split(',')
                        self._data[internal_name].read(vals)
                else:
                    wd = WeatherData()
                    wd.read(line.strip().split(','))
                    self.add_weatherdata(wd)
