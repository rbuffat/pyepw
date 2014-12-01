#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on the EPW IDD specification given in the document
Auxiliary EnergyPlus Programs - Extra programs for EnergyPlus,
Date: November 22 2013

Do not expect that it actually works!

Generation date: {{ generation_date}}

"""
from collections import OrderedDict
import re

{% for datadict in datadicts %}
{{ datadict }}
{% endfor %}

class EPW(object):
    """ Represens a EnergyPlus EPW weather data file
    """

    def __init__(
            self,
            {%- for obj in objs %}
            {{obj.var_name}}=None,
            {%- endfor %}
            weatherdata=None):
        """ Inits EPW with no data dictionary set."""
        self._data = OrderedDict()
        {%- for obj in objs %}
        self._data["{{obj.internal_name}}"] = {{ obj.var_name }}
        {%- endfor %}
        if weatherdata is None:
            weatherdata = []
        
        self._data["WEATHER DATA"] = weatherdata

    {%- for obj in objs %}
    @property
    def {{obj.var_name}}(self):
        """Get {{obj.var_name}} data dictionary object
        
           Returns:
               Object of type {{obj.class_name}} or None if not yet set
        """
        return self._data["{{obj.internal_name}}"]
    
    @{{obj.var_name}}.setter
    def {{obj.var_name}}(self, value):
        """Set {{obj.var_name}} data dictionary object
        
           Args:
               value ({{obj.class_name}}): sets data dictionary for IDD {{obj.internal_name}}
        """
        self._data["{{obj.internal_name}}"] = value
     
    {%- endfor %}
    
    @property
    def weatherdata(self):
        """Get list of WeatherData data dictionary objects
        
           Returns:
               list of WeatherData objects
        """
        return self._data["WEATHER DATA"]
    
    @weatherdata.setter
    def weatherdata(self, weatherdata):
        """Set list of WeatherData data dictionary objects
        
        Args:
            weatherdata (list): list of WeatherData objects
        """
        self._data["WEATHER DATA"] = weatherdata

    def add_weatherdata(self, data):
        """ Appends weather data
        
        Args:
            data (WeatherData): weather data object
        """
        if not isinstance(data, WeatherData):
            raise ValueError('Weather data need to be of type WeatherData')
        self._data["WEATHER DATA"].append(data)

    def save(self, path, check=True):
        """ Save WeatherData in EPW format to path
        
            Args:
                path (str): path where EPW file should be saved
        """
        with open(path, 'w') as f:
            if check:
                {%- for obj in objs %}
                if ("{{obj.internal_name}}" not in self._data or 
                    self._data["{{obj.internal_name}}"] is None):
                    raise ValueError('{{ obj.var_name }} is not valid.')
                {%- endfor %}
            {%- for obj in objs %}
            if ("{{obj.internal_name}}" in self._data and 
                self._data["{{obj.internal_name}}"] is not None):
                f.write(self._data["{{obj.internal_name}}"].export() + "\n")
            {%- endfor %}
            for item in self._data["WEATHER DATA"]:
                f.write(item.export(False) + "\n")

    @classmethod
    def _create_datadict(cls, internal_name):
        """ Creates an object depending on `internal_name`
        
            Args:
                internal_name (str): IDD name
                
            Raises:
                ValueError: if `internal_name` cannot be matched to a data dictionary object
        """
        {%- for obj in objs %}
        if internal_name == "{{ obj.internal_name }}":
            return {{ obj.class_name }}()
        {%- endfor %}
        raise ValueError("No DataDictionary known for {}".format(internal_name))

    def read(self, path):
        """Read EPW weather data from path
        
           Args:
               path (str): path to read weather data from
        """
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
