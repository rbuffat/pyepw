import os
import tempfile
import unittest
from pyepw.epw import {{ obj.class_name }},{% for field in obj.fields %}{% if field.is_list %}{{field.object_name}} ,{% endif %}{% endfor %}EPW


class Test{{ obj.class_name }}(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_{{ obj.var_name }}(self):

        obj = {{ obj.class_name }}()
        {%- for field in obj.fields %}
        {%- if not field.is_list %}

        {%- if field.attributes.pytype == "str" %}
        {%- if field.attributes.type == "choice" %}
        var_{{field.field_name}} = "{{ field.attributes.key[0] }}"
        {%- else %}
        var_{{field.field_name}} = "{{field.field_name }}"
        {%- endif %}
        {%- elif field.attributes.pytype == "float" %}
        {%- if (field.attributes['maximum<'] or field.attributes.maximum) and (field.attributes['minimum>'] or field.attributes.minimum) %}
        var_{{field.field_name}} = ({%if field.attributes['maximum<'] %} ({{ field.attributes["maximum<"] }} - 1.0 ) {%- else %} {{ field.attributes.maximum }} {%- endif %} + {%if field.attributes['minimum>'] %} ({{ field.attributes["minimum>"] }} + 1.0 ) {%- else %} {{ field.attributes.minimum }} {%- endif %})    * 0.5
        {%- elif (field.attributes['maximum<'] or field.attributes.maximum) and not (field.attributes['minimum>'] or field.attributes.minimum) %}
        var_{{field.field_name}} = {%if field.attributes['maximum<'] %} ({{ field.attributes["maximum<"] }} - 1.0 ) {%- else %} {{ field.attributes.maximum }} {%- endif %}
        {%- else %}
        var_{{field.field_name}} = {{loop.index}}.{{loop.index}}
        {%- endif %}
        {%- elif field.attributes.pytype == "int" %}
        {%- if (field.attributes['maximum<'] or field.attributes.maximum) and (field.attributes['minimum>'] or field.attributes.minimum) %}
        var_{{field.field_name}} = int(({%if field.attributes['maximum<'] %} ({{ field.attributes["maximum<"] }} - 1) {%- else %} {{ field.attributes.maximum }} {%- endif %} + {%if field.attributes['minimum>'] %} ({{ field.attributes["minimum>"] }} + 1) {%- else %} {{ field.attributes.minimum }} {%- endif %})    * 0.5)
        {%- elif (field.attributes['maximum<'] or field.attributes.maximum) and not (field.attributes['minimum>'] or field.attributes.minimum) %}
        var_{{field.field_name}} = {%if field.attributes['maximum<'] %} ({{ field.attributes["maximum<"] }} - 1 ) {%- else %} {{ field.attributes.maximum }} {%- endif %}
        {%- else %}
        var_{{field.field_name}} = {{loop.index}}
        {%- endif %}
        {%- endif %}
        obj.{{field.field_name}} = var_{{field.field_name}}
        {%- else %}
        {{field.field_name}}_obj = {{objs[field.object_name].class_name}}()
        {%- for field2 in objs[field.object_name].fields %}
        {%- if field2.attributes.pytype == "str" %}
        {%- if field2.attributes.type == "choice" %}
        var_{{field.field_name}}_{{field2.field_name}} = "{{ field2.attributes.key[0] }}"
        {%- else %}
        var_{{field.field_name}}_{{field2.field_name}} = "{{field2.field_name }}"
        {%- endif %}
        {%- elif field2.attributes.pytype == "float" %}
        {%- if (field2.attributes['maximum<'] or field2.attributes.maximum) and (field2.attributes['minimum>'] or field2.attributes.minimum) %}
        var_{{field.field_name}}_{{field2.field_name}} = ({%if field2.attributes['maximum<'] %} ({{ field2.attributes["maximum<"] }} - 1.0 ) {%- else %} {{ field2.attributes.maximum }} {%- endif %} + {%if field2.attributes['minimum>'] %} ({{ field2.attributes["minimum>"] }} + 1.0 ) {%- else %} {{ field2.attributes.minimum }} {%- endif %})    * 0.5
        {%- elif (field.attributes['maximum<'] or field.attributes.maximum) and not (field.attributes['minimum>'] or field.attributes.minimum) %}
        var_{{field.field_name}}_{{field2.field_name}} = {%if field2.attributes['maximum<'] %} ({{ field2.attributes["maximum<"] }} - 1.0 ) {%- else %} {{ field2.attributes.maximum }} {%- endif %}
        {%- else %}
        var_{{field.field_name}}_{{field2.field_name}} = {{loop.index}}.{{loop.index}}
        {%- endif %}
        {%- elif field2.attributes.pytype == "int" %}
        {%- if (field2.attributes['maximum<'] or field2.attributes.maximum) and (field2.attributes['minimum>'] or field2.attributes.minimum) %}
        var_{{field.field_name}}_{{field2.field_name}} = int(({%if field2.attributes['maximum<'] %} ({{ field2.attributes["maximum<"] }} - 1) {%- else %} {{ field2.attributes.maximum }} {%- endif %} + {%if field2.attributes['minimum>'] %} ({{ field2.attributes["minimum>"] }} + 1) {%- else %} {{ field2.attributes.minimum }} {%- endif %})    * 0.5)
        {%- elif (field2.attributes['maximum<'] or field2.attributes.maximum) and not (field2.attributes['minimum>'] or field2.attributes.minimum) %}
        var_{{field.field_name}}_{{field2.field_name}} = {%if field2.attributes['maximum<'] %} ({{ field2.attributes["maximum<"] }} - 1 ) {%- else %} {{ field2.attributes.maximum }} {%- endif %}
        {%- else %}
        var_{{field.field_name}}_{{field2.field_name}} = {{loop.index}}
        {%- endif %}
        {%- endif %}
        {{field.field_name}}_obj.{{field2.field_name}} = var_{{field.field_name}}_{{field2.field_name}}
        {%- endfor %}
        obj.add_{{field.field_name}}({{field.field_name}}_obj)
        {%- endif %}
        {%- endfor %}

        epw = EPW({{ obj.var_name }}=obj)
        epw.save(self.path)

        epw2 = EPW()
        epw2.read(self.path)
        {%- for field in obj.fields %}
        {%- if not field.is_list %}
            {%- if field.attributes.pytype == "str" %}
        self.assertEqual(epw2.{{obj.var_name}}.{{field.field_name}}, var_{{field.field_name}})
            {%- elif field.attributes.pytype == "int" %}
        self.assertEqual(epw2.{{obj.var_name}}.{{field.field_name}}, var_{{field.field_name}})
            {%- elif field.attributes.pytype == "float" %}
        self.assertAlmostEqual(epw2.{{obj.var_name}}.{{field.field_name}}, var_{{field.field_name}})
            {%- endif %}
        {%- else %}
        {%- for field2 in objs[field.object_name].fields %}
            {%- if field2.attributes.pytype == "str" %}
        self.assertEqual(epw2.{{obj.var_name}}.{{field.field_name}}s[0].{{field2.field_name}}, var_{{field.field_name}}_{{field2.field_name}})
            {%- elif field2.attributes.pytype == "int" %}
        self.assertEqual(epw2.{{obj.var_name}}.{{field.field_name}}s[0].{{field2.field_name}}, var_{{field.field_name}}_{{field2.field_name}})
            {%- elif field2.attributes.pytype == "float" %}
        self.assertAlmostEqual(epw2.{{obj.var_name}}.{{field.field_name}}s[0].{{field2.field_name}}, var_{{field.field_name}}_{{field2.field_name}})
            {%- endif %}
        {%- endfor %}
        {%- endif %}
        {%- endfor %}