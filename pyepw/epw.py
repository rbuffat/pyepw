"""
WARNING: This is an automatic generated file.
It is based on the EPW IDD specification given in the document
Auxiliary EnergyPlus Programs - Extra programs for EnergyPlus, Date: November 22 2013

Do not expect that it actually works!

Generation date: 2014-11-18

"""


class Location(object):

    """ Corresponds to EPW IDD object `LOCATION`
    """
    internal_name = "LOCATION"

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

    @property
    def city(self):
        """Get city"""
        return self._city

    @city.setter
    def city(self, value=None):
        """  Corresponds to IDD Field `city`

        """

        assert isinstance(value, str)

        self._city = value

    @property
    def state_province_region(self):
        """Get state_province_region"""
        return self._state_province_region

    @state_province_region.setter
    def state_province_region(self, value=None):
        """  Corresponds to IDD Field `State Province Region`

        """

        assert isinstance(value, str)

        self._state_province_region = value

    @property
    def country(self):
        """Get country"""
        return self._country

    @country.setter
    def country(self, value=None):
        """  Corresponds to IDD Field `Country`

        """

        assert isinstance(value, str)

        self._country = value

    @property
    def source(self):
        """Get source"""
        return self._source

    @source.setter
    def source(self, value=None):
        """  Corresponds to IDD Field `Source`

        """

        assert isinstance(value, str)

        self._source = value

    @property
    def wmo(self):
        """Get wmo"""
        return self._wmo

    @wmo.setter
    def wmo(self, value=None):
        """  Corresponds to IDD Field `WMO`

        usually a 6 digit field. Used as alpha in EnergyPlus
        """

        assert isinstance(value, str)

        self._wmo = value

    @property
    def latitude(self):
        """Get latitude"""
        return self._latitude

    @latitude.setter
    def latitude(self, value=0.0):
        """  Corresponds to IDD Field `Latitude`

        + is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)
        Unit: deg
        Minimum: -90.0
        Maximum: 90.0
        Default: 0.0
        """

        assert isinstance(value, float)
        assert value >= -90.0
        assert value <= 90.0

        self._latitude = value

    @property
    def longitude(self):
        """Get longitude"""
        return self._longitude

    @longitude.setter
    def longitude(self, value=0.0):
        """  Corresponds to IDD Field `Longitude`

        - is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)
        Unit: deg
        Minimum: -180.0
        Maximum: 180.0
        Default: 0.0
        """

        assert isinstance(value, float)
        assert value >= -180.0
        assert value <= 180.0

        self._longitude = value

    @property
    def timezone(self):
        """Get timezone"""
        return self._timezone

    @timezone.setter
    def timezone(self, value=0.0):
        """  Corresponds to IDD Field `TimeZone`

        Time relative to GMT.
        Unit: hr - not on standard units list???
        Minimum: -12.0
        Maximum: 12.0
        Default: 0.0
        """

        assert isinstance(value, float)
        assert value >= -12.0
        assert value <= 12.0

        self._timezone = value

    @property
    def elevation(self):
        """Get elevation"""
        return self._elevation

    @elevation.setter
    def elevation(self, value=0.0):
        """  Corresponds to IDD Field `Elevation`

        Unit: m
        Minimum: -1000.0
        Maximum<: 9999.9
        Default: 0.0
        """

        assert isinstance(value, float)
        assert value >= -1000.0
        assert value < 9999.9

        self._elevation = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
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


class TypicalOrExtremePeriod(object):

    """ Corresponds to EPW IDD object `TYPICAL/EXTREME PERIOD`
    """
    internal_name = "TYPICAL/EXTREME PERIOD"

    def __init__(self):
        self._typical_or_extreme_period_name = None
        self._typical_or_extreme_period__type = None
        self._period_start_day = None
        self._period__end_day = None

    @property
    def typical_or_extreme_period_name(self):
        """Get typical_or_extreme_period_name"""
        return self._typical_or_extreme_period_name

    @typical_or_extreme_period_name.setter
    def typical_or_extreme_period_name(self, value=None):
        """  Corresponds to IDD Field `Typical/Extreme Period Name`

        """

        assert isinstance(value, str)

        self._typical_or_extreme_period_name = value

    @property
    def typical_or_extreme_period__type(self):
        """Get typical_or_extreme_period__type"""
        return self._typical_or_extreme_period__type

    @typical_or_extreme_period__type.setter
    def typical_or_extreme_period__type(self, value=None):
        """  Corresponds to IDD Field `Typical/Extreme Period  Type`

        """

        assert isinstance(value, str)

        self._typical_or_extreme_period__type = value

    @property
    def period_start_day(self):
        """Get period_start_day"""
        return self._period_start_day

    @period_start_day.setter
    def period_start_day(self, value=None):
        """  Corresponds to IDD Field `Period Start Day`

        """

        assert isinstance(value, str)

        self._period_start_day = value

    @property
    def period__end_day(self):
        """Get period__end_day"""
        return self._period__end_day

    @period__end_day.setter
    def period__end_day(self, value=None):
        """  Corresponds to IDD Field `Period  End Day`

        """

        assert isinstance(value, str)

        self._period__end_day = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(self._to_str(self.typical_or_extreme_period_name))
        out.append(self._to_str(self.typical_or_extreme_period__type))
        out.append(self._to_str(self.period_start_day))
        out.append(self._to_str(self.period__end_day))
        return ",".join(out)


class TypicalOrExtremePeriods(object):

    """ Corresponds to EPW IDD object `TYPICAL/EXTREME PERIODS`
    """
    internal_name = "TYPICAL/EXTREME PERIODS"

    def __init__(self):
        self._typical_or_extreme_periods = []

    def add_typical_or_extreme_period(self, value):
        """Add TypicalOrExtremePeriod"""
        self._typical_or_extreme_periods.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(str(len(self._typical_or_extreme_periods)))
        for obj in self._typical_or_extreme_periods:
            out.append(obj.export(top=False))
        return ",".join(out)


class GroundTemperature(object):

    """ Corresponds to EPW IDD object `GROUND TEMPERATURE`
    """
    internal_name = "GROUND TEMPERATURE"

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

    @property
    def ground_temperature_depth(self):
        """Get ground_temperature_depth"""
        return self._ground_temperature_depth

    @ground_temperature_depth.setter
    def ground_temperature_depth(self, value=None):
        """  Corresponds to IDD Field `Ground Temperature Depth`

        Unit: m
        """

        assert isinstance(value, float)

        self._ground_temperature_depth = value

    @property
    def depth_soil_conductivity(self):
        """Get depth_soil_conductivity"""
        return self._depth_soil_conductivity

    @depth_soil_conductivity.setter
    def depth_soil_conductivity(self, value=None):
        """  Corresponds to IDD Field `Depth Soil Conductivity`

        Unit: W/m-K,
        """

        assert isinstance(value, float)

        self._depth_soil_conductivity = value

    @property
    def depth_soil_density(self):
        """Get depth_soil_density"""
        return self._depth_soil_density

    @depth_soil_density.setter
    def depth_soil_density(self, value=None):
        """  Corresponds to IDD Field `Depth Soil Density`

        Unit: kg/m3
        """

        assert isinstance(value, float)

        self._depth_soil_density = value

    @property
    def depth_soil_specific_heat(self):
        """Get depth_soil_specific_heat"""
        return self._depth_soil_specific_heat

    @depth_soil_specific_heat.setter
    def depth_soil_specific_heat(self, value=None):
        """  Corresponds to IDD Field `Depth Soil Specific Heat`

        Unit: J/kg-K,
        """

        assert isinstance(value, float)

        self._depth_soil_specific_heat = value

    @property
    def depth_january_average_ground_temperature(self):
        """Get depth_january_average_ground_temperature"""
        return self._depth_january_average_ground_temperature

    @depth_january_average_ground_temperature.setter
    def depth_january_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth January Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_january_average_ground_temperature = value

    @property
    def depth_february_average_ground_temperature(self):
        """Get depth_february_average_ground_temperature"""
        return self._depth_february_average_ground_temperature

    @depth_february_average_ground_temperature.setter
    def depth_february_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth February Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_february_average_ground_temperature = value

    @property
    def depth_march_average_ground_temperature(self):
        """Get depth_march_average_ground_temperature"""
        return self._depth_march_average_ground_temperature

    @depth_march_average_ground_temperature.setter
    def depth_march_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth March Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_march_average_ground_temperature = value

    @property
    def depth_april_average_ground_temperature(self):
        """Get depth_april_average_ground_temperature"""
        return self._depth_april_average_ground_temperature

    @depth_april_average_ground_temperature.setter
    def depth_april_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth April Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_april_average_ground_temperature = value

    @property
    def depth_may_average_ground_temperature(self):
        """Get depth_may_average_ground_temperature"""
        return self._depth_may_average_ground_temperature

    @depth_may_average_ground_temperature.setter
    def depth_may_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth May Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_may_average_ground_temperature = value

    @property
    def depth_june_average_ground_temperature(self):
        """Get depth_june_average_ground_temperature"""
        return self._depth_june_average_ground_temperature

    @depth_june_average_ground_temperature.setter
    def depth_june_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth June Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_june_average_ground_temperature = value

    @property
    def depth_july_average_ground_temperature(self):
        """Get depth_july_average_ground_temperature"""
        return self._depth_july_average_ground_temperature

    @depth_july_average_ground_temperature.setter
    def depth_july_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth July Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_july_average_ground_temperature = value

    @property
    def depth_august_average_ground_temperature(self):
        """Get depth_august_average_ground_temperature"""
        return self._depth_august_average_ground_temperature

    @depth_august_average_ground_temperature.setter
    def depth_august_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth August Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_august_average_ground_temperature = value

    @property
    def depth_september_average_ground_temperature(self):
        """Get depth_september_average_ground_temperature"""
        return self._depth_september_average_ground_temperature

    @depth_september_average_ground_temperature.setter
    def depth_september_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth September Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_september_average_ground_temperature = value

    @property
    def depth_october_average_ground_temperature(self):
        """Get depth_october_average_ground_temperature"""
        return self._depth_october_average_ground_temperature

    @depth_october_average_ground_temperature.setter
    def depth_october_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth October Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_october_average_ground_temperature = value

    @property
    def depth_november_average_ground_temperature(self):
        """Get depth_november_average_ground_temperature"""
        return self._depth_november_average_ground_temperature

    @depth_november_average_ground_temperature.setter
    def depth_november_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth November Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_november_average_ground_temperature = value

    @property
    def depth_december_average_ground_temperature(self):
        """Get depth_december_average_ground_temperature"""
        return self._depth_december_average_ground_temperature

    @depth_december_average_ground_temperature.setter
    def depth_december_average_ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Depth December Average Ground Temperature`

        Unit: C
        """

        assert isinstance(value, float)

        self._depth_december_average_ground_temperature = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
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


class GroundTemperatures(object):

    """ Corresponds to EPW IDD object `GROUND TEMPERATURES`
    """
    internal_name = "GROUND TEMPERATURES"

    def __init__(self):
        self._ground_temperatures = []

    def add_ground_temperature(self, value):
        """Add GroundTemperature"""
        self._ground_temperatures.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(str(len(self._ground_temperatures)))
        for obj in self._ground_temperatures:
            out.append(obj.export(top=False))
        return ",".join(out)


class Holiday(object):

    """ Corresponds to EPW IDD object `HOLIDAY`
    """
    internal_name = "HOLIDAY"

    def __init__(self):
        self._holiday_name = None
        self._holiday_day = None

    @property
    def holiday_name(self):
        """Get holiday_name"""
        return self._holiday_name

    @holiday_name.setter
    def holiday_name(self, value=None):
        """  Corresponds to IDD Field `Holiday Name`

        """

        assert isinstance(value, str)

        self._holiday_name = value

    @property
    def holiday_day(self):
        """Get holiday_day"""
        return self._holiday_day

    @holiday_day.setter
    def holiday_day(self, value=None):
        """  Corresponds to IDD Field `Holiday Day`

        """

        assert isinstance(value, str)

        self._holiday_day = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(self._to_str(self.holiday_name))
        out.append(self._to_str(self.holiday_day))
        return ",".join(out)


class HolidaysOrDaylightSaving(object):

    """ Corresponds to EPW IDD object `HOLIDAYS/DAYLIGHT SAVING`
    """
    internal_name = "HOLIDAYS/DAYLIGHT SAVING"

    def __init__(self):
        self._leapyear_observed = None
        self._daylight_saving_start_day = None
        self._daylight_saving_end_day = None
        self._holidays = []

    @property
    def leapyear_observed(self):
        """Get leapyear_observed"""
        return self._leapyear_observed

    @leapyear_observed.setter
    def leapyear_observed(self, value=None):
        """  Corresponds to IDD Field `LeapYear Observed`

        Yes if Leap Year will be observed for this file
        No if Leap Year days (29 Feb) should be ignored in this file
        Accepted values:
         - Yes
         - No
        """

        assert value in ["Yes", "No"]

        self._leapyear_observed = value

    @property
    def daylight_saving_start_day(self):
        """Get daylight_saving_start_day"""
        return self._daylight_saving_start_day

    @daylight_saving_start_day.setter
    def daylight_saving_start_day(self, value=None):
        """  Corresponds to IDD Field `Daylight Saving Start Day`

        """

        assert isinstance(value, str)

        self._daylight_saving_start_day = value

    @property
    def daylight_saving_end_day(self):
        """Get daylight_saving_end_day"""
        return self._daylight_saving_end_day

    @daylight_saving_end_day.setter
    def daylight_saving_end_day(self, value=None):
        """  Corresponds to IDD Field `Daylight Saving End Day`

        """

        assert isinstance(value, str)

        self._daylight_saving_end_day = value

    def add_holiday(self, value):
        """Add Holiday"""
        self._holidays.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(self._to_str(self.leapyear_observed))
        out.append(self._to_str(self.daylight_saving_start_day))
        out.append(self._to_str(self.daylight_saving_end_day))
        out.append(str(len(self._holidays)))
        for obj in self._holidays:
            out.append(obj.export(top=False))
        return ",".join(out)


class Comments1(object):

    """ Corresponds to EPW IDD object `COMMENTS 1`
    """
    internal_name = "COMMENTS 1"

    def __init__(self):
        self._comments_1 = None

    @property
    def comments_1(self):
        """Get comments_1"""
        return self._comments_1

    @comments_1.setter
    def comments_1(self, value=None):
        """  Corresponds to IDD Field `Comments_1`

        """

        assert isinstance(value, str)

        self._comments_1 = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(self._to_str(self.comments_1))
        return ",".join(out)


class Comments2(object):

    """ Corresponds to EPW IDD object `COMMENTS 2`
    """
    internal_name = "COMMENTS 2"

    def __init__(self):
        self._comments_2 = None

    @property
    def comments_2(self):
        """Get comments_2"""
        return self._comments_2

    @comments_2.setter
    def comments_2(self, value=None):
        """  Corresponds to IDD Field `Comments_2`

        """

        assert isinstance(value, str)

        self._comments_2 = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(self._to_str(self.comments_2))
        return ",".join(out)


class DataPeriod(object):

    """ Corresponds to EPW IDD object `DATA PERIOD`
    """
    internal_name = "DATA PERIOD"

    def __init__(self):
        self._number_of_records_per_hour = None
        self._data_period_name_or_description = None
        self._data_period_start_day_of_week = None
        self._data_period_start_day = None
        self._data_period_end_day = None

    @property
    def number_of_records_per_hour(self):
        """Get number_of_records_per_hour"""
        return self._number_of_records_per_hour

    @number_of_records_per_hour.setter
    def number_of_records_per_hour(self, value=None):
        """  Corresponds to IDD Field `Number of Records per hour`

        """

        assert isinstance(value, float)

        self._number_of_records_per_hour = value

    @property
    def data_period_name_or_description(self):
        """Get data_period_name_or_description"""
        return self._data_period_name_or_description

    @data_period_name_or_description.setter
    def data_period_name_or_description(self, value=None):
        """  Corresponds to IDD Field `Data Period Name/Description`

        """

        assert isinstance(value, str)

        self._data_period_name_or_description = value

    @property
    def data_period_start_day_of_week(self):
        """Get data_period_start_day_of_week"""
        return self._data_period_start_day_of_week

    @data_period_start_day_of_week.setter
    def data_period_start_day_of_week(self, value=None):
        """  Corresponds to IDD Field `Data Period Start Day of Week`

        Accepted values:
         - Sunday
         - Monday
         - Tuesday
         - Wednesday
         - Thursday
         - Friday
         - Saturday
        """

        assert value in [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"]

        self._data_period_start_day_of_week = value

    @property
    def data_period_start_day(self):
        """Get data_period_start_day"""
        return self._data_period_start_day

    @data_period_start_day.setter
    def data_period_start_day(self, value=None):
        """  Corresponds to IDD Field `Data Period Start Day`

        """

        assert isinstance(value, str)

        self._data_period_start_day = value

    @property
    def data_period_end_day(self):
        """Get data_period_end_day"""
        return self._data_period_end_day

    @data_period_end_day.setter
    def data_period_end_day(self, value=None):
        """  Corresponds to IDD Field `Data Period End Day`

        """

        assert isinstance(value, str)

        self._data_period_end_day = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(self._to_str(self.number_of_records_per_hour))
        out.append(self._to_str(self.data_period_name_or_description))
        out.append(self._to_str(self.data_period_start_day_of_week))
        out.append(self._to_str(self.data_period_start_day))
        out.append(self._to_str(self.data_period_end_day))
        return ",".join(out)


class DataPeriods(object):

    """ Corresponds to EPW IDD object `DATA PERIODS`
    """
    internal_name = "DATA PERIODS"

    def __init__(self):
        self._data_periods = []

    def add_data_period(self, value):
        """Add DataPeriod"""
        self._data_periods.append(value)

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
        out.append(str(len(self._data_periods)))
        for obj in self._data_periods:
            out.append(obj.export(top=False))
        return ",".join(out)


class Items(object):

    """ Corresponds to EPW IDD object `ITEMS`
    """
    internal_name = "ITEMS"

    def __init__(self):
        self._year = None
        self._month = None
        self._day = None
        self._hour = None
        self._minute = None
        self._data_source_and_uncertainty_flags = None
        self._dry_bulb_temperature = 99.9
        self._dew_point_temperature = 99.9
        self._relative_humidity = 999.0
        self._atmospheric_station_pressure = 999999.0
        self._extraterrestrial_horizontal_radiation = 9999.0
        self._extraterrestrial_direct_normal_radiation = 9999.0
        self._horizontal_infrared_radiation_intensity = 9999.0
        self._global_horizontal_radiation = 9999.0
        self._direct_normal_radiation = 9999.0
        self._diffuse_horizontal_radiation = 9999.0
        self._global_horizontal_illuminance = 999999.0
        self._direct_normal_illuminance = 999999.0
        self._diffuse_horizontal_illuminance = 999999.0
        self._zenith_luminance = 9999.0
        self._wind_direction = 999.0
        self._wind_speed = 999.0
        self._total_sky_cover = 99.0
        self._opaque_sky_cover_used_if_horizontal_ir_intensity_missing = 99.0
        self._visibility = 9999.0
        self._ceiling_height = 99999.0
        self._present_weather_observation = None
        self._present_weather_codes = None
        self._precipitable_water = 999.0
        self._aerosol_optical_depth = 0.999
        self._snow_depth = 999.0
        self._days_since_last_snowfall = 99.0
        self._albedo = 999.0
        self._liquid_precipitation_depth = 999.0
        self._liquid_precipitation_quantity = 99.0

    @property
    def year(self):
        """Get year"""
        return self._year

    @year.setter
    def year(self, value=None):
        """  Corresponds to IDD Field `Year`

        """

        assert isinstance(value, float)

        self._year = value

    @property
    def month(self):
        """Get month"""
        return self._month

    @month.setter
    def month(self, value=None):
        """  Corresponds to IDD Field `Month`

        """

        assert isinstance(value, float)

        self._month = value

    @property
    def day(self):
        """Get day"""
        return self._day

    @day.setter
    def day(self, value=None):
        """  Corresponds to IDD Field `Day`

        """

        assert isinstance(value, float)

        self._day = value

    @property
    def hour(self):
        """Get hour"""
        return self._hour

    @hour.setter
    def hour(self, value=None):
        """  Corresponds to IDD Field `Hour`

        """

        assert isinstance(value, float)

        self._hour = value

    @property
    def minute(self):
        """Get minute"""
        return self._minute

    @minute.setter
    def minute(self, value=None):
        """  Corresponds to IDD Field `Minute`

        """

        assert isinstance(value, float)

        self._minute = value

    @property
    def data_source_and_uncertainty_flags(self):
        """Get data_source_and_uncertainty_flags"""
        return self._data_source_and_uncertainty_flags

    @data_source_and_uncertainty_flags.setter
    def data_source_and_uncertainty_flags(self, value=None):
        """  Corresponds to IDD Field `Data Source and Uncertainty Flags`

        Initial day of weather file is checked by EnergyPlus for validity (as shown below)
        Each field is checked for "missing" as shown below. Reasonable values, calculated
        values or the last "good" value is substituted.
        """

        assert isinstance(value, str)

        self._data_source_and_uncertainty_flags = value

    @property
    def dry_bulb_temperature(self):
        """Get dry_bulb_temperature"""
        return self._dry_bulb_temperature

    @dry_bulb_temperature.setter
    def dry_bulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Dry Bulb Temperature`

        Unit: C
        Minimum>: -70.0
        Maximum<: 70.0
        """

        assert isinstance(value, float)
        assert value > -70.0
        assert value < 70.0

        self._dry_bulb_temperature = value

    @property
    def dew_point_temperature(self):
        """Get dew_point_temperature"""
        return self._dew_point_temperature

    @dew_point_temperature.setter
    def dew_point_temperature(self, value=None):
        """  Corresponds to IDD Field `Dew Point Temperature`

        Unit: C
        Minimum>: -70.0
        Maximum<: 70.0
        """

        assert isinstance(value, float)
        assert value > -70.0
        assert value < 70.0

        self._dew_point_temperature = value

    @property
    def relative_humidity(self):
        """Get relative_humidity"""
        return self._relative_humidity

    @relative_humidity.setter
    def relative_humidity(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity`

        Minimum: 0.0
        Maximum: 110.0
        """

        assert isinstance(value, float)
        assert value >= 0.0
        assert value <= 110.0

        self._relative_humidity = value

    @property
    def atmospheric_station_pressure(self):
        """Get atmospheric_station_pressure"""
        return self._atmospheric_station_pressure

    @atmospheric_station_pressure.setter
    def atmospheric_station_pressure(self, value=None):
        """  Corresponds to IDD Field `Atmospheric Station Pressure`

        Unit: Pa
        Minimum>: 31000.0
        Maximum<: 120000.0
        """

        assert isinstance(value, float)
        assert value > 31000.0
        assert value < 120000.0

        self._atmospheric_station_pressure = value

    @property
    def extraterrestrial_horizontal_radiation(self):
        """Get extraterrestrial_horizontal_radiation"""
        return self._extraterrestrial_horizontal_radiation

    @extraterrestrial_horizontal_radiation.setter
    def extraterrestrial_horizontal_radiation(self, value=None):
        """  Corresponds to IDD Field `Extraterrestrial Horizontal Radiation`

        Unit: Wh/m2
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._extraterrestrial_horizontal_radiation = value

    @property
    def extraterrestrial_direct_normal_radiation(self):
        """Get extraterrestrial_direct_normal_radiation"""
        return self._extraterrestrial_direct_normal_radiation

    @extraterrestrial_direct_normal_radiation.setter
    def extraterrestrial_direct_normal_radiation(self, value=None):
        """  Corresponds to IDD Field `Extraterrestrial Direct Normal Radiation`

        Unit: Wh/m2
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._extraterrestrial_direct_normal_radiation = value

    @property
    def horizontal_infrared_radiation_intensity(self):
        """Get horizontal_infrared_radiation_intensity"""
        return self._horizontal_infrared_radiation_intensity

    @horizontal_infrared_radiation_intensity.setter
    def horizontal_infrared_radiation_intensity(self, value=None):
        """  Corresponds to IDD Field `Horizontal Infrared Radiation Intensity`

        Unit: Wh/m2
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._horizontal_infrared_radiation_intensity = value

    @property
    def global_horizontal_radiation(self):
        """Get global_horizontal_radiation"""
        return self._global_horizontal_radiation

    @global_horizontal_radiation.setter
    def global_horizontal_radiation(self, value=None):
        """  Corresponds to IDD Field `Global Horizontal Radiation`

        Unit: Wh/m2
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._global_horizontal_radiation = value

    @property
    def direct_normal_radiation(self):
        """Get direct_normal_radiation"""
        return self._direct_normal_radiation

    @direct_normal_radiation.setter
    def direct_normal_radiation(self, value=None):
        """  Corresponds to IDD Field `Direct Normal Radiation`

        Unit: Wh/m2
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._direct_normal_radiation = value

    @property
    def diffuse_horizontal_radiation(self):
        """Get diffuse_horizontal_radiation"""
        return self._diffuse_horizontal_radiation

    @diffuse_horizontal_radiation.setter
    def diffuse_horizontal_radiation(self, value=None):
        """  Corresponds to IDD Field `Diffuse Horizontal Radiation`

        Unit: Wh/m2
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._diffuse_horizontal_radiation = value

    @property
    def global_horizontal_illuminance(self):
        """Get global_horizontal_illuminance"""
        return self._global_horizontal_illuminance

    @global_horizontal_illuminance.setter
    def global_horizontal_illuminance(self, value=None):
        """  Corresponds to IDD Field `Global Horizontal Illuminance`

        will be missing if >= 999900
        Unit: lux
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._global_horizontal_illuminance = value

    @property
    def direct_normal_illuminance(self):
        """Get direct_normal_illuminance"""
        return self._direct_normal_illuminance

    @direct_normal_illuminance.setter
    def direct_normal_illuminance(self, value=None):
        """  Corresponds to IDD Field `Direct Normal Illuminance`

        will be missing if >= 999900
        Unit: lux
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._direct_normal_illuminance = value

    @property
    def diffuse_horizontal_illuminance(self):
        """Get diffuse_horizontal_illuminance"""
        return self._diffuse_horizontal_illuminance

    @diffuse_horizontal_illuminance.setter
    def diffuse_horizontal_illuminance(self, value=None):
        """  Corresponds to IDD Field `Diffuse Horizontal Illuminance`

        will be missing if >= 999900
        Unit: lux
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._diffuse_horizontal_illuminance = value

    @property
    def zenith_luminance(self):
        """Get zenith_luminance"""
        return self._zenith_luminance

    @zenith_luminance.setter
    def zenith_luminance(self, value=None):
        """  Corresponds to IDD Field `Zenith Luminance`

        will be missing if >= 9999
        Unit: Cd/m2
        Minimum: 0.0
        """

        assert isinstance(value, float)
        assert value >= 0.0

        self._zenith_luminance = value

    @property
    def wind_direction(self):
        """Get wind_direction"""
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value=None):
        """  Corresponds to IDD Field `Wind Direction`

        Unit: degrees
        Minimum: 0.0
        Maximum: 360.0
        """

        assert isinstance(value, float)
        assert value >= 0.0
        assert value <= 360.0

        self._wind_direction = value

    @property
    def wind_speed(self):
        """Get wind_speed"""
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value=None):
        """  Corresponds to IDD Field `Wind Speed`

        Unit: m/s
        Minimum: 0.0
        Maximum: 40.0
        """

        assert isinstance(value, float)
        assert value >= 0.0
        assert value <= 40.0

        self._wind_speed = value

    @property
    def total_sky_cover(self):
        """Get total_sky_cover"""
        return self._total_sky_cover

    @total_sky_cover.setter
    def total_sky_cover(self, value=None):
        """  Corresponds to IDD Field `Total Sky Cover`

        Minimum: 0.0
        Maximum: 10.0
        """

        assert isinstance(value, float)
        assert value >= 0.0
        assert value <= 10.0

        self._total_sky_cover = value

    @property
    def opaque_sky_cover_used_if_horizontal_ir_intensity_missing(self):
        """Get opaque_sky_cover_used_if_horizontal_ir_intensity_missing"""
        return self._opaque_sky_cover_used_if_horizontal_ir_intensity_missing

    @opaque_sky_cover_used_if_horizontal_ir_intensity_missing.setter
    def opaque_sky_cover_used_if_horizontal_ir_intensity_missing(
            self,
            value=None):
        """  Corresponds to IDD Field `Opaque Sky Cover (used if Horizontal IR Intensity missing)`

        Minimum: 0.0
        Maximum: 10.0
        """

        assert isinstance(value, float)
        assert value >= 0.0
        assert value <= 10.0

        self._opaque_sky_cover_used_if_horizontal_ir_intensity_missing = value

    @property
    def visibility(self):
        """Get visibility"""
        return self._visibility

    @visibility.setter
    def visibility(self, value=None):
        """  Corresponds to IDD Field `Visibility`

        Unit: km
        """

        assert isinstance(value, float)

        self._visibility = value

    @property
    def ceiling_height(self):
        """Get ceiling_height"""
        return self._ceiling_height

    @ceiling_height.setter
    def ceiling_height(self, value=None):
        """  Corresponds to IDD Field `Ceiling Height`

        Unit: m
        """

        assert isinstance(value, float)

        self._ceiling_height = value

    @property
    def present_weather_observation(self):
        """Get present_weather_observation"""
        return self._present_weather_observation

    @present_weather_observation.setter
    def present_weather_observation(self, value=None):
        """  Corresponds to IDD Field `Present Weather Observation`

        """

        assert isinstance(value, float)

        self._present_weather_observation = value

    @property
    def present_weather_codes(self):
        """Get present_weather_codes"""
        return self._present_weather_codes

    @present_weather_codes.setter
    def present_weather_codes(self, value=None):
        """  Corresponds to IDD Field `Present Weather Codes`

        """

        assert isinstance(value, float)

        self._present_weather_codes = value

    @property
    def precipitable_water(self):
        """Get precipitable_water"""
        return self._precipitable_water

    @precipitable_water.setter
    def precipitable_water(self, value=None):
        """  Corresponds to IDD Field `Precipitable Water`

        Unit: mm
        """

        assert isinstance(value, float)

        self._precipitable_water = value

    @property
    def aerosol_optical_depth(self):
        """Get aerosol_optical_depth"""
        return self._aerosol_optical_depth

    @aerosol_optical_depth.setter
    def aerosol_optical_depth(self, value=None):
        """  Corresponds to IDD Field `Aerosol Optical Depth`

        Unit: thousandths
        """

        assert isinstance(value, float)

        self._aerosol_optical_depth = value

    @property
    def snow_depth(self):
        """Get snow_depth"""
        return self._snow_depth

    @snow_depth.setter
    def snow_depth(self, value=None):
        """  Corresponds to IDD Field `Snow Depth`

        Unit: cm
        """

        assert isinstance(value, float)

        self._snow_depth = value

    @property
    def days_since_last_snowfall(self):
        """Get days_since_last_snowfall"""
        return self._days_since_last_snowfall

    @days_since_last_snowfall.setter
    def days_since_last_snowfall(self, value=None):
        """  Corresponds to IDD Field `Days Since Last Snowfall`

        """

        assert isinstance(value, float)

        self._days_since_last_snowfall = value

    @property
    def albedo(self):
        """Get albedo"""
        return self._albedo

    @albedo.setter
    def albedo(self, value=None):
        """  Corresponds to IDD Field `Albedo`

        """

        assert isinstance(value, float)

        self._albedo = value

    @property
    def liquid_precipitation_depth(self):
        """Get liquid_precipitation_depth"""
        return self._liquid_precipitation_depth

    @liquid_precipitation_depth.setter
    def liquid_precipitation_depth(self, value=None):
        """  Corresponds to IDD Field `Liquid Precipitation Depth`

        Unit: mm
        """

        assert isinstance(value, float)

        self._liquid_precipitation_depth = value

    @property
    def liquid_precipitation_quantity(self):
        """Get liquid_precipitation_quantity"""
        return self._liquid_precipitation_quantity

    @liquid_precipitation_quantity.setter
    def liquid_precipitation_quantity(self, value=None):
        """  Corresponds to IDD Field `Liquid Precipitation Quantity`

        Unit: hr
        """

        assert isinstance(value, float)

        self._liquid_precipitation_quantity = value

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return value.__str__()

    def export(self, top=True):
        out = []
        if top:
            out.append(self.internal_name)
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


class EPW(object):

    def create(
            self,
            location,
            typical_or_extreme_periods,
            ground_temperatures,
            holidays_or_daylight_saving,
            comments_1,
            comments_2,
            data_periods,
            items):
        out = []
        out.append(location.export() + "\n")
        out.append(typical_or_extreme_periods.export() + "\n")
        out.append(ground_temperatures.export() + "\n")
        out.append(holidays_or_daylight_saving.export() + "\n")
        out.append(comments_1.export() + "\n")
        out.append(comments_2.export() + "\n")
        out.append(data_periods.export() + "\n")
        for item in items:
            out.append(item.export(False))
        return "".join(out)
