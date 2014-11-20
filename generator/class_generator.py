'''
Created on Oct 30, 2014

@author: rene
'''
import string
IND = "    "


class EPWGenerator():

    def __init__(self):
        pass

    def normalize_object_name(self, internal_name):
        name = internal_name.replace('/', ' or ').strip()
        name = string.capwords(name)
        name = name.replace(' ', '')
        return name

    def normalize_object_name2(self, internal_name):
        name = internal_name.strip().replace('/', ' or ').lower()
        name = name.replace(' ', '_')
        name = name.replace('(', '')
        name = name.replace(')', '')
        return name

    def _value2py(self, value, vtype):

        if vtype == 'alpha':
            return str(value)
        if vtype == 'integer':
            return str(int(value))
        if vtype == 'real':
            return str(float(value))
        return value

    def _value2pyconv(self, vtype):

        if vtype == 'alpha':
            return "str"
        if vtype == 'integer':
            return "int"
        if vtype == 'real':
            return "float"
        return "str"

    def generate_class(self, obj):
        source = "class {}(object):\n".format(obj.name)
        source += IND + "\"\"\" Corresponds to EPW IDD object `{}`\n".format(
            obj.internal_name)
        source += IND + "\"\"\"\n"

        source += IND + "internal_name = \"{}\"\n".format(obj.internal_name)
        source += IND + "_fields_count = {}\n".format(len(obj.fields))

        params = ""
        lists = []
        for field in obj.fields:
            params += ", "
            params += field.name
            if "default" in field.attributes:
                params += "=" + field.attributes["default"]
            else:
                params += "=None"

            if field.is_list:
                lists.append(field)

            if not field.is_list and "type" not in field.attributes:
                if field.ftype == 'A':
                    field.attributes["type"] = "alpha"
                elif field.ftype == "N":
                    field.attributes["type"] = "real"

        if len(obj.fields) > 0:
            source += IND + "def __init__(self):\n"
            for field in obj.fields:
                if field.is_list:
                    source += IND + IND + "self._{}s = []\n".format(field.name)
                else:
                    val = "None"
                    if "missing" in field.attributes:
                        val = field.attributes["missing"]
                        if "type" in field.attributes:
                            val = self._value2py(val, field.attributes["type"])
                    source += IND + IND + "self._{} = {}\n".format(field.name, val)

        source += IND + "def read(self, vals):\n"
        source += IND + IND + "i = 0\n"

        for field in obj.fields:
            if not field.is_list:
                conv = "str"
                if "type" in field.attributes:
                    conv = self._value2pyconv(field.attributes["type"])
                source += IND + IND + "if len(vals[i]) == 0:\n"
                source += IND + IND + IND + "self.{} = None\n".format(field.name)
                source += IND + IND + "else:\n"
                source += IND + IND + IND + "self.{} = {}(vals[i])\n".format(field.name,
                                                                   conv)
                source += IND + IND + "i += 1\n"
            else:
                source += IND + IND + "count = int(vals[i])\n"
                source += IND + IND + "i += 1\n"
                source += IND + IND + "for _ in xrange(count):\n"
                source += IND + IND + IND + "obj = {}()\n".format(self.normalize_object_name(field.internal_name))
                source += IND + IND + IND + "obj.read(vals[i:i+obj._fields_count])\n"
                source += IND + IND + IND + "self._{}s.append(obj)\n".format(field.name)
                source += IND + IND + IND + "i += obj._fields_count\n"

        for field in obj.fields:
            if field.is_list:
                source += IND + "def add_{}(self, value):\n".format(field.name)
                source += IND + IND + "\"\"\"Add {}\"\"\"\n".format(
                    field.object_name)
                source += "        self._{}s.append(value)\n\n".format(
                    field.name)
            else:
                source += IND + "@property\n"
                source += IND + "def {}(self):\n".format(field.name)
                source += IND + IND + "\"\"\"Get {}\"\"\"\n".format(field.name)
                source += IND + IND + "return self._{}\n\n".format(field.name)

                asserts = ""

                # function signature
                default = "=None"
                if "default" in field.attributes:
                    default = "=" + field.attributes["default"]

                source += ""
                source += IND + "@{}.setter\n".format(field.name)
                source += IND + "def {}(self, value{}):\n".format(field.name,
                                                                default)
                source += IND + IND + "\"\"\"  Corresponds to IDD Field `{}`\n\n".format(
                    field.internal_name)

                if "note" in field.attributes:
                    for note in field.attributes["note"]:
                        source += IND + IND + "{}\n".format(note)

                if "units" in field.attributes:
                    source += IND + IND + "Unit: {}\n".format(
                        field.attributes["units"])

                def process_bound_field(field_name, op):
                    new_source = ""
                    new_assert = ""
                    if field_name in field.attributes:
                        val = field.attributes[field_name]
                        if "type" in field.attributes:
                            val = self._value2py(val, field.attributes["type"])
                        new_source = IND + IND + "{}: {} \n".format(
                            field_name.capitalize(),
                            val)
                        new_assert = IND + IND + "assert value {} {}\n".format(
                            op, val)
                    return new_source, new_assert

                s, a = process_bound_field("minimum", ">=")
                source += s
                asserts += a
                s, a = process_bound_field("minimum>", ">")
                source += s
                asserts += a
                s, a = process_bound_field("maximum<", "<")
                source += s
                asserts += a
                s, a = process_bound_field("maximum", "<=")
                source += s
                asserts += a

                if "type" in field.attributes:
                    ftype = field.attributes["type"]
                    if ftype == 'alpha':
                        asserts = IND + IND + "assert value is None or isinstance(value, {})\n".format(
                            'str') + asserts
                    if ftype == 'integer':
                        asserts = IND + IND + "assert value is None or isinstance(value, {})\n".format(
                            'int') + asserts
                    if ftype == 'real':
                        asserts = IND + IND + "assert value is None or isinstance(value, {})\n".format(
                            'float') + asserts
                    if ftype == 'choice':
                        keys = "[" + ",".join("\"{}\"".format(k) for k in field.attributes["key"]) + "]"
                        asserts = IND + IND + "assert value is None or value in {}\n".format(keys) + asserts

                        source += IND + IND + "Accepted values:\n"
                        for key in field.attributes["key"]:
                            source += IND + IND + " - {}\n".format(key)

                if "default" in field.attributes:
                    val = field.attributes["default"]
                    if "type" in field.attributes:
                        val = self._value2py(val, field.attributes["type"])
                    source += IND + IND + "Default: {}\n".format(
                        val)
                source += IND + IND + "\"\"\"\n\n"

                source += asserts + "\n"
                source += IND + IND + "self._{} = value".format(
                    field.name) + "\n\n"

        source += IND + "def _to_str(self, value):\n"
        source += IND + IND + "if value is None:\n"
        source += IND + IND + IND + "return ''\n"
        source += IND + IND + "else:\n"
        source += IND + IND + IND + "return value.__str__()\n"

        source += IND + "def export(self, top=True):\n"
        source += IND + IND + "out = []\n"
        source += IND + IND + "if top:\n"
        source += IND + IND + IND + "out.append(self.internal_name)\n"
        for field in obj.fields:
            if field.is_list:
                source += IND + IND + "out.append(str(len(self._{}s)))\n".format(field.name)
                source += IND + IND + "for obj in self._{}s:\n".format(field.name)
                source += IND + IND + IND + "out.append(obj.export(top=False))\n"
#                 source += IND + IND + "out.append(self._to_str(self._{}s))\n".format(field.name)
            else:
                source += IND + IND + "out.append(self._to_str(self.{}))\n".format(field.name)
        source += IND + IND + "return \",\".join(out)\n\n"

        source += IND + "def __str__(self):\n"
        source += IND + IND + "return self.export(True)\n"
        return source

    def generate_epw(self, objs):

        source = "class EPW(object):\n"

        list_objs = []
        for obj in objs:
            for field in obj.fields:
                if field.is_list:
                    list_objs.append(field.object_name)
        paras = ["self"]
        for obj in objs[:-1]:
            if obj.name not in list_objs:
                paras.append("{}={}()".format(self.normalize_object_name2(obj.internal_name),
                                            self.normalize_object_name(obj.internal_name)
                                            ))
        paras.append("items=[]")
        paras_str = ", ".join(paras)

        source += IND + "def __init__({}):\n".format(paras_str)
        source += IND + IND + "self._data = OrderedDict()\n"
        for obj in objs[:-1]:
            if obj.name not in list_objs:
                source += IND + IND + "self._data[\"{}\"] = {}\n".format(obj.internal_name,
                                                                         self.normalize_object_name2(obj.internal_name))
        source += IND + IND + "self._data[\"ITEMS\"] = items\n"

        source += IND + "def set(self, data_dictionary):\n"
        source += IND + IND + "if not data_dictionary.internal_name == \"ITEMS\":\n"
        source += IND + IND + IND + "self._data[data_dictionary.iternal_name] = data_dictionary\n".format(obj.internal_name)
        source += IND + IND + "else:\n"
        source += IND + IND + IND + "self._data[\"ITEMS\"].append(data_dictionary)\n".format(obj.internal_name)

        source += IND + "def create(self):\n"
        source += IND + IND + "out = []\n"

        for obj in objs[:-1]:
            if obj.name not in list_objs:
                source += IND + IND + "out.append(self._data[\"{}\"].export() + \"\\n\")\n".format(obj.internal_name)
        source += IND + IND + "for item in self._data[\"{}\"]:\n".format(objs[-1].internal_name)
        source += IND + IND + IND + "out.append(item.export(False) + \"\\n\")\n"
        source += IND + IND + "return \"\".join(out)\n"

        source += """
    def read(self, path):
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                match_obj_name = re.search(r"^([A-Z][A-Z/ \d]+),", line)
                if match_obj_name is not None:
                    obj_name = match_obj_name.group(1)
                    if obj_name in self._data:
                        data_line = line[len(obj_name) + 1:]
                        vals = data_line.strip().split(',')
                        self._data[obj_name].read(vals)
                else:
                    item = Items()
                    item.read(line.strip().split(','))
                    self._data["ITEMS"].append(item)
        """
        return source

