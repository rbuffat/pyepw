#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on the EPW IDD specification given in the document
Auxiliary EnergyPlus Programs - Extra programs for EnergyPlus,
Date: November 22 2013

Do not expect that it actually works!

Generation date: 2014-11-28

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
            self.city = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.state_province_region = None
        else:
            self.state_province_region = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.country = None
        else:
            self.country = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source = None
        else:
            self.source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wmo = None
        else:
            self.wmo = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latitude = None
        else:
            self.latitude = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.longitude = None
        else:
            self.longitude = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.timezone = None
        else:
            self.timezone = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.elevation = None
        else:
            self.elevation = vals[i]
        i += 1

    @property
    def city(self):
        """Get city.

        Returns:
            str: The value of `city` or None if not set

        """
        return self._city

    @city.setter
    def city(self, value=None):
        """Corresponds to IDD Field `city`

        Args:
            value (str): value for IDD Field `city`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `city`'.format(value))

        self._city = value

    @property
    def state_province_region(self):
        """Get state_province_region.

        Returns:
            str: The value of `state_province_region` or None if not set

        """
        return self._state_province_region

    @state_province_region.setter
    def state_province_region(self, value=None):
        """Corresponds to IDD Field `state_province_region`

        Args:
            value (str): value for IDD Field `state_province_region`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `state_province_region`'.format(value))

        self._state_province_region = value

    @property
    def country(self):
        """Get country.

        Returns:
            str: The value of `country` or None if not set

        """
        return self._country

    @country.setter
    def country(self, value=None):
        """Corresponds to IDD Field `country`

        Args:
            value (str): value for IDD Field `country`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `country`'.format(value))

        self._country = value

    @property
    def source(self):
        """Get source.

        Returns:
            str: The value of `source` or None if not set

        """
        return self._source

    @source.setter
    def source(self, value=None):
        """Corresponds to IDD Field `source`

        Args:
            value (str): value for IDD Field `source`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source`'.format(value))

        self._source = value

    @property
    def wmo(self):
        """Get wmo.

        Returns:
            str: The value of `wmo` or None if not set

        """
        return self._wmo

    @wmo.setter
    def wmo(self, value=None):
        """Corresponds to IDD Field `wmo` usually a 6 digit field. Used as
        alpha in EnergyPlus.

        Args:
            value (str): value for IDD Field `wmo`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wmo`'.format(value))

        self._wmo = value

    @property
    def latitude(self):
        """Get latitude.

        Returns:
            float: The value of `latitude` or None if not set

        """
        return self._latitude

    @latitude.setter
    def latitude(self, value=0.0):
        """Corresponds to IDD Field `latitude`

        + is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)

        Args:
            value (float): value for IDD Field `latitude`
                Unit: deg
                Default value: 0.0
                value >= -90.0
                value <= 90.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `latitude`'.format(value))
            if value < -90.0:
                raise ValueError('value need to be greater or equal -90.0 '
                                 'for field `latitude`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `latitude`')

        self._latitude = value

    @property
    def longitude(self):
        """Get longitude.

        Returns:
            float: The value of `longitude` or None if not set

        """
        return self._longitude

    @longitude.setter
    def longitude(self, value=0.0):
        """Corresponds to IDD Field `longitude`

        - is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)

        Args:
            value (float): value for IDD Field `longitude`
                Unit: deg
                Default value: 0.0
                value >= -180.0
                value <= 180.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `longitude`'.format(value))
            if value < -180.0:
                raise ValueError('value need to be greater or equal -180.0 '
                                 'for field `longitude`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `longitude`')

        self._longitude = value

    @property
    def timezone(self):
        """Get timezone.

        Returns:
            float: The value of `timezone` or None if not set

        """
        return self._timezone

    @timezone.setter
    def timezone(self, value=0.0):
        """Corresponds to IDD Field `timezone` Time relative to GMT.

        Args:
            value (float): value for IDD Field `timezone`
                Unit: hr - not on standard units list???
                Default value: 0.0
                value >= -12.0
                value <= 12.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `timezone`'.format(value))
            if value < -12.0:
                raise ValueError('value need to be greater or equal -12.0 '
                                 'for field `timezone`')
            if value > 12.0:
                raise ValueError('value need to be smaller 12.0 '
                                 'for field `timezone`')

        self._timezone = value

    @property
    def elevation(self):
        """Get elevation.

        Returns:
            float: The value of `elevation` or None if not set

        """
        return self._elevation

    @elevation.setter
    def elevation(self, value=0.0):
        """Corresponds to IDD Field `elevation`

        Args:
            value (float): value for IDD Field `elevation`
                Unit: m
                Default value: 0.0
                value >= -1000.0
                value < 9999.9
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `elevation`'.format(value))
            if value < -1000.0:
                raise ValueError('value need to be greater or equal -1000.0 '
                                 'for field `elevation`')
            if value >= 9999.9:
                raise ValueError('value need to be smaller 9999.9 '
                                 'for field `elevation`')

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


class DesignCondition(object):

    """Corresponds to EPW IDD object `DESIGN CONDITION`"""
    _internal_name = "DESIGN CONDITION"
    _field_count = 68

    def __init__(self):
        self._title_of_design_condition = None
        self._unkown_field = None
        self._design_stat_heating = None
        self._coldestmonth = None
        self._db996 = None
        self._db990 = None
        self._dp996 = None
        self._hr_dp996 = None
        self._db_dp996 = None
        self._dp990 = None
        self._hr_dp990 = None
        self._db_dp990 = None
        self._ws004c = None
        self._db_ws004c = None
        self._ws010c = None
        self._db_ws010c = None
        self._ws_db996 = None
        self._wd_db996 = None
        self._design_stat_cooling = None
        self._hottestmonth = None
        self._dbr = None
        self._db004 = None
        self._wb_db004 = None
        self._db010 = None
        self._wb_db010 = None
        self._db020 = None
        self._wb_db020 = None
        self._wb004 = None
        self._db_wb004 = None
        self._wb010 = None
        self._db_wb010 = None
        self._wb020 = None
        self._db_wb020 = None
        self._ws_db004 = None
        self._wd_db004 = None
        self._dp004 = None
        self._hr_dp004 = None
        self._db_dp004 = None
        self._dp010 = None
        self._hr_dp010 = None
        self._db_dp010 = None
        self._dp020 = None
        self._hr_dp020 = None
        self._db_dp020 = None
        self._en004 = None
        self._db_en004 = None
        self._en010 = None
        self._db_en010 = None
        self._en020 = None
        self._db_en020 = None
        self._hrs_84_and_db12_8_or_20_6 = None
        self._design_stat_extremes = None
        self._ws010 = None
        self._ws025 = None
        self._ws050 = None
        self._wbmax = None
        self._dbmin_mean = None
        self._dbmax_mean = None
        self._dbmin_stddev = None
        self._dbmax_stddev = None
        self._dbmin05years = None
        self._dbmax05years = None
        self._dbmin10years = None
        self._dbmax10years = None
        self._dbmin20years = None
        self._dbmax20years = None
        self._dbmin50years = None
        self._dbmax50years = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.title_of_design_condition = None
        else:
            self.title_of_design_condition = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.unkown_field = None
        else:
            self.unkown_field = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_stat_heating = None
        else:
            self.design_stat_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coldestmonth = None
        else:
            self.coldestmonth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db996 = None
        else:
            self.db996 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db990 = None
        else:
            self.db990 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dp996 = None
        else:
            self.dp996 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hr_dp996 = None
        else:
            self.hr_dp996 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_dp996 = None
        else:
            self.db_dp996 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dp990 = None
        else:
            self.dp990 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hr_dp990 = None
        else:
            self.hr_dp990 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_dp990 = None
        else:
            self.db_dp990 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ws004c = None
        else:
            self.ws004c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_ws004c = None
        else:
            self.db_ws004c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ws010c = None
        else:
            self.ws010c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_ws010c = None
        else:
            self.db_ws010c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ws_db996 = None
        else:
            self.ws_db996 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wd_db996 = None
        else:
            self.wd_db996 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_stat_cooling = None
        else:
            self.design_stat_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hottestmonth = None
        else:
            self.hottestmonth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbr = None
        else:
            self.dbr = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db004 = None
        else:
            self.db004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wb_db004 = None
        else:
            self.wb_db004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db010 = None
        else:
            self.db010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wb_db010 = None
        else:
            self.wb_db010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db020 = None
        else:
            self.db020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wb_db020 = None
        else:
            self.wb_db020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wb004 = None
        else:
            self.wb004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_wb004 = None
        else:
            self.db_wb004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wb010 = None
        else:
            self.wb010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_wb010 = None
        else:
            self.db_wb010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wb020 = None
        else:
            self.wb020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_wb020 = None
        else:
            self.db_wb020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ws_db004 = None
        else:
            self.ws_db004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wd_db004 = None
        else:
            self.wd_db004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dp004 = None
        else:
            self.dp004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hr_dp004 = None
        else:
            self.hr_dp004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_dp004 = None
        else:
            self.db_dp004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dp010 = None
        else:
            self.dp010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hr_dp010 = None
        else:
            self.hr_dp010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_dp010 = None
        else:
            self.db_dp010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dp020 = None
        else:
            self.dp020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hr_dp020 = None
        else:
            self.hr_dp020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_dp020 = None
        else:
            self.db_dp020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.en004 = None
        else:
            self.en004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_en004 = None
        else:
            self.db_en004 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.en010 = None
        else:
            self.en010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_en010 = None
        else:
            self.db_en010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.en020 = None
        else:
            self.en020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.db_en020 = None
        else:
            self.db_en020 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hrs_84_and_db12_8_or_20_6 = None
        else:
            self.hrs_84_and_db12_8_or_20_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_stat_extremes = None
        else:
            self.design_stat_extremes = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ws010 = None
        else:
            self.ws010 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ws025 = None
        else:
            self.ws025 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ws050 = None
        else:
            self.ws050 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wbmax = None
        else:
            self.wbmax = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmin_mean = None
        else:
            self.dbmin_mean = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmax_mean = None
        else:
            self.dbmax_mean = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmin_stddev = None
        else:
            self.dbmin_stddev = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmax_stddev = None
        else:
            self.dbmax_stddev = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmin05years = None
        else:
            self.dbmin05years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmax05years = None
        else:
            self.dbmax05years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmin10years = None
        else:
            self.dbmin10years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmax10years = None
        else:
            self.dbmax10years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmin20years = None
        else:
            self.dbmin20years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmax20years = None
        else:
            self.dbmax20years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmin50years = None
        else:
            self.dbmin50years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dbmax50years = None
        else:
            self.dbmax50years = vals[i]
        i += 1

    @property
    def title_of_design_condition(self):
        """Get title_of_design_condition.

        Returns:
            str: The value of `title_of_design_condition` or None if not set

        """
        return self._title_of_design_condition

    @title_of_design_condition.setter
    def title_of_design_condition(self, value=None):
        """Corresponds to IDD Field `title_of_design_condition`

        Args:
            value (str): value for IDD Field `title_of_design_condition`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `title_of_design_condition`'.format(value))

        self._title_of_design_condition = value

    @property
    def unkown_field(self):
        """Get unkown_field.

        Returns:
            str: The value of `unkown_field` or None if not set

        """
        return self._unkown_field

    @unkown_field.setter
    def unkown_field(self, value=None):
        """Corresponds to IDD Field `unkown_field` Empty field in data.

        Args:
            value (str): value for IDD Field `unkown_field`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `unkown_field`'.format(value))

        self._unkown_field = value

    @property
    def design_stat_heating(self):
        """Get design_stat_heating.

        Returns:
            str: The value of `design_stat_heating` or None if not set

        """
        return self._design_stat_heating

    @design_stat_heating.setter
    def design_stat_heating(self, value="Heating"):
        """Corresponds to IDD Field `design_stat_heating`

        Args:
            value (str): value for IDD Field `design_stat_heating`
                Accepted values are:
                      - Heating
                Default value: Heating
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `design_stat_heating`'.format(value))
            vals = set()
            vals.add("Heating")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_stat_heating`'.format(value))

        self._design_stat_heating = value

    @property
    def coldestmonth(self):
        """Get coldestmonth.

        Returns:
            int: The value of `coldestmonth` or None if not set

        """
        return self._coldestmonth

    @coldestmonth.setter
    def coldestmonth(self, value=None):
        """Corresponds to IDD Field `coldestmonth`

        Args:
            value (int): value for IDD Field `coldestmonth`
                value >= 1
                value <= 12
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `coldestmonth`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `coldestmonth`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `coldestmonth`')

        self._coldestmonth = value

    @property
    def db996(self):
        """Get db996.

        Returns:
            float: The value of `db996` or None if not set

        """
        return self._db996

    @db996.setter
    def db996(self, value=None):
        """  Corresponds to IDD Field `db996`
        Dry-bulb temperature corresponding to 99.6% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `db996`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db996`'.format(value))

        self._db996 = value

    @property
    def db990(self):
        """Get db990.

        Returns:
            float: The value of `db990` or None if not set

        """
        return self._db990

    @db990.setter
    def db990(self, value=None):
        """  Corresponds to IDD Field `db990`
        Dry-bulb temperature corresponding to 90.0% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `db990`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db990`'.format(value))

        self._db990 = value

    @property
    def dp996(self):
        """Get dp996.

        Returns:
            float: The value of `dp996` or None if not set

        """
        return self._dp996

    @dp996.setter
    def dp996(self, value=None):
        """  Corresponds to IDD Field `dp996`
        Dew-point temperature corresponding to 99.6% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `dp996`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dp996`'.format(value))

        self._dp996 = value

    @property
    def hr_dp996(self):
        """Get hr_dp996.

        Returns:
            float: The value of `hr_dp996` or None if not set

        """
        return self._hr_dp996

    @hr_dp996.setter
    def hr_dp996(self, value=None):
        """  Corresponds to IDD Field `hr_dp996`
        humidity ratio, calculated at standard atmospheric pressure
        at elevation of station, corresponding to
        Dew-point temperature corresponding to 99.6% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `hr_dp996`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hr_dp996`'.format(value))

        self._hr_dp996 = value

    @property
    def db_dp996(self):
        """Get db_dp996.

        Returns:
            float: The value of `db_dp996` or None if not set

        """
        return self._db_dp996

    @db_dp996.setter
    def db_dp996(self, value=None):
        """  Corresponds to IDD Field `db_dp996`
        mean coincident drybulb temperature corresponding to
        Dew-point temperature corresponding to 99.6% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `db_dp996`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_dp996`'.format(value))

        self._db_dp996 = value

    @property
    def dp990(self):
        """Get dp990.

        Returns:
            float: The value of `dp990` or None if not set

        """
        return self._dp990

    @dp990.setter
    def dp990(self, value=None):
        """  Corresponds to IDD Field `dp990`
        Dew-point temperature corresponding to 90.0% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `dp990`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dp990`'.format(value))

        self._dp990 = value

    @property
    def hr_dp990(self):
        """Get hr_dp990.

        Returns:
            float: The value of `hr_dp990` or None if not set

        """
        return self._hr_dp990

    @hr_dp990.setter
    def hr_dp990(self, value=None):
        """  Corresponds to IDD Field `hr_dp990`
        humidity ratio, calculated at standard atmospheric pressure
        at elevation of station, corresponding to
        Dew-point temperature corresponding to 90.0% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `hr_dp990`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hr_dp990`'.format(value))

        self._hr_dp990 = value

    @property
    def db_dp990(self):
        """Get db_dp990.

        Returns:
            float: The value of `db_dp990` or None if not set

        """
        return self._db_dp990

    @db_dp990.setter
    def db_dp990(self, value=None):
        """  Corresponds to IDD Field `db_dp990`
        mean coincident drybulb temperature corresponding to
        Dew-point temperature corresponding to 90.0% annual cumulative
        frequency of occurrence (cold conditions)

        Args:
            value (float): value for IDD Field `db_dp990`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_dp990`'.format(value))

        self._db_dp990 = value

    @property
    def ws004c(self):
        """Get ws004c.

        Returns:
            float: The value of `ws004c` or None if not set

        """
        return self._ws004c

    @ws004c.setter
    def ws004c(self, value=None):
        """Corresponds to IDD Field `ws004c`

        Args:
            value (float): value for IDD Field `ws004c`
                Unit: m/s
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ws004c`'.format(value))

        self._ws004c = value

    @property
    def db_ws004c(self):
        """Get db_ws004c.

        Returns:
            float: The value of `db_ws004c` or None if not set

        """
        return self._db_ws004c

    @db_ws004c.setter
    def db_ws004c(self, value=None):
        """  Corresponds to IDD Field `db_ws004c`
        Mean coincident dry-bulb temperature to wind speed corresponding to 0.40% cumulative frequency for coldest month

        Args:
            value (float): value for IDD Field `db_ws004c`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_ws004c`'.format(value))

        self._db_ws004c = value

    @property
    def ws010c(self):
        """Get ws010c.

        Returns:
            float: The value of `ws010c` or None if not set

        """
        return self._ws010c

    @ws010c.setter
    def ws010c(self, value=None):
        """  Corresponds to IDD Field `ws010c`
        Wind speed corresponding to 1.0% cumulative frequency
        of occurrence for coldest month;

        Args:
            value (float): value for IDD Field `ws010c`
                Unit: m/s
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ws010c`'.format(value))

        self._ws010c = value

    @property
    def db_ws010c(self):
        """Get db_ws010c.

        Returns:
            float: The value of `db_ws010c` or None if not set

        """
        return self._db_ws010c

    @db_ws010c.setter
    def db_ws010c(self, value=None):
        """  Corresponds to IDD Field `db_ws010c`
        Mean coincident dry-bulb temperature to wind speed corresponding to 1.0% cumulative frequency for coldest month

        Args:
            value (float): value for IDD Field `db_ws010c`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_ws010c`'.format(value))

        self._db_ws010c = value

    @property
    def ws_db996(self):
        """Get ws_db996.

        Returns:
            float: The value of `ws_db996` or None if not set

        """
        return self._ws_db996

    @ws_db996.setter
    def ws_db996(self, value=None):
        """  Corresponds to IDD Field `ws_db996`
        Mean wind speed coincident with 99.6% dry-bulb temperature

        Args:
            value (float): value for IDD Field `ws_db996`
                Unit: m/s
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ws_db996`'.format(value))

        self._ws_db996 = value

    @property
    def wd_db996(self):
        """Get wd_db996.

        Returns:
            float: The value of `wd_db996` or None if not set

        """
        return self._wd_db996

    @wd_db996.setter
    def wd_db996(self, value=None):
        """  Corresponds to IDD Field `wd_db996`
        most frequent wind direction corresponding to mean wind speed coincident with 99.6% dry-bulb temperature
        degrees from north (east = 90 deg)

        Args:
            value (float): value for IDD Field `wd_db996`
                Unit: deg
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wd_db996`'.format(value))

        self._wd_db996 = value

    @property
    def design_stat_cooling(self):
        """Get design_stat_cooling.

        Returns:
            str: The value of `design_stat_cooling` or None if not set

        """
        return self._design_stat_cooling

    @design_stat_cooling.setter
    def design_stat_cooling(self, value="Cooling"):
        """Corresponds to IDD Field `design_stat_cooling`

        Args:
            value (str): value for IDD Field `design_stat_cooling`
                Accepted values are:
                      - Cooling
                Default value: Cooling
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `design_stat_cooling`'.format(value))
            vals = set()
            vals.add("Cooling")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_stat_cooling`'.format(value))

        self._design_stat_cooling = value

    @property
    def hottestmonth(self):
        """Get hottestmonth.

        Returns:
            int: The value of `hottestmonth` or None if not set

        """
        return self._hottestmonth

    @hottestmonth.setter
    def hottestmonth(self, value=None):
        """Corresponds to IDD Field `hottestmonth`

        Args:
            value (int): value for IDD Field `hottestmonth`
                value >= 1
                value <= 12
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `hottestmonth`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `hottestmonth`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `hottestmonth`')

        self._hottestmonth = value

    @property
    def dbr(self):
        """Get dbr.

        Returns:
            float: The value of `dbr` or None if not set

        """
        return self._dbr

    @dbr.setter
    def dbr(self, value=None):
        """Corresponds to IDD Field `dbr` Daily temperature range for hottest
        month.

        [defined as mean of the difference between daily maximum
        and daily minimum dry-bulb temperatures for hottest month]

        Args:
            value (float): value for IDD Field `dbr`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbr`'.format(value))

        self._dbr = value

    @property
    def db004(self):
        """Get db004.

        Returns:
            float: The value of `db004` or None if not set

        """
        return self._db004

    @db004.setter
    def db004(self, value=None):
        """  Corresponds to IDD Field `db004`
        Dry-bulb temperature corresponding to 0.4% annual cumulative frequency of occurrence (warm conditions)

        Args:
            value (float): value for IDD Field `db004`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db004`'.format(value))

        self._db004 = value

    @property
    def wb_db004(self):
        """Get wb_db004.

        Returns:
            float: The value of `wb_db004` or None if not set

        """
        return self._wb_db004

    @wb_db004.setter
    def wb_db004(self, value=None):
        """  Corresponds to IDD Field `wb_db004`
        mean coincident wet-bulb temperature to
        Dry-bulb temperature corresponding to 0.4% annual cumulative frequency of occurrence (warm conditions)

        Args:
            value (float): value for IDD Field `wb_db004`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wb_db004`'.format(value))

        self._wb_db004 = value

    @property
    def db010(self):
        """Get db010.

        Returns:
            float: The value of `db010` or None if not set

        """
        return self._db010

    @db010.setter
    def db010(self, value=None):
        """  Corresponds to IDD Field `db010`
        Dry-bulb temperature corresponding to 1.0% annual cumulative frequency of occurrence (warm conditions)

        Args:
            value (float): value for IDD Field `db010`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db010`'.format(value))

        self._db010 = value

    @property
    def wb_db010(self):
        """Get wb_db010.

        Returns:
            float: The value of `wb_db010` or None if not set

        """
        return self._wb_db010

    @wb_db010.setter
    def wb_db010(self, value=None):
        """  Corresponds to IDD Field `wb_db010`
        mean coincident wet-bulb temperature to
        Dry-bulb temperature corresponding to 1.0% annual cumulative frequency of occurrence (warm conditions)

        Args:
            value (float): value for IDD Field `wb_db010`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wb_db010`'.format(value))

        self._wb_db010 = value

    @property
    def db020(self):
        """Get db020.

        Returns:
            float: The value of `db020` or None if not set

        """
        return self._db020

    @db020.setter
    def db020(self, value=None):
        """  Corresponds to IDD Field `db020`
        mean coincident wet-bulb temperature to
        Dry-bulb temperature corresponding to 2.0% annual cumulative frequency of occurrence (warm conditions)

        Args:
            value (float): value for IDD Field `db020`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db020`'.format(value))

        self._db020 = value

    @property
    def wb_db020(self):
        """Get wb_db020.

        Returns:
            float: The value of `wb_db020` or None if not set

        """
        return self._wb_db020

    @wb_db020.setter
    def wb_db020(self, value=None):
        """  Corresponds to IDD Field `wb_db020`
        mean coincident wet-bulb temperature to
        Dry-bulb temperature corresponding to 2.0% annual cumulative frequency of occurrence (warm conditions)

        Args:
            value (float): value for IDD Field `wb_db020`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wb_db020`'.format(value))

        self._wb_db020 = value

    @property
    def wb004(self):
        """Get wb004.

        Returns:
            float: The value of `wb004` or None if not set

        """
        return self._wb004

    @wb004.setter
    def wb004(self, value=None):
        """  Corresponds to IDD Field `wb004`
        Wet-bulb temperature corresponding to 0.4% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `wb004`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wb004`'.format(value))

        self._wb004 = value

    @property
    def db_wb004(self):
        """Get db_wb004.

        Returns:
            float: The value of `db_wb004` or None if not set

        """
        return self._db_wb004

    @db_wb004.setter
    def db_wb004(self, value=None):
        """  Corresponds to IDD Field `db_wb004`
        mean coincident dry-bulb temperature to
        Wet-bulb temperature corresponding to 0.4% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_wb004`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_wb004`'.format(value))

        self._db_wb004 = value

    @property
    def wb010(self):
        """Get wb010.

        Returns:
            float: The value of `wb010` or None if not set

        """
        return self._wb010

    @wb010.setter
    def wb010(self, value=None):
        """  Corresponds to IDD Field `wb010`
        Wet-bulb temperature corresponding to 1.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `wb010`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wb010`'.format(value))

        self._wb010 = value

    @property
    def db_wb010(self):
        """Get db_wb010.

        Returns:
            float: The value of `db_wb010` or None if not set

        """
        return self._db_wb010

    @db_wb010.setter
    def db_wb010(self, value=None):
        """  Corresponds to IDD Field `db_wb010`
        mean coincident dry-bulb temperature to
        Wet-bulb temperature corresponding to 1.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_wb010`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_wb010`'.format(value))

        self._db_wb010 = value

    @property
    def wb020(self):
        """Get wb020.

        Returns:
            float: The value of `wb020` or None if not set

        """
        return self._wb020

    @wb020.setter
    def wb020(self, value=None):
        """  Corresponds to IDD Field `wb020`
        Wet-bulb temperature corresponding to 02.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `wb020`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wb020`'.format(value))

        self._wb020 = value

    @property
    def db_wb020(self):
        """Get db_wb020.

        Returns:
            float: The value of `db_wb020` or None if not set

        """
        return self._db_wb020

    @db_wb020.setter
    def db_wb020(self, value=None):
        """  Corresponds to IDD Field `db_wb020`
        mean coincident dry-bulb temperature to
        Wet-bulb temperature corresponding to 2.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_wb020`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_wb020`'.format(value))

        self._db_wb020 = value

    @property
    def ws_db004(self):
        """Get ws_db004.

        Returns:
            float: The value of `ws_db004` or None if not set

        """
        return self._ws_db004

    @ws_db004.setter
    def ws_db004(self, value=None):
        """  Corresponds to IDD Field `ws_db004`
        Mean wind speed coincident with 0.4% dry-bulb temperature

        Args:
            value (float): value for IDD Field `ws_db004`
                Unit: m/s
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ws_db004`'.format(value))

        self._ws_db004 = value

    @property
    def wd_db004(self):
        """Get wd_db004.

        Returns:
            float: The value of `wd_db004` or None if not set

        """
        return self._wd_db004

    @wd_db004.setter
    def wd_db004(self, value=None):
        """  Corresponds to IDD Field `wd_db004`
        corresponding most frequent wind direction
        Mean wind speed coincident with 0.4% dry-bulb temperature
        degrees true from north (east = 90 deg)

        Args:
            value (float): value for IDD Field `wd_db004`
                Unit: deg
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wd_db004`'.format(value))

        self._wd_db004 = value

    @property
    def dp004(self):
        """Get dp004.

        Returns:
            float: The value of `dp004` or None if not set

        """
        return self._dp004

    @dp004.setter
    def dp004(self, value=None):
        """  Corresponds to IDD Field `dp004`
        Dew-point temperature corresponding to 0.4% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `dp004`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dp004`'.format(value))

        self._dp004 = value

    @property
    def hr_dp004(self):
        """Get hr_dp004.

        Returns:
            float: The value of `hr_dp004` or None if not set

        """
        return self._hr_dp004

    @hr_dp004.setter
    def hr_dp004(self, value=None):
        """  Corresponds to IDD Field `hr_dp004`
        humidity ratio corresponding to
        Dew-point temperature corresponding to 0.4% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `hr_dp004`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hr_dp004`'.format(value))

        self._hr_dp004 = value

    @property
    def db_dp004(self):
        """Get db_dp004.

        Returns:
            float: The value of `db_dp004` or None if not set

        """
        return self._db_dp004

    @db_dp004.setter
    def db_dp004(self, value=None):
        """  Corresponds to IDD Field `db_dp004`
        mean coincident dry-bulb temperature to
        Dew-point temperature corresponding to 0.4% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_dp004`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_dp004`'.format(value))

        self._db_dp004 = value

    @property
    def dp010(self):
        """Get dp010.

        Returns:
            float: The value of `dp010` or None if not set

        """
        return self._dp010

    @dp010.setter
    def dp010(self, value=None):
        """  Corresponds to IDD Field `dp010`
        Dew-point temperature corresponding to 1.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `dp010`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dp010`'.format(value))

        self._dp010 = value

    @property
    def hr_dp010(self):
        """Get hr_dp010.

        Returns:
            float: The value of `hr_dp010` or None if not set

        """
        return self._hr_dp010

    @hr_dp010.setter
    def hr_dp010(self, value=None):
        """  Corresponds to IDD Field `hr_dp010`
        humidity ratio corresponding to
        Dew-point temperature corresponding to 1.0,% annual cumulative frequency of occurrence
        calculated at the standard atmospheric pressure at elevation of station

        Args:
            value (float): value for IDD Field `hr_dp010`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hr_dp010`'.format(value))

        self._hr_dp010 = value

    @property
    def db_dp010(self):
        """Get db_dp010.

        Returns:
            float: The value of `db_dp010` or None if not set

        """
        return self._db_dp010

    @db_dp010.setter
    def db_dp010(self, value=None):
        """  Corresponds to IDD Field `db_dp010`
        mean coincident dry-bulb temperature to
        Dew-point temperature corresponding to 1.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_dp010`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_dp010`'.format(value))

        self._db_dp010 = value

    @property
    def dp020(self):
        """Get dp020.

        Returns:
            float: The value of `dp020` or None if not set

        """
        return self._dp020

    @dp020.setter
    def dp020(self, value=None):
        """  Corresponds to IDD Field `dp020`
        Dew-point temperature corresponding to 2.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `dp020`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dp020`'.format(value))

        self._dp020 = value

    @property
    def hr_dp020(self):
        """Get hr_dp020.

        Returns:
            float: The value of `hr_dp020` or None if not set

        """
        return self._hr_dp020

    @hr_dp020.setter
    def hr_dp020(self, value=None):
        """  Corresponds to IDD Field `hr_dp020`
        humidity ratio corresponding to
        Dew-point temperature corresponding to 2.0% annual cumulative frequency of occurrence
        calculated at the standard atmospheric pressure at elevation of station

        Args:
            value (float): value for IDD Field `hr_dp020`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hr_dp020`'.format(value))

        self._hr_dp020 = value

    @property
    def db_dp020(self):
        """Get db_dp020.

        Returns:
            float: The value of `db_dp020` or None if not set

        """
        return self._db_dp020

    @db_dp020.setter
    def db_dp020(self, value=None):
        """  Corresponds to IDD Field `db_dp020`
        mean coincident dry-bulb temperature to
        Dew-point temperature corresponding to 2.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_dp020`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_dp020`'.format(value))

        self._db_dp020 = value

    @property
    def en004(self):
        """Get en004.

        Returns:
            float: The value of `en004` or None if not set

        """
        return self._en004

    @en004.setter
    def en004(self, value=None):
        """  Corresponds to IDD Field `en004`
        mean coincident dry-bulb temperature to
        Enthalpy corresponding to 0.4% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `en004`
                Unit: kJ/kg
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `en004`'.format(value))

        self._en004 = value

    @property
    def db_en004(self):
        """Get db_en004.

        Returns:
            float: The value of `db_en004` or None if not set

        """
        return self._db_en004

    @db_en004.setter
    def db_en004(self, value=None):
        """  Corresponds to IDD Field `db_en004`
        mean coincident dry-bulb temperature to
        Enthalpy corresponding to 0.4% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_en004`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_en004`'.format(value))

        self._db_en004 = value

    @property
    def en010(self):
        """Get en010.

        Returns:
            float: The value of `en010` or None if not set

        """
        return self._en010

    @en010.setter
    def en010(self, value=None):
        """  Corresponds to IDD Field `en010`
        mean coincident dry-bulb temperature to
        Enthalpy corresponding to 1.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `en010`
                Unit: kJ/kg
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `en010`'.format(value))

        self._en010 = value

    @property
    def db_en010(self):
        """Get db_en010.

        Returns:
            float: The value of `db_en010` or None if not set

        """
        return self._db_en010

    @db_en010.setter
    def db_en010(self, value=None):
        """  Corresponds to IDD Field `db_en010`
        mean coincident dry-bulb temperature to
        Enthalpy corresponding to 1.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_en010`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_en010`'.format(value))

        self._db_en010 = value

    @property
    def en020(self):
        """Get en020.

        Returns:
            float: The value of `en020` or None if not set

        """
        return self._en020

    @en020.setter
    def en020(self, value=None):
        """  Corresponds to IDD Field `en020`
        mean coincident dry-bulb temperature to
        Enthalpy corresponding to 2.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `en020`
                Unit: kJ/kg
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `en020`'.format(value))

        self._en020 = value

    @property
    def db_en020(self):
        """Get db_en020.

        Returns:
            float: The value of `db_en020` or None if not set

        """
        return self._db_en020

    @db_en020.setter
    def db_en020(self, value=None):
        """  Corresponds to IDD Field `db_en020`
        mean coincident dry-bulb temperature to
        Enthalpy corresponding to 2.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `db_en020`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_en020`'.format(value))

        self._db_en020 = value

    @property
    def hrs_84_and_db12_8_or_20_6(self):
        """Get hrs_84_and_db12_8_or_20_6.

        Returns:
            float: The value of `hrs_84_and_db12_8_or_20_6` or None if not set

        """
        return self._hrs_84_and_db12_8_or_20_6

    @hrs_84_and_db12_8_or_20_6.setter
    def hrs_84_and_db12_8_or_20_6(self, value=None):
        """  Corresponds to IDD Field `hrs_84_and_db12_8_or_20_6`
        Number of hours between 8 AM and 4 PM (inclusive) with dry-bulb temperature between 12.8 and 20.6 C

        Args:
            value (float): value for IDD Field `hrs_84_and_db12_8_or_20_6`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `hrs_84_and_db12_8_or_20_6`'.format(value))

        self._hrs_84_and_db12_8_or_20_6 = value

    @property
    def design_stat_extremes(self):
        """Get design_stat_extremes.

        Returns:
            str: The value of `design_stat_extremes` or None if not set

        """
        return self._design_stat_extremes

    @design_stat_extremes.setter
    def design_stat_extremes(self, value="Extremes"):
        """Corresponds to IDD Field `design_stat_extremes`

        Args:
            value (str): value for IDD Field `design_stat_extremes`
                Accepted values are:
                      - Extremes
                Default value: Extremes
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `design_stat_extremes`'.format(value))
            vals = set()
            vals.add("Extremes")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_stat_extremes`'.format(value))

        self._design_stat_extremes = value

    @property
    def ws010(self):
        """Get ws010.

        Returns:
            float: The value of `ws010` or None if not set

        """
        return self._ws010

    @ws010.setter
    def ws010(self, value=None):
        """  Corresponds to IDD Field `ws010`
        Wind speed corresponding to 1.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `ws010`
                Unit: m/s
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ws010`'.format(value))

        self._ws010 = value

    @property
    def ws025(self):
        """Get ws025.

        Returns:
            float: The value of `ws025` or None if not set

        """
        return self._ws025

    @ws025.setter
    def ws025(self, value=None):
        """  Corresponds to IDD Field `ws025`
        Wind speed corresponding to 2.5% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `ws025`
                Unit: m/s
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ws025`'.format(value))

        self._ws025 = value

    @property
    def ws050(self):
        """Get ws050.

        Returns:
            float: The value of `ws050` or None if not set

        """
        return self._ws050

    @ws050.setter
    def ws050(self, value=None):
        """  Corresponds to IDD Field `ws050`
        Wind speed corresponding 5.0% annual cumulative frequency of occurrence

        Args:
            value (float): value for IDD Field `ws050`
                Unit: m/s
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ws050`'.format(value))

        self._ws050 = value

    @property
    def wbmax(self):
        """Get wbmax.

        Returns:
            float: The value of `wbmax` or None if not set

        """
        return self._wbmax

    @wbmax.setter
    def wbmax(self, value=None):
        """  Corresponds to IDD Field `wbmax`
        Extreme maximum wet-bulb temperature

        Args:
            value (float): value for IDD Field `wbmax`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wbmax`'.format(value))

        self._wbmax = value

    @property
    def dbmin_mean(self):
        """Get dbmin_mean.

        Returns:
            float: The value of `dbmin_mean` or None if not set

        """
        return self._dbmin_mean

    @dbmin_mean.setter
    def dbmin_mean(self, value=None):
        """  Corresponds to IDD Field `dbmin_mean`
        Mean of extreme annual minimum dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmin_mean`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmin_mean`'.format(value))

        self._dbmin_mean = value

    @property
    def dbmax_mean(self):
        """Get dbmax_mean.

        Returns:
            float: The value of `dbmax_mean` or None if not set

        """
        return self._dbmax_mean

    @dbmax_mean.setter
    def dbmax_mean(self, value=None):
        """  Corresponds to IDD Field `dbmax_mean`
        Mean of extreme annual maximum dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmax_mean`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmax_mean`'.format(value))

        self._dbmax_mean = value

    @property
    def dbmin_stddev(self):
        """Get dbmin_stddev.

        Returns:
            float: The value of `dbmin_stddev` or None if not set

        """
        return self._dbmin_stddev

    @dbmin_stddev.setter
    def dbmin_stddev(self, value=None):
        """  Corresponds to IDD Field `dbmin_stddev`
        Standard deviation of extreme annual minimum dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmin_stddev`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmin_stddev`'.format(value))

        self._dbmin_stddev = value

    @property
    def dbmax_stddev(self):
        """Get dbmax_stddev.

        Returns:
            float: The value of `dbmax_stddev` or None if not set

        """
        return self._dbmax_stddev

    @dbmax_stddev.setter
    def dbmax_stddev(self, value=None):
        """  Corresponds to IDD Field `dbmax_stddev`
        Standard deviation of extreme annual maximum dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmax_stddev`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmax_stddev`'.format(value))

        self._dbmax_stddev = value

    @property
    def dbmin05years(self):
        """Get dbmin05years.

        Returns:
            float: The value of `dbmin05years` or None if not set

        """
        return self._dbmin05years

    @dbmin05years.setter
    def dbmin05years(self, value=None):
        """  Corresponds to IDD Field `dbmin05years`
        5-year return period values for minimum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmin05years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmin05years`'.format(value))

        self._dbmin05years = value

    @property
    def dbmax05years(self):
        """Get dbmax05years.

        Returns:
            float: The value of `dbmax05years` or None if not set

        """
        return self._dbmax05years

    @dbmax05years.setter
    def dbmax05years(self, value=None):
        """  Corresponds to IDD Field `dbmax05years`
        5-year return period values for maximum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmax05years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmax05years`'.format(value))

        self._dbmax05years = value

    @property
    def dbmin10years(self):
        """Get dbmin10years.

        Returns:
            float: The value of `dbmin10years` or None if not set

        """
        return self._dbmin10years

    @dbmin10years.setter
    def dbmin10years(self, value=None):
        """  Corresponds to IDD Field `dbmin10years`
        10-year return period values for minimum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmin10years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmin10years`'.format(value))

        self._dbmin10years = value

    @property
    def dbmax10years(self):
        """Get dbmax10years.

        Returns:
            float: The value of `dbmax10years` or None if not set

        """
        return self._dbmax10years

    @dbmax10years.setter
    def dbmax10years(self, value=None):
        """  Corresponds to IDD Field `dbmax10years`
        10-year return period values for maximum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmax10years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmax10years`'.format(value))

        self._dbmax10years = value

    @property
    def dbmin20years(self):
        """Get dbmin20years.

        Returns:
            float: The value of `dbmin20years` or None if not set

        """
        return self._dbmin20years

    @dbmin20years.setter
    def dbmin20years(self, value=None):
        """  Corresponds to IDD Field `dbmin20years`
        20-year return period values for minimum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmin20years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmin20years`'.format(value))

        self._dbmin20years = value

    @property
    def dbmax20years(self):
        """Get dbmax20years.

        Returns:
            float: The value of `dbmax20years` or None if not set

        """
        return self._dbmax20years

    @dbmax20years.setter
    def dbmax20years(self, value=None):
        """  Corresponds to IDD Field `dbmax20years`
        20-year return period values for maximum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmax20years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmax20years`'.format(value))

        self._dbmax20years = value

    @property
    def dbmin50years(self):
        """Get dbmin50years.

        Returns:
            float: The value of `dbmin50years` or None if not set

        """
        return self._dbmin50years

    @dbmin50years.setter
    def dbmin50years(self, value=None):
        """  Corresponds to IDD Field `dbmin50years`
        50-year return period values for minimum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmin50years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmin50years`'.format(value))

        self._dbmin50years = value

    @property
    def dbmax50years(self):
        """Get dbmax50years.

        Returns:
            float: The value of `dbmax50years` or None if not set

        """
        return self._dbmax50years

    @dbmax50years.setter
    def dbmax50years(self, value=None):
        """  Corresponds to IDD Field `dbmax50years`
        50-year return period values for maximum extreme dry-bulb temperature

        Args:
            value (float): value for IDD Field `dbmax50years`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dbmax50years`'.format(value))

        self._dbmax50years = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(self._to_str(self.title_of_design_condition))
        out.append(self._to_str(self.unkown_field))
        out.append(self._to_str(self.design_stat_heating))
        out.append(self._to_str(self.coldestmonth))
        out.append(self._to_str(self.db996))
        out.append(self._to_str(self.db990))
        out.append(self._to_str(self.dp996))
        out.append(self._to_str(self.hr_dp996))
        out.append(self._to_str(self.db_dp996))
        out.append(self._to_str(self.dp990))
        out.append(self._to_str(self.hr_dp990))
        out.append(self._to_str(self.db_dp990))
        out.append(self._to_str(self.ws004c))
        out.append(self._to_str(self.db_ws004c))
        out.append(self._to_str(self.ws010c))
        out.append(self._to_str(self.db_ws010c))
        out.append(self._to_str(self.ws_db996))
        out.append(self._to_str(self.wd_db996))
        out.append(self._to_str(self.design_stat_cooling))
        out.append(self._to_str(self.hottestmonth))
        out.append(self._to_str(self.dbr))
        out.append(self._to_str(self.db004))
        out.append(self._to_str(self.wb_db004))
        out.append(self._to_str(self.db010))
        out.append(self._to_str(self.wb_db010))
        out.append(self._to_str(self.db020))
        out.append(self._to_str(self.wb_db020))
        out.append(self._to_str(self.wb004))
        out.append(self._to_str(self.db_wb004))
        out.append(self._to_str(self.wb010))
        out.append(self._to_str(self.db_wb010))
        out.append(self._to_str(self.wb020))
        out.append(self._to_str(self.db_wb020))
        out.append(self._to_str(self.ws_db004))
        out.append(self._to_str(self.wd_db004))
        out.append(self._to_str(self.dp004))
        out.append(self._to_str(self.hr_dp004))
        out.append(self._to_str(self.db_dp004))
        out.append(self._to_str(self.dp010))
        out.append(self._to_str(self.hr_dp010))
        out.append(self._to_str(self.db_dp010))
        out.append(self._to_str(self.dp020))
        out.append(self._to_str(self.hr_dp020))
        out.append(self._to_str(self.db_dp020))
        out.append(self._to_str(self.en004))
        out.append(self._to_str(self.db_en004))
        out.append(self._to_str(self.en010))
        out.append(self._to_str(self.db_en010))
        out.append(self._to_str(self.en020))
        out.append(self._to_str(self.db_en020))
        out.append(self._to_str(self.hrs_84_and_db12_8_or_20_6))
        out.append(self._to_str(self.design_stat_extremes))
        out.append(self._to_str(self.ws010))
        out.append(self._to_str(self.ws025))
        out.append(self._to_str(self.ws050))
        out.append(self._to_str(self.wbmax))
        out.append(self._to_str(self.dbmin_mean))
        out.append(self._to_str(self.dbmax_mean))
        out.append(self._to_str(self.dbmin_stddev))
        out.append(self._to_str(self.dbmax_stddev))
        out.append(self._to_str(self.dbmin05years))
        out.append(self._to_str(self.dbmax05years))
        out.append(self._to_str(self.dbmin10years))
        out.append(self._to_str(self.dbmax10years))
        out.append(self._to_str(self.dbmin20years))
        out.append(self._to_str(self.dbmax20years))
        out.append(self._to_str(self.dbmin50years))
        out.append(self._to_str(self.dbmax50years))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class DesignConditions(object):

    """Corresponds to EPW IDD object `DESIGN CONDITIONS`"""
    _internal_name = "DESIGN CONDITIONS"
    _field_count = 1

    def __init__(self):
        self._design_conditions = []

    def read(self, vals):
        i = 0
        count = int(vals[i])
        i += 1
        for _ in range(count):
            obj = DesignCondition()
            obj.read(vals[i:i + obj._field_count])
            self.add_design_condition(obj)
            i += obj._field_count

    @property
    def design_conditions(self):
        """Get design_conditions.

        Returns:
            A list of DesignCondition objects

        """
        return self._design_conditions

    def add_design_condition(self, value):
        """Add design_condition.

        Args:
            DesignCondition: New value to add to `design_conditions`

        """
        self._design_conditions.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        out.append(str(len(self.design_conditions)))
        for obj in self.design_conditions:
            out.append(obj.export(top=False))
        return ",".join(out)

    def __str__(self):
        return self.export(True)


class TypicalOrExtremePeriod(object):

    """Corresponds to EPW IDD object `TYPICAL/EXTREME PERIOD`"""
    _internal_name = "TYPICAL/EXTREME PERIOD"
    _field_count = 4

    def __init__(self):
        self._typical_or_extreme_period_name = None
        self._typical_or_extreme_period_type = None
        self._period_start_day = None
        self._period_end_day = None

    def read(self, vals):
        i = 0
        if len(vals[i]) == 0:
            self.typical_or_extreme_period_name = None
        else:
            self.typical_or_extreme_period_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.typical_or_extreme_period_type = None
        else:
            self.typical_or_extreme_period_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.period_start_day = None
        else:
            self.period_start_day = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.period_end_day = None
        else:
            self.period_end_day = vals[i]
        i += 1

    @property
    def typical_or_extreme_period_name(self):
        """Get typical_or_extreme_period_name.

        Returns:
            str: The value of `typical_or_extreme_period_name` or None if not set

        """
        return self._typical_or_extreme_period_name

    @typical_or_extreme_period_name.setter
    def typical_or_extreme_period_name(self, value=None):
        """Corresponds to IDD Field `typical_or_extreme_period_name`

        Args:
            value (str): value for IDD Field `typical_or_extreme_period_name`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `typical_or_extreme_period_name`'.format(value))

        self._typical_or_extreme_period_name = value

    @property
    def typical_or_extreme_period_type(self):
        """Get typical_or_extreme_period_type.

        Returns:
            str: The value of `typical_or_extreme_period_type` or None if not set

        """
        return self._typical_or_extreme_period_type

    @typical_or_extreme_period_type.setter
    def typical_or_extreme_period_type(self, value=None):
        """Corresponds to IDD Field `typical_or_extreme_period_type`

        Args:
            value (str): value for IDD Field `typical_or_extreme_period_type`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `typical_or_extreme_period_type`'.format(value))

        self._typical_or_extreme_period_type = value

    @property
    def period_start_day(self):
        """Get period_start_day.

        Returns:
            str: The value of `period_start_day` or None if not set

        """
        return self._period_start_day

    @period_start_day.setter
    def period_start_day(self, value=None):
        """Corresponds to IDD Field `period_start_day`

        Args:
            value (str): value for IDD Field `period_start_day`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `period_start_day`'.format(value))

        self._period_start_day = value

    @property
    def period_end_day(self):
        """Get period_end_day.

        Returns:
            str: The value of `period_end_day` or None if not set

        """
        return self._period_end_day

    @period_end_day.setter
    def period_end_day(self, value=None):
        """Corresponds to IDD Field `period_end_day`

        Args:
            value (str): value for IDD Field `period_end_day`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `period_end_day`'.format(value))

        self._period_end_day = value

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
        out.append(self._to_str(self.typical_or_extreme_period_type))
        out.append(self._to_str(self.period_start_day))
        out.append(self._to_str(self.period_end_day))
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
        """Get typical_or_extreme_periods.

        Returns:
            A list of TypicalOrExtremePeriod objects

        """
        return self._typical_or_extreme_periods

    def add_typical_or_extreme_period(self, value):
        """Add typical_or_extreme_period.

        Args:
            TypicalOrExtremePeriod: New value to add to `typical_or_extreme_periods`

        """
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
            self.ground_temperature_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_soil_conductivity = None
        else:
            self.depth_soil_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_soil_density = None
        else:
            self.depth_soil_density = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_soil_specific_heat = None
        else:
            self.depth_soil_specific_heat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_january_average_ground_temperature = None
        else:
            self.depth_january_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_february_average_ground_temperature = None
        else:
            self.depth_february_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_march_average_ground_temperature = None
        else:
            self.depth_march_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_april_average_ground_temperature = None
        else:
            self.depth_april_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_may_average_ground_temperature = None
        else:
            self.depth_may_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_june_average_ground_temperature = None
        else:
            self.depth_june_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_july_average_ground_temperature = None
        else:
            self.depth_july_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_august_average_ground_temperature = None
        else:
            self.depth_august_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_september_average_ground_temperature = None
        else:
            self.depth_september_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_october_average_ground_temperature = None
        else:
            self.depth_october_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_november_average_ground_temperature = None
        else:
            self.depth_november_average_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_december_average_ground_temperature = None
        else:
            self.depth_december_average_ground_temperature = vals[i]
        i += 1

    @property
    def ground_temperature_depth(self):
        """Get ground_temperature_depth.

        Returns:
            float: The value of `ground_temperature_depth` or None if not set

        """
        return self._ground_temperature_depth

    @ground_temperature_depth.setter
    def ground_temperature_depth(self, value=None):
        """Corresponds to IDD Field `ground_temperature_depth`

        Args:
            value (float): value for IDD Field `ground_temperature_depth`
                Unit: m
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `ground_temperature_depth`'.format(value))

        self._ground_temperature_depth = value

    @property
    def depth_soil_conductivity(self):
        """Get depth_soil_conductivity.

        Returns:
            float: The value of `depth_soil_conductivity` or None if not set

        """
        return self._depth_soil_conductivity

    @depth_soil_conductivity.setter
    def depth_soil_conductivity(self, value=None):
        """Corresponds to IDD Field `depth_soil_conductivity`

        Args:
            value (float): value for IDD Field `depth_soil_conductivity`
                Unit: W/m-K,
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_soil_conductivity`'.format(value))

        self._depth_soil_conductivity = value

    @property
    def depth_soil_density(self):
        """Get depth_soil_density.

        Returns:
            float: The value of `depth_soil_density` or None if not set

        """
        return self._depth_soil_density

    @depth_soil_density.setter
    def depth_soil_density(self, value=None):
        """Corresponds to IDD Field `depth_soil_density`

        Args:
            value (float): value for IDD Field `depth_soil_density`
                Unit: kg/m3
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_soil_density`'.format(value))

        self._depth_soil_density = value

    @property
    def depth_soil_specific_heat(self):
        """Get depth_soil_specific_heat.

        Returns:
            float: The value of `depth_soil_specific_heat` or None if not set

        """
        return self._depth_soil_specific_heat

    @depth_soil_specific_heat.setter
    def depth_soil_specific_heat(self, value=None):
        """Corresponds to IDD Field `depth_soil_specific_heat`

        Args:
            value (float): value for IDD Field `depth_soil_specific_heat`
                Unit: J/kg-K,
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_soil_specific_heat`'.format(value))

        self._depth_soil_specific_heat = value

    @property
    def depth_january_average_ground_temperature(self):
        """Get depth_january_average_ground_temperature.

        Returns:
            float: The value of `depth_january_average_ground_temperature` or None if not set

        """
        return self._depth_january_average_ground_temperature

    @depth_january_average_ground_temperature.setter
    def depth_january_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_january_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_january_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_january_average_ground_temperature`'.format(value))

        self._depth_january_average_ground_temperature = value

    @property
    def depth_february_average_ground_temperature(self):
        """Get depth_february_average_ground_temperature.

        Returns:
            float: The value of `depth_february_average_ground_temperature` or None if not set

        """
        return self._depth_february_average_ground_temperature

    @depth_february_average_ground_temperature.setter
    def depth_february_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_february_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_february_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_february_average_ground_temperature`'.format(value))

        self._depth_february_average_ground_temperature = value

    @property
    def depth_march_average_ground_temperature(self):
        """Get depth_march_average_ground_temperature.

        Returns:
            float: The value of `depth_march_average_ground_temperature` or None if not set

        """
        return self._depth_march_average_ground_temperature

    @depth_march_average_ground_temperature.setter
    def depth_march_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_march_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_march_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_march_average_ground_temperature`'.format(value))

        self._depth_march_average_ground_temperature = value

    @property
    def depth_april_average_ground_temperature(self):
        """Get depth_april_average_ground_temperature.

        Returns:
            float: The value of `depth_april_average_ground_temperature` or None if not set

        """
        return self._depth_april_average_ground_temperature

    @depth_april_average_ground_temperature.setter
    def depth_april_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_april_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_april_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_april_average_ground_temperature`'.format(value))

        self._depth_april_average_ground_temperature = value

    @property
    def depth_may_average_ground_temperature(self):
        """Get depth_may_average_ground_temperature.

        Returns:
            float: The value of `depth_may_average_ground_temperature` or None if not set

        """
        return self._depth_may_average_ground_temperature

    @depth_may_average_ground_temperature.setter
    def depth_may_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_may_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_may_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_may_average_ground_temperature`'.format(value))

        self._depth_may_average_ground_temperature = value

    @property
    def depth_june_average_ground_temperature(self):
        """Get depth_june_average_ground_temperature.

        Returns:
            float: The value of `depth_june_average_ground_temperature` or None if not set

        """
        return self._depth_june_average_ground_temperature

    @depth_june_average_ground_temperature.setter
    def depth_june_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_june_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_june_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_june_average_ground_temperature`'.format(value))

        self._depth_june_average_ground_temperature = value

    @property
    def depth_july_average_ground_temperature(self):
        """Get depth_july_average_ground_temperature.

        Returns:
            float: The value of `depth_july_average_ground_temperature` or None if not set

        """
        return self._depth_july_average_ground_temperature

    @depth_july_average_ground_temperature.setter
    def depth_july_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_july_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_july_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_july_average_ground_temperature`'.format(value))

        self._depth_july_average_ground_temperature = value

    @property
    def depth_august_average_ground_temperature(self):
        """Get depth_august_average_ground_temperature.

        Returns:
            float: The value of `depth_august_average_ground_temperature` or None if not set

        """
        return self._depth_august_average_ground_temperature

    @depth_august_average_ground_temperature.setter
    def depth_august_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_august_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_august_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_august_average_ground_temperature`'.format(value))

        self._depth_august_average_ground_temperature = value

    @property
    def depth_september_average_ground_temperature(self):
        """Get depth_september_average_ground_temperature.

        Returns:
            float: The value of `depth_september_average_ground_temperature` or None if not set

        """
        return self._depth_september_average_ground_temperature

    @depth_september_average_ground_temperature.setter
    def depth_september_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field
        `depth_september_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_september_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_september_average_ground_temperature`'.format(value))

        self._depth_september_average_ground_temperature = value

    @property
    def depth_october_average_ground_temperature(self):
        """Get depth_october_average_ground_temperature.

        Returns:
            float: The value of `depth_october_average_ground_temperature` or None if not set

        """
        return self._depth_october_average_ground_temperature

    @depth_october_average_ground_temperature.setter
    def depth_october_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_october_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_october_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_october_average_ground_temperature`'.format(value))

        self._depth_october_average_ground_temperature = value

    @property
    def depth_november_average_ground_temperature(self):
        """Get depth_november_average_ground_temperature.

        Returns:
            float: The value of `depth_november_average_ground_temperature` or None if not set

        """
        return self._depth_november_average_ground_temperature

    @depth_november_average_ground_temperature.setter
    def depth_november_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_november_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_november_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_november_average_ground_temperature`'.format(value))

        self._depth_november_average_ground_temperature = value

    @property
    def depth_december_average_ground_temperature(self):
        """Get depth_december_average_ground_temperature.

        Returns:
            float: The value of `depth_december_average_ground_temperature` or None if not set

        """
        return self._depth_december_average_ground_temperature

    @depth_december_average_ground_temperature.setter
    def depth_december_average_ground_temperature(self, value=None):
        """Corresponds to IDD Field `depth_december_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_december_average_ground_temperature`
                Unit: C
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `depth_december_average_ground_temperature`'.format(value))

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
        """Get ground_temperatures.

        Returns:
            A list of GroundTemperature objects

        """
        return self._ground_temperatures

    def add_ground_temperature(self, value):
        """Add ground_temperature.

        Args:
            GroundTemperature: New value to add to `ground_temperatures`

        """
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
            self.holiday_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.holiday_day = None
        else:
            self.holiday_day = vals[i]
        i += 1

    @property
    def holiday_name(self):
        """Get holiday_name.

        Returns:
            str: The value of `holiday_name` or None if not set

        """
        return self._holiday_name

    @holiday_name.setter
    def holiday_name(self, value=None):
        """Corresponds to IDD Field `holiday_name`

        Args:
            value (str): value for IDD Field `holiday_name`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `holiday_name`'.format(value))

        self._holiday_name = value

    @property
    def holiday_day(self):
        """Get holiday_day.

        Returns:
            str: The value of `holiday_day` or None if not set

        """
        return self._holiday_day

    @holiday_day.setter
    def holiday_day(self, value=None):
        """Corresponds to IDD Field `holiday_day`

        Args:
            value (str): value for IDD Field `holiday_day`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `holiday_day`'.format(value))

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
            self.leapyear_observed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daylight_saving_start_day = None
        else:
            self.daylight_saving_start_day = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daylight_saving_end_day = None
        else:
            self.daylight_saving_end_day = vals[i]
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
        """Get leapyear_observed.

        Returns:
            str: The value of `leapyear_observed` or None if not set

        """
        return self._leapyear_observed

    @leapyear_observed.setter
    def leapyear_observed(self, value=None):
        """Corresponds to IDD Field `leapyear_observed` Yes if Leap Year will
        be observed for this file No if Leap Year days (29 Feb) should be
        ignored in this file.

        Args:
            value (str): value for IDD Field `leapyear_observed`
                Accepted values are:
                      - Yes
                      - No
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `leapyear_observed`'.format(value))
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `leapyear_observed`'.format(value))

        self._leapyear_observed = value

    @property
    def daylight_saving_start_day(self):
        """Get daylight_saving_start_day.

        Returns:
            str: The value of `daylight_saving_start_day` or None if not set

        """
        return self._daylight_saving_start_day

    @daylight_saving_start_day.setter
    def daylight_saving_start_day(self, value=None):
        """Corresponds to IDD Field `daylight_saving_start_day`

        Args:
            value (str): value for IDD Field `daylight_saving_start_day`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `daylight_saving_start_day`'.format(value))

        self._daylight_saving_start_day = value

    @property
    def daylight_saving_end_day(self):
        """Get daylight_saving_end_day.

        Returns:
            str: The value of `daylight_saving_end_day` or None if not set

        """
        return self._daylight_saving_end_day

    @daylight_saving_end_day.setter
    def daylight_saving_end_day(self, value=None):
        """Corresponds to IDD Field `daylight_saving_end_day`

        Args:
            value (str): value for IDD Field `daylight_saving_end_day`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `daylight_saving_end_day`'.format(value))

        self._daylight_saving_end_day = value

    @property
    def holidays(self):
        """Get holidays.

        Returns:
            A list of Holiday objects

        """
        return self._holidays

    def add_holiday(self, value):
        """Add holiday.

        Args:
            Holiday: New value to add to `holidays`

        """
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
            self.comments_1 = vals[i]
        i += 1

    @property
    def comments_1(self):
        """Get comments_1.

        Returns:
            str: The value of `comments_1` or None if not set

        """
        return self._comments_1

    @comments_1.setter
    def comments_1(self, value=None):
        """Corresponds to IDD Field `comments_1`

        Args:
            value (str): value for IDD Field `comments_1`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `comments_1`'.format(value))

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
            self.comments_2 = vals[i]
        i += 1

    @property
    def comments_2(self):
        """Get comments_2.

        Returns:
            str: The value of `comments_2` or None if not set

        """
        return self._comments_2

    @comments_2.setter
    def comments_2(self, value=None):
        """Corresponds to IDD Field `comments_2`

        Args:
            value (str): value for IDD Field `comments_2`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `comments_2`'.format(value))

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
            self.number_of_records_per_hour = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.data_period_name_or_description = None
        else:
            self.data_period_name_or_description = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.data_period_start_day_of_week = None
        else:
            self.data_period_start_day_of_week = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.data_period_start_day = None
        else:
            self.data_period_start_day = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.data_period_end_day = None
        else:
            self.data_period_end_day = vals[i]
        i += 1

    @property
    def number_of_records_per_hour(self):
        """Get number_of_records_per_hour.

        Returns:
            int: The value of `number_of_records_per_hour` or None if not set

        """
        return self._number_of_records_per_hour

    @number_of_records_per_hour.setter
    def number_of_records_per_hour(self, value=None):
        """Corresponds to IDD Field `number_of_records_per_hour`

        Args:
            value (int): value for IDD Field `number_of_records_per_hour`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError(
                    'value {} need to be of type int '
                    'for field `number_of_records_per_hour`'.format(value))

        self._number_of_records_per_hour = value

    @property
    def data_period_name_or_description(self):
        """Get data_period_name_or_description.

        Returns:
            str: The value of `data_period_name_or_description` or None if not set

        """
        return self._data_period_name_or_description

    @data_period_name_or_description.setter
    def data_period_name_or_description(self, value=None):
        """Corresponds to IDD Field `data_period_name_or_description`

        Args:
            value (str): value for IDD Field `data_period_name_or_description`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `data_period_name_or_description`'.format(value))

        self._data_period_name_or_description = value

    @property
    def data_period_start_day_of_week(self):
        """Get data_period_start_day_of_week.

        Returns:
            str: The value of `data_period_start_day_of_week` or None if not set

        """
        return self._data_period_start_day_of_week

    @data_period_start_day_of_week.setter
    def data_period_start_day_of_week(self, value=None):
        """Corresponds to IDD Field `data_period_start_day_of_week`

        Args:
            value (str): value for IDD Field `data_period_start_day_of_week`
                Accepted values are:
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `data_period_start_day_of_week`'.format(value))
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
                    'value {} is not an accepted value for '
                    'field `data_period_start_day_of_week`'.format(value))

        self._data_period_start_day_of_week = value

    @property
    def data_period_start_day(self):
        """Get data_period_start_day.

        Returns:
            str: The value of `data_period_start_day` or None if not set

        """
        return self._data_period_start_day

    @data_period_start_day.setter
    def data_period_start_day(self, value=None):
        """Corresponds to IDD Field `data_period_start_day`

        Args:
            value (str): value for IDD Field `data_period_start_day`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `data_period_start_day`'.format(value))

        self._data_period_start_day = value

    @property
    def data_period_end_day(self):
        """Get data_period_end_day.

        Returns:
            str: The value of `data_period_end_day` or None if not set

        """
        return self._data_period_end_day

    @data_period_end_day.setter
    def data_period_end_day(self, value=None):
        """Corresponds to IDD Field `data_period_end_day`

        Args:
            value (str): value for IDD Field `data_period_end_day`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `data_period_end_day`'.format(value))

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
        """Get data_periods.

        Returns:
            A list of DataPeriod objects

        """
        return self._data_periods

    def add_data_period(self, value):
        """Add data_period.

        Args:
            DataPeriod: New value to add to `data_periods`

        """
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
        self._opaque_sky_cover = None
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
            self.year = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.month = None
        else:
            self.month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day = None
        else:
            self.day = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hour = None
        else:
            self.hour = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minute = None
        else:
            self.minute = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.data_source_and_uncertainty_flags = None
        else:
            self.data_source_and_uncertainty_flags = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dry_bulb_temperature = None
        else:
            self.dry_bulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dew_point_temperature = None
        else:
            self.dew_point_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity = None
        else:
            self.relative_humidity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.atmospheric_station_pressure = None
        else:
            self.atmospheric_station_pressure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.extraterrestrial_horizontal_radiation = None
        else:
            self.extraterrestrial_horizontal_radiation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.extraterrestrial_direct_normal_radiation = None
        else:
            self.extraterrestrial_direct_normal_radiation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.horizontal_infrared_radiation_intensity = None
        else:
            self.horizontal_infrared_radiation_intensity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.global_horizontal_radiation = None
        else:
            self.global_horizontal_radiation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.direct_normal_radiation = None
        else:
            self.direct_normal_radiation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_horizontal_radiation = None
        else:
            self.diffuse_horizontal_radiation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.global_horizontal_illuminance = None
        else:
            self.global_horizontal_illuminance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.direct_normal_illuminance = None
        else:
            self.direct_normal_illuminance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_horizontal_illuminance = None
        else:
            self.diffuse_horizontal_illuminance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zenith_luminance = None
        else:
            self.zenith_luminance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction = None
        else:
            self.wind_direction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed = None
        else:
            self.wind_speed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_sky_cover = None
        else:
            self.total_sky_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opaque_sky_cover = None
        else:
            self.opaque_sky_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visibility = None
        else:
            self.visibility = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ceiling_height = None
        else:
            self.ceiling_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.present_weather_observation = None
        else:
            self.present_weather_observation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.present_weather_codes = None
        else:
            self.present_weather_codes = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.precipitable_water = None
        else:
            self.precipitable_water = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.aerosol_optical_depth = None
        else:
            self.aerosol_optical_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.snow_depth = None
        else:
            self.snow_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.days_since_last_snowfall = None
        else:
            self.days_since_last_snowfall = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.albedo = None
        else:
            self.albedo = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_precipitation_depth = None
        else:
            self.liquid_precipitation_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_precipitation_quantity = None
        else:
            self.liquid_precipitation_quantity = vals[i]
        i += 1

    @property
    def year(self):
        """Get year.

        Returns:
            int: The value of `year` or None if not set

        """
        return self._year

    @year.setter
    def year(self, value=None):
        """Corresponds to IDD Field `year`

        Args:
            value (int): value for IDD Field `year`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `year`'.format(value))

        self._year = value

    @property
    def month(self):
        """Get month.

        Returns:
            int: The value of `month` or None if not set

        """
        return self._month

    @month.setter
    def month(self, value=None):
        """Corresponds to IDD Field `month`

        Args:
            value (int): value for IDD Field `month`
                value >= 1
                value <= 12
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `month`')

        self._month = value

    @property
    def day(self):
        """Get day.

        Returns:
            int: The value of `day` or None if not set

        """
        return self._day

    @day.setter
    def day(self, value=None):
        """Corresponds to IDD Field `day`

        Args:
            value (int): value for IDD Field `day`
                value >= 1
                value <= 31
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `day`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `day`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `day`')

        self._day = value

    @property
    def hour(self):
        """Get hour.

        Returns:
            int: The value of `hour` or None if not set

        """
        return self._hour

    @hour.setter
    def hour(self, value=None):
        """Corresponds to IDD Field `hour`

        Args:
            value (int): value for IDD Field `hour`
                value >= 1
                value <= 24
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `hour`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `hour`')
            if value > 24:
                raise ValueError('value need to be smaller 24 '
                                 'for field `hour`')

        self._hour = value

    @property
    def minute(self):
        """Get minute.

        Returns:
            int: The value of `minute` or None if not set

        """
        return self._minute

    @minute.setter
    def minute(self, value=None):
        """Corresponds to IDD Field `minute`

        Args:
            value (int): value for IDD Field `minute`
                value >= 0
                value <= 60
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `minute`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `minute`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `minute`')

        self._minute = value

    @property
    def data_source_and_uncertainty_flags(self):
        """Get data_source_and_uncertainty_flags.

        Returns:
            str: The value of `data_source_and_uncertainty_flags` or None if not set

        """
        return self._data_source_and_uncertainty_flags

    @data_source_and_uncertainty_flags.setter
    def data_source_and_uncertainty_flags(self, value=None):
        """Corresponds to IDD Field `data_source_and_uncertainty_flags` Initial
        day of weather file is checked by EnergyPlus for validity (as shown
        below) Each field is checked for "missing" as shown below. Reasonable
        values, calculated values or the last "good" value is substituted.

        Args:
            value (str): value for IDD Field `data_source_and_uncertainty_flags`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError(
                    'value {} need to be of type str '
                    'for field `data_source_and_uncertainty_flags`'.format(value))

        self._data_source_and_uncertainty_flags = value

    @property
    def dry_bulb_temperature(self):
        """Get dry_bulb_temperature.

        Returns:
            float: The value of `dry_bulb_temperature` or None if not set

        """
        return self._dry_bulb_temperature

    @dry_bulb_temperature.setter
    def dry_bulb_temperature(self, value=99.9):
        """Corresponds to IDD Field `dry_bulb_temperature`

        Args:
            value (float): value for IDD Field `dry_bulb_temperature`
                Unit: C
                value > -70.0
                value < 70.0
                Missing value: 99.9
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `dry_bulb_temperature`'.format(value))
            if value <= -70.0:
                raise ValueError('value need to be greater -70.0 '
                                 'for field `dry_bulb_temperature`')
            if value >= 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dry_bulb_temperature`')

        self._dry_bulb_temperature = value

    @property
    def dew_point_temperature(self):
        """Get dew_point_temperature.

        Returns:
            float: The value of `dew_point_temperature` or None if not set

        """
        return self._dew_point_temperature

    @dew_point_temperature.setter
    def dew_point_temperature(self, value=99.9):
        """Corresponds to IDD Field `dew_point_temperature`

        Args:
            value (float): value for IDD Field `dew_point_temperature`
                Unit: C
                value > -70.0
                value < 70.0
                Missing value: 99.9
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `dew_point_temperature`'.format(value))
            if value <= -70.0:
                raise ValueError('value need to be greater -70.0 '
                                 'for field `dew_point_temperature`')
            if value >= 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dew_point_temperature`')

        self._dew_point_temperature = value

    @property
    def relative_humidity(self):
        """Get relative_humidity.

        Returns:
            int: The value of `relative_humidity` or None if not set

        """
        return self._relative_humidity

    @relative_humidity.setter
    def relative_humidity(self, value=999):
        """Corresponds to IDD Field `relative_humidity`

        Args:
            value (int): value for IDD Field `relative_humidity`
                value >= 0
                value <= 110
                Missing value: 999
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `relative_humidity`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `relative_humidity`')
            if value > 110:
                raise ValueError('value need to be smaller 110 '
                                 'for field `relative_humidity`')

        self._relative_humidity = value

    @property
    def atmospheric_station_pressure(self):
        """Get atmospheric_station_pressure.

        Returns:
            int: The value of `atmospheric_station_pressure` or None if not set

        """
        return self._atmospheric_station_pressure

    @atmospheric_station_pressure.setter
    def atmospheric_station_pressure(self, value=999999):
        """Corresponds to IDD Field `atmospheric_station_pressure`

        Args:
            value (int): value for IDD Field `atmospheric_station_pressure`
                Unit: Pa
                value > 31000
                value < 120000
                Missing value: 999999
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError(
                    'value {} need to be of type int '
                    'for field `atmospheric_station_pressure`'.format(value))
            if value <= 31000:
                raise ValueError('value need to be greater 31000 '
                                 'for field `atmospheric_station_pressure`')
            if value >= 120000:
                raise ValueError('value need to be smaller 120000 '
                                 'for field `atmospheric_station_pressure`')

        self._atmospheric_station_pressure = value

    @property
    def extraterrestrial_horizontal_radiation(self):
        """Get extraterrestrial_horizontal_radiation.

        Returns:
            float: The value of `extraterrestrial_horizontal_radiation` or None if not set

        """
        return self._extraterrestrial_horizontal_radiation

    @extraterrestrial_horizontal_radiation.setter
    def extraterrestrial_horizontal_radiation(self, value=9999.0):
        """Corresponds to IDD Field `extraterrestrial_horizontal_radiation`

        Args:
            value (float): value for IDD Field `extraterrestrial_horizontal_radiation`
                Unit: Wh/m2
                value >= 0.0
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `extraterrestrial_horizontal_radiation`'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 '
                    'for field `extraterrestrial_horizontal_radiation`')

        self._extraterrestrial_horizontal_radiation = value

    @property
    def extraterrestrial_direct_normal_radiation(self):
        """Get extraterrestrial_direct_normal_radiation.

        Returns:
            float: The value of `extraterrestrial_direct_normal_radiation` or None if not set

        """
        return self._extraterrestrial_direct_normal_radiation

    @extraterrestrial_direct_normal_radiation.setter
    def extraterrestrial_direct_normal_radiation(self, value=9999.0):
        """Corresponds to IDD Field `extraterrestrial_direct_normal_radiation`

        Args:
            value (float): value for IDD Field `extraterrestrial_direct_normal_radiation`
                Unit: Wh/m2
                value >= 0.0
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `extraterrestrial_direct_normal_radiation`'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 '
                    'for field `extraterrestrial_direct_normal_radiation`')

        self._extraterrestrial_direct_normal_radiation = value

    @property
    def horizontal_infrared_radiation_intensity(self):
        """Get horizontal_infrared_radiation_intensity.

        Returns:
            float: The value of `horizontal_infrared_radiation_intensity` or None if not set

        """
        return self._horizontal_infrared_radiation_intensity

    @horizontal_infrared_radiation_intensity.setter
    def horizontal_infrared_radiation_intensity(self, value=9999.0):
        """Corresponds to IDD Field `horizontal_infrared_radiation_intensity`

        Args:
            value (float): value for IDD Field `horizontal_infrared_radiation_intensity`
                Unit: Wh/m2
                value >= 0.0
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `horizontal_infrared_radiation_intensity`'.format(value))
            if value < 0.0:
                raise ValueError(
                    'value need to be greater or equal 0.0 '
                    'for field `horizontal_infrared_radiation_intensity`')

        self._horizontal_infrared_radiation_intensity = value

    @property
    def global_horizontal_radiation(self):
        """Get global_horizontal_radiation.

        Returns:
            float: The value of `global_horizontal_radiation` or None if not set

        """
        return self._global_horizontal_radiation

    @global_horizontal_radiation.setter
    def global_horizontal_radiation(self, value=9999.0):
        """Corresponds to IDD Field `global_horizontal_radiation`

        Args:
            value (float): value for IDD Field `global_horizontal_radiation`
                Unit: Wh/m2
                value >= 0.0
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `global_horizontal_radiation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `global_horizontal_radiation`')

        self._global_horizontal_radiation = value

    @property
    def direct_normal_radiation(self):
        """Get direct_normal_radiation.

        Returns:
            float: The value of `direct_normal_radiation` or None if not set

        """
        return self._direct_normal_radiation

    @direct_normal_radiation.setter
    def direct_normal_radiation(self, value=9999.0):
        """Corresponds to IDD Field `direct_normal_radiation`

        Args:
            value (float): value for IDD Field `direct_normal_radiation`
                Unit: Wh/m2
                value >= 0.0
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `direct_normal_radiation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `direct_normal_radiation`')

        self._direct_normal_radiation = value

    @property
    def diffuse_horizontal_radiation(self):
        """Get diffuse_horizontal_radiation.

        Returns:
            float: The value of `diffuse_horizontal_radiation` or None if not set

        """
        return self._diffuse_horizontal_radiation

    @diffuse_horizontal_radiation.setter
    def diffuse_horizontal_radiation(self, value=9999.0):
        """Corresponds to IDD Field `diffuse_horizontal_radiation`

        Args:
            value (float): value for IDD Field `diffuse_horizontal_radiation`
                Unit: Wh/m2
                value >= 0.0
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `diffuse_horizontal_radiation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuse_horizontal_radiation`')

        self._diffuse_horizontal_radiation = value

    @property
    def global_horizontal_illuminance(self):
        """Get global_horizontal_illuminance.

        Returns:
            float: The value of `global_horizontal_illuminance` or None if not set

        """
        return self._global_horizontal_illuminance

    @global_horizontal_illuminance.setter
    def global_horizontal_illuminance(self, value=999999.0):
        """  Corresponds to IDD Field `global_horizontal_illuminance`
        will be missing if >= 999900

        Args:
            value (float): value for IDD Field `global_horizontal_illuminance`
                Unit: lux
                value >= 0.0
                Missing value: 999999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `global_horizontal_illuminance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `global_horizontal_illuminance`')

        self._global_horizontal_illuminance = value

    @property
    def direct_normal_illuminance(self):
        """Get direct_normal_illuminance.

        Returns:
            float: The value of `direct_normal_illuminance` or None if not set

        """
        return self._direct_normal_illuminance

    @direct_normal_illuminance.setter
    def direct_normal_illuminance(self, value=999999.0):
        """  Corresponds to IDD Field `direct_normal_illuminance`
        will be missing if >= 999900

        Args:
            value (float): value for IDD Field `direct_normal_illuminance`
                Unit: lux
                value >= 0.0
                Missing value: 999999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `direct_normal_illuminance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `direct_normal_illuminance`')

        self._direct_normal_illuminance = value

    @property
    def diffuse_horizontal_illuminance(self):
        """Get diffuse_horizontal_illuminance.

        Returns:
            float: The value of `diffuse_horizontal_illuminance` or None if not set

        """
        return self._diffuse_horizontal_illuminance

    @diffuse_horizontal_illuminance.setter
    def diffuse_horizontal_illuminance(self, value=999999.0):
        """  Corresponds to IDD Field `diffuse_horizontal_illuminance`
        will be missing if >= 999900

        Args:
            value (float): value for IDD Field `diffuse_horizontal_illuminance`
                Unit: lux
                value >= 0.0
                Missing value: 999999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `diffuse_horizontal_illuminance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuse_horizontal_illuminance`')

        self._diffuse_horizontal_illuminance = value

    @property
    def zenith_luminance(self):
        """Get zenith_luminance.

        Returns:
            float: The value of `zenith_luminance` or None if not set

        """
        return self._zenith_luminance

    @zenith_luminance.setter
    def zenith_luminance(self, value=9999.0):
        """  Corresponds to IDD Field `zenith_luminance`
        will be missing if >= 9999

        Args:
            value (float): value for IDD Field `zenith_luminance`
                Unit: Cd/m2
                value >= 0.0
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zenith_luminance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zenith_luminance`')

        self._zenith_luminance = value

    @property
    def wind_direction(self):
        """Get wind_direction.

        Returns:
            float: The value of `wind_direction` or None if not set

        """
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value=999.0):
        """Corresponds to IDD Field `wind_direction`

        Args:
            value (float): value for IDD Field `wind_direction`
                Unit: degrees
                value >= 0.0
                value <= 360.0
                Missing value: 999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wind_direction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction`')

        self._wind_direction = value

    @property
    def wind_speed(self):
        """Get wind_speed.

        Returns:
            float: The value of `wind_speed` or None if not set

        """
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value=999.0):
        """Corresponds to IDD Field `wind_speed`

        Args:
            value (float): value for IDD Field `wind_speed`
                Unit: m/s
                value >= 0.0
                value <= 40.0
                Missing value: 999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wind_speed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_speed`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `wind_speed`')

        self._wind_speed = value

    @property
    def total_sky_cover(self):
        """Get total_sky_cover.

        Returns:
            float: The value of `total_sky_cover` or None if not set

        """
        return self._total_sky_cover

    @total_sky_cover.setter
    def total_sky_cover(self, value=99.0):
        """Corresponds to IDD Field `total_sky_cover` This is the value for
        total sky cover (tenths of coverage). (i.e. 1 is 1/10 covered. 10 is
        total coverage). (Amount of sky dome in tenths covered by clouds or
        obscuring phenomena at the  hour indicated at the time indicated.)

        Args:
            value (float): value for IDD Field `total_sky_cover`
                value >= 0.0
                value <= 10.0
                Missing value: 99.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `total_sky_cover`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `total_sky_cover`')
            if value > 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `total_sky_cover`')

        self._total_sky_cover = value

    @property
    def opaque_sky_cover(self):
        """Get opaque_sky_cover.

        Returns:
            float: The value of `opaque_sky_cover` or None if not set

        """
        return self._opaque_sky_cover

    @opaque_sky_cover.setter
    def opaque_sky_cover(self, value=99.0):
        """Corresponds to IDD Field `opaque_sky_cover` This is the value for
        opaque sky cover (tenths of coverage). (i.e. 1 is 1/10 covered. 10 is
        total  coverage). (Amount of sky dome in tenths covered by clouds or
        obscuring phenomena that  prevent observing the sky or higher cloud
        layers at the time indicated.) This is not used unless the field for
        Horizontal Infrared Radiation Intensity is missing and then it is used
        to  calculate Horizontal Infrared Radiation Intensity.

        Args:
            value (float): value for IDD Field `opaque_sky_cover`
                value >= 0.0
                value <= 10.0
                Missing value: 99.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `opaque_sky_cover`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `opaque_sky_cover`')
            if value > 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `opaque_sky_cover`')

        self._opaque_sky_cover = value

    @property
    def visibility(self):
        """Get visibility.

        Returns:
            float: The value of `visibility` or None if not set

        """
        return self._visibility

    @visibility.setter
    def visibility(self, value=9999.0):
        """Corresponds to IDD Field `visibility` This is the value for
        visibility in km. (Horizontal visibility at the time indicated.)

        Args:
            value (float): value for IDD Field `visibility`
                Unit: km
                Missing value: 9999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `visibility`'.format(value))

        self._visibility = value

    @property
    def ceiling_height(self):
        """Get ceiling_height.

        Returns:
            float: The value of `ceiling_height` or None if not set

        """
        return self._ceiling_height

    @ceiling_height.setter
    def ceiling_height(self, value=99999.0):
        """Corresponds to IDD Field `ceiling_height` This is the value for
        ceiling height in m. (77777 is unlimited ceiling height. 88888 is
        cirroform ceiling.) It is not currently used in EnergyPlus
        calculations.

        Args:
            value (float): value for IDD Field `ceiling_height`
                Unit: m
                Missing value: 99999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ceiling_height`'.format(value))

        self._ceiling_height = value

    @property
    def present_weather_observation(self):
        """Get present_weather_observation.

        Returns:
            int: The value of `present_weather_observation` or None if not set

        """
        return self._present_weather_observation

    @present_weather_observation.setter
    def present_weather_observation(self, value=None):
        """Corresponds to IDD Field `present_weather_observation` If the value
        of the field is 0, then the observed weather codes are taken from the
        following field. If the value of the field is 9, then "missing" weather
        is assumed. Since the primary use of these fields (Present Weather
        Observation and Present Weather Codes) is for rain/wet surfaces, a
        missing observation field or a missing weather code implies "no rain".

        Args:
            value (int): value for IDD Field `present_weather_observation`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError(
                    'value {} need to be of type int '
                    'for field `present_weather_observation`'.format(value))

        self._present_weather_observation = value

    @property
    def present_weather_codes(self):
        """Get present_weather_codes.

        Returns:
            int: The value of `present_weather_codes` or None if not set

        """
        return self._present_weather_codes

    @present_weather_codes.setter
    def present_weather_codes(self, value=None):
        """Corresponds to IDD Field `present_weather_codes`

        Args:
            value (int): value for IDD Field `present_weather_codes`
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError(
                    'value {} need to be of type int '
                    'for field `present_weather_codes`'.format(value))

        self._present_weather_codes = value

    @property
    def precipitable_water(self):
        """Get precipitable_water.

        Returns:
            float: The value of `precipitable_water` or None if not set

        """
        return self._precipitable_water

    @precipitable_water.setter
    def precipitable_water(self, value=999.0):
        """Corresponds to IDD Field `precipitable_water`

        Args:
            value (float): value for IDD Field `precipitable_water`
                Unit: mm
                Missing value: 999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `precipitable_water`'.format(value))

        self._precipitable_water = value

    @property
    def aerosol_optical_depth(self):
        """Get aerosol_optical_depth.

        Returns:
            float: The value of `aerosol_optical_depth` or None if not set

        """
        return self._aerosol_optical_depth

    @aerosol_optical_depth.setter
    def aerosol_optical_depth(self, value=0.999):
        """Corresponds to IDD Field `aerosol_optical_depth`

        Args:
            value (float): value for IDD Field `aerosol_optical_depth`
                Unit: thousandths
                Missing value: 0.999
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `aerosol_optical_depth`'.format(value))

        self._aerosol_optical_depth = value

    @property
    def snow_depth(self):
        """Get snow_depth.

        Returns:
            float: The value of `snow_depth` or None if not set

        """
        return self._snow_depth

    @snow_depth.setter
    def snow_depth(self, value=999.0):
        """Corresponds to IDD Field `snow_depth`

        Args:
            value (float): value for IDD Field `snow_depth`
                Unit: cm
                Missing value: 999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `snow_depth`'.format(value))

        self._snow_depth = value

    @property
    def days_since_last_snowfall(self):
        """Get days_since_last_snowfall.

        Returns:
            int: The value of `days_since_last_snowfall` or None if not set

        """
        return self._days_since_last_snowfall

    @days_since_last_snowfall.setter
    def days_since_last_snowfall(self, value=99):
        """Corresponds to IDD Field `days_since_last_snowfall`

        Args:
            value (int): value for IDD Field `days_since_last_snowfall`
                Missing value: 99
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError(
                    'value {} need to be of type int '
                    'for field `days_since_last_snowfall`'.format(value))

        self._days_since_last_snowfall = value

    @property
    def albedo(self):
        """Get albedo.

        Returns:
            float: The value of `albedo` or None if not set

        """
        return self._albedo

    @albedo.setter
    def albedo(self, value=999.0):
        """Corresponds to IDD Field `albedo`

        Args:
            value (float): value for IDD Field `albedo`
                Missing value: 999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `albedo`'.format(value))

        self._albedo = value

    @property
    def liquid_precipitation_depth(self):
        """Get liquid_precipitation_depth.

        Returns:
            float: The value of `liquid_precipitation_depth` or None if not set

        """
        return self._liquid_precipitation_depth

    @liquid_precipitation_depth.setter
    def liquid_precipitation_depth(self, value=999.0):
        """Corresponds to IDD Field `liquid_precipitation_depth`

        Args:
            value (float): value for IDD Field `liquid_precipitation_depth`
                Unit: mm
                Missing value: 999.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `liquid_precipitation_depth`'.format(value))

        self._liquid_precipitation_depth = value

    @property
    def liquid_precipitation_quantity(self):
        """Get liquid_precipitation_quantity.

        Returns:
            float: The value of `liquid_precipitation_quantity` or None if not set

        """
        return self._liquid_precipitation_quantity

    @liquid_precipitation_quantity.setter
    def liquid_precipitation_quantity(self, value=99.0):
        """Corresponds to IDD Field `liquid_precipitation_quantity`

        Args:
            value (float): value for IDD Field `liquid_precipitation_quantity`
                Unit: hr
                Missing value: 99.0
                 a `value` of None will not be checked against the specification

        Raises:
            ValueError: if `value` is not a valid value

        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError(
                    'value {} need to be of type float '
                    'for field `liquid_precipitation_quantity`'.format(value))

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
        out.append(self._to_str(self.opaque_sky_cover))
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
            design_conditions=None,
            typical_or_extreme_periods=None,
            ground_temperatures=None,
            holidays_or_daylight_savings=None,
            comments_1=None,
            comments_2=None,
            data_periods=None,
            weatherdata=[]):
        self._data = OrderedDict()
        self._data["LOCATION"] = location
        self._data["DESIGN CONDITIONS"] = design_conditions
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
    def design_conditions(self):
        """Get design_conditions data dictionary object."""
        return self._data["DESIGN CONDITIONS"]

    @design_conditions.setter
    def design_conditions(self, data_dictionary):
        """Set design_conditions data dictionary object."""
        self._data["DESIGN CONDITIONS"] = data_dictionary

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
            f.write(self._data["DESIGN CONDITIONS"].export() + "\n")
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
        if internal_name == "DESIGN CONDITIONS":
            return DesignConditions()
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
