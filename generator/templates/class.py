class {{ class_name }}(object):

    """ Corresponds to EPW IDD object `{{ internal_name }}`
    """
    _internal_name = "{{ internal_name }}"
    _field_count = {{ field_count}}

    def __init__(self):
    {%- for field in fields %}
    {%- if field.is_list %}
        self._{{field.field_name}}s = []
    {%- else %}
        self._{{field.field_name}} = None
    {%- endif %}
    {%- endfor %}

    def read(self, vals):
        i = 0
        {%- for field in fields %}
        {%- if field.is_list %}
        count = int(vals[i])
        i += 1
        for _ in xrange(count):
            obj = {{field.object_name}}()
            obj.read(vals[i:i + obj._field_count])
            self.add_{{field.field_name}}(obj)
            i += obj._field_count
        {%- else %}
        if len(vals[i]) == 0:
            self.{{field.field_name}} = None
        else:
            self.{{field.field_name}} = str(vals[i])
        i += 1
        {%- endif %}
        {%- endfor %}

    {%- for field in fields %}
    {%- if field.is_list %}

    @property
    def {{field.field_name}}s(self):
        """Get {{field.field_name}}s"""
        return self._{{field.field_name}}s

    def add_{{field.field_name}}(self, value):
        """Add TypicalOrExtremePeriod"""
        self._{{field.field_name}}s.append(value)
    {%- else %}

    @property
    def {{field.field_name}}(self):
        """Get {{field.field_name}}"""
        return self._{{field.field_name}}

    @{{field.field_name}}.setter
    def {{field.field_name}}(self, value={%if field.attributes.default %}{{field.attributes.default}}{%elif not field.attributes.default and field.attributes.missing  %}{{field.attributes.missing}}{% else %}None{% endif %}):
        """  Corresponds to IDD Field `{{field.field_name}}`
        {%- for comment in field.attributes.note %}
        {{comment}}
        {%- endfor %}
        {%- if field.attributes.type == "choice" %}

        Accepted values:
        {%- for k in field.attributes.key %}
          - {{ k }}
        {%- endfor %}
        {%- endif %}
        {%- if field.attributes.units %}
        Unit: {{ field.attributes.units }}
        {%- endif %}
        {%- if field.attributes.default %}
        Default value: {{ field.attributes.default }}
        {%- endif %}
        {%- if field.attributes.minimum %}
        value >= {{ field.attributes.minimum }}
        {%- endif %}
        {%- if field.attributes['minimum>'] %}
        value > {{ field.attributes['minimum>'] }}
        {%- endif %}
        {%- if field.attributes.maximum %}
        value <= {{ field.attributes.maximum }}
        {%- endif %}
        {%- if field.attributes['maximum<'] %}
        value < {{ field.attributes['maximum<'] }}
        {%- endif %}
        {%- if field.attributes.missing %}
        Missing value: {{ field.attributes.missing }}
        {%- endif %}
        """
        {%- if field.attributes|length > 0  %}
        if value is not None:
        {%- endif %}
            {%- if field.attributes.type == "alpha" or field.attributes.type == "choice"  %}
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type string for field {{field.field_name}}'.format(value))
            {%- elif field.attributes.type == "integer" %}
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int for field {{field.field_name}}'.format(value))
            {%- elif field.attributes.type == "real" %}
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float for field {{field.field_name}}'.format(value))
            {%- endif %}
            {%- if field.attributes.minimum %}
            if value < {{ field.attributes.minimum }}:
                raise ValueError('value need to be greater or equal {{ field.attributes.minimum }} for field {{field.field_name}}')
            {%- endif %}
            {%- if field.attributes['minimum>'] %}
            if value <= {{ field.attributes['minimum>'] }}:
                raise ValueError('value need to be greater {{ field.attributes["minimum>"] }} for field {{field.field_name}}')
            {%- endif %}
            {%- if field.attributes.maximum %}
            if value > {{ field.attributes.maximum }}:
                raise ValueError('value need to be smaller {{ field.attributes.maximum }} for field {{field.field_name}}')
            {%- endif %}
            {%- if field.attributes['maximum<'] %}
            if value >= {{ field.attributes['maximum<'] }}:
                raise ValueError('value need to be smaller or equal {{ field.attributes["maximum<"] }} for field {{field.field_name}}')
            {%- endif %}
            {%- if field.attributes.type == "choice" %}
            vals = set()
            {%- for k in field.attributes.key %}
            vals.add("{{k}}")
            {%- endfor %}
            if not value in vals:
                raise ValueError('value {} is not an accepted value for field {{field.field_name}}'.format(value))
            {%- endif %}

        self._{{field.field_name}} = value
    {%- endif %}
    {%- endfor %}

    def _to_str(self, value):
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        out = []
        if top:
            out.append(self._internal_name)
        {%- for field in fields %}
        {%- if field.is_list %}
        out.append(str(len(self.{{field.field_name}}s)))
        for obj in self.{{field.field_name}}s:
            out.append(obj.export(top=False))
        {%- else %}
        out.append(self._to_str(self.{{field.field_name}}))
        {%- endif %}
        {%- endfor %}
        return ",".join(out)

    def __str__(self):
        return self.export(True)
