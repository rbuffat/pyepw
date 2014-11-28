#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on the EPW IDD specification given in the document
Auxiliary EnergyPlus Programs - Extra programs for EnergyPlus, Date: November 22 2013

Do not expect that it actually works!

Generation date: {{ generation_date}}

"""
from collections import OrderedDict
import re

{% for datadict in datadicts %}
{{ datadict }}
{% endfor %}

class EPW(object):

    def __init__(
            self,
            {%- for obj in objs %}
            {{obj.var_name}}=None,
            {%- endfor %}
            weatherdata=[]):
        self._data = OrderedDict()
        {%- for obj in objs %}
        self._data["{{obj.internal_name}}"] = {{ obj.var_name }}
        {%- endfor %}
        self._data["WEATHER DATA"] = weatherdata

    {%- for obj in objs %}
    @property
    def {{obj.var_name}}(self):
        """Get {{obj.var_name}} data dictionary object"""
        return self._data["{{obj.internal_name}}"]
    
    @{{obj.var_name}}.setter
    def {{obj.var_name}}(self, data_dictionary):
        """Set {{obj.var_name}} data dictionary object"""
        self._data["{{obj.internal_name}}"] = data_dictionary
     
    {%- endfor %}
    
    @property
    def weatherdata(self):
        """Get list of WeatherData data dictionary objects"""
        return self._data["WEATHER DATA"]
    
    @weatherdata.setter
    def weatherdata(self, weatherdata):
        """Set list of WeatherData data dictionary objects"""
        self._data["WEATHER DATA"] = weatherdata

    def add_weatherdata(self, data):
        """ Add weather data, data need to be of type WeatherData"""
        if not isinstance(data, WeatherData):
            raise ValueError('Weather data need to be of type WeatherData')
        self._data["WEATHER DATA"].append(data)

    def save(self, path):
        """ Save WeatherData in EPW format to path"""
        with open(path, 'w') as f:
            {%- for obj in objs %}
            f.write(self._data["{{obj.internal_name}}"].export() + "\n")
            {%- endfor %}
            for item in self._data["WEATHER DATA"]:
                f.write(item.export(False) + "\n")

    def _create_datadict(self, internal_name):
        {%- for obj in objs %}
        if internal_name == "{{ obj.internal_name }}":
            return {{ obj.class_name }}()
        {%- endfor %}
        raise ValueError("No DataDictionary known for {}".format(internal_name))

    def read(self, path):
        """Read EPW weather data from path"""
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                match_obj_name = re.search(r"^([A-Z][A-Z/ \d]+),", line)
                if match_obj_name is not None:
                    internal_name = match_obj_name.group(1)
                    if internal_name in self._data:
                        self._data[internal_name] = self._create_datadict(internal_name)
                        data_line = line[len(internal_name) + 1:]
                        vals = data_line.strip().split(',')
                        self._data[internal_name].read(vals)
                else:
                    wd = WeatherData()
                    wd.read(line.strip().split(','))
                    self.add_weatherdata(wd)
